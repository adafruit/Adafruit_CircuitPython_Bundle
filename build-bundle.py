#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2016 Scott Shawcroft for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
import shlex
import shutil
import sys
import subprocess
import zipfile

os.chdir("micropython/mpy-cross")
make = subprocess.run(["make"])
os.chdir("../../")

if make.returncode != 0:
    print("Unable to make mpy-cross.")
    sys.exit(1)

mpy_cross = "micropython/mpy-cross/mpy-cross"

if "build" in os.listdir("."):
    print("Deleting existing build.")
    shutil.rmtree("build")
os.mkdir("build")
os.mkdir("build/lib")

success = True
total_size = 512
for subdirectory in os.listdir("libraries"):
    for library in os.listdir(os.path.join("libraries", subdirectory)):
        library_path = os.path.join("libraries", subdirectory, library)

        py_files = []
        package_files = []
        for filename in os.listdir(library_path):
            full_path = os.path.join(library_path, filename)
            if os.path.isdir(full_path) and os.path.isfile(os.path.join(full_path, "__init__.py")):
                files = os.listdir(full_path)
                files = filter(lambda x: x.endswith(".py"), files)
                files = map(lambda x: os.path.join(filename, x), files)
                package_files.extend(files)
            if filename.endswith(".py") and filename != "setup.py" and filename != "conf.py":
                py_files.append(filename)

        output_directory = os.path.join("build", "lib")
        if len(py_files) > 1:
            output_directory = os.path.join(output_directory, library)
            os.makedirs(output_directory)
            package_init = os.path.join(output_directory, "__init__.py")
            with open(package_init, 'a'):
                pass
            print(output_directory, 512)
            total_size += 512

        if len(package_files) > 1:
            for fn in package_files:
                base_dir = os.path.join(output_directory, os.path.dirname(fn))
                if not os.path.isdir(base_dir):
                    os.makedirs(base_dir)
                    print(base_dir, 512)
                    total_size += 512

        for filename in py_files:
            full_path = os.path.join(library_path, filename)
            output_file = os.path.join(output_directory, filename.replace(".py", ".mpy"))
            mpy_success = subprocess.call([mpy_cross, "-o", output_file, full_path])
            if mpy_success != 0:
                print("mpy-cross failed on", full_path)
                success = False
                continue

        for filename in package_files:
            full_path = os.path.join(library_path, filename)
            if os.stat(full_path).st_size == 0 or filename.endswith("__init__.py"):
                output_file = os.path.join(output_directory, filename)
                shutil.copyfile(full_path, output_file)
            else:
                output_file = os.path.join(output_directory, filename.replace(".py", ".mpy"))
                mpy_success = subprocess.call([mpy_cross, "-o", output_file, full_path])
                if mpy_success != 0:
                    print("mpy-cross failed on", full_path)
                    success = False
                    continue

version = None
tag = subprocess.run(shlex.split("git describe --tags --exact-match"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if tag.returncode == 0:
    version = tag.stdout.strip()
else:
    commitish = subprocess.run(shlex.split("git log --pretty=format:'%h' -n 1"), stdout=subprocess.PIPE)
    version = commitish.stdout.strip()

with open("build/lib/VERSIONS.txt", "w") as f:
    f.write(version.decode("utf-8", "strict") + "\r\n")
    versions = subprocess.run(shlex.split("git submodule foreach \"git remote get-url origin && git describe --tags\""), stdout=subprocess.PIPE)
    repo = None
    for line in versions.stdout.split(b"\n"):
        if line.startswith(b"Entering"):
            continue
        if line.startswith(b"git@"):
            repo = b"https://github.com/" + line.split(b":")[1][:-len(".git")]
        elif line.startswith(b"https:"):
            repo = line.strip()
        else:
            f.write(repo.decode("utf-8", "strict") + "/releases/tag/" + line.strip().decode("utf-8", "strict") + "\r\n")

zip_filename = 'build/adafruit-micropython-bundle-' + version.decode("utf-8", "strict") + '.zip'

def add_file(bundle, src_file, zip_name):
    global total_size
    bundle.write(src_file, zip_name)
    file_size = os.stat(src_file).st_size
    file_sector_size = file_size
    if file_size % 512 != 0:
     file_sector_size = (file_size // 512 + 1) * 512
    total_size += file_sector_size
    print(zip_name, file_size, file_sector_size)

with zipfile.ZipFile(zip_filename, 'w') as bundle:
    add_file(bundle, "README.txt", "lib/README.txt")
    for filename in os.listdir("update_scripts"):
        src_file = os.path.join("update_scripts", filename)
        add_file(bundle, src_file, os.path.join("lib", filename))
    for root, dirs, files in os.walk("build/lib"):
        ziproot = root[len("build/"):].replace("-", "_")
        for filename in files:
            add_file(bundle, os.path.join(root, filename),
                     os.path.join(ziproot, filename.replace("-", "_")))

print()
print(total_size, "B", total_size / 1024, "kiB", total_size / 1024 / 1024, "MiB")
print("Bundled in", zip_filename)
if not success:
    sys.exit(2)
