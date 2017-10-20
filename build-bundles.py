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
import os.path
import shlex
import shutil
import sys
import subprocess
import zipfile

def build_bundle(circuitpython_tag):
    title = "Building bundle for circuitpython " + circuitpython_tag
    print()
    print(title)
    print("=" * len(title))

    current_dir = os.getcwd()
    os.chdir("circuitpython/mpy-cross")
    make = subprocess.run("git checkout {TAG} && git submodule update && make clean && make".format(TAG=circuitpython_tag), shell=True)
    os.chdir(current_dir)

    if make.returncode != 0:
        print("Unable to make mpy-cross.")
        sys.exit(1)

    MPY_CROSS = "circuitpython/mpy-cross/mpy-cross"

    build_dir = "build-" + circuitpython_tag
    build_lib_dir = os.path.join(build_dir, "lib")
    if os.path.isdir(build_dir):
        print("Deleting existing build.")
        shutil.rmtree(build_dir)
        os.mkdir(build_dir)
        os.mkdir(build_lib_dir)

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

            output_directory = build_lib_dir
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
                mpy_success = subprocess.call([MPY_CROSS, "-o", output_file, full_path])
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
                    mpy_success = subprocess.call([MPY_CROSS, "-o", output_file, full_path])
                    if mpy_success != 0:
                        print("mpy-cross failed on", full_path)
                        success = False
                        continue

    version = None
    tag = subprocess.run('git describe --tags --exact-match', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if tag.returncode == 0:
        version = tag.stdout.strip()
    else:
        commitish = subprocess.run("git log --pretty=format:'%h' -n 1", shell=True, stdout=subprocess.PIPE)
        version = commitish.stdout.strip()

    with open(os.path.join(build_lib_dir, "VERSIONS.txt"), "w") as f:
        f.write(version.decode("utf-8", "strict") + "\r\n")
        versions = subprocess.run('git submodule foreach \"git remote get-url origin && git describe --tags\"', shell=True, stdout=subprocess.PIPE)
        repo = None
        for line in versions.stdout.split(b"\n"):
            if line.startswith(b"Entering") or not line:
                continue
            if line.startswith(b"git@"):
                repo = b"https://github.com/" + line.split(b":")[1][:-len(".git")]
            elif line.startswith(b"https:"):
                repo = line.strip()[:-len(".git")]
            else:
                f.write(repo.decode("utf-8", "strict") + "/releases/tag/" + line.strip().decode("utf-8", "strict") + "\r\n")

    zip_filename = os.path.join(build_dir,
                                'adafruit-circuitpython-bundle-{TAG}-{VERSION}.zip'.format(TAG=circuitpython_tag,
                                                                                           VERSION=version.decode("utf-8", "strict")))

    with zipfile.ZipFile(zip_filename, 'w') as bundle:
        total_size += add_file(bundle, "README.txt", "lib/README.txt")
        for filename in os.listdir("update_scripts"):
            src_file = os.path.join("update_scripts", filename)
            total_size += add_file(bundle, src_file, os.path.join("lib", filename))
        for root, dirs, files in os.walk(build_lib_dir):
            ziproot = root[len(build_dir + "/"):].replace("-", "_")
            for filename in files:
                total_size += add_file(bundle, os.path.join(root, filename),
                                       os.path.join(ziproot, filename.replace("-", "_")))

    print()
    print(total_size, "B", total_size / 1024, "kiB", total_size / 1024 / 1024, "MiB")
    print("Bundled in", zip_filename)
    if not success:
        print("WARNING: some failures above")
        sys.exit(2)

def add_file(bundle, src_file, zip_name):
    global total_size
    bundle.write(src_file, zip_name)
    file_size = os.stat(src_file).st_size
    file_sector_size = file_size
    if file_size % 512 != 0:
        file_sector_size = (file_size // 512 + 1) * 512
    print(zip_name, file_size, file_sector_size)
    return file_sector_size

if __name__ == "__main__":
    tagged = input("Did you tag this release already ([y]/n)? ")
    if tagged and tagged.lower() != 'y':
        print("Go ahead and tag. I'll wait.")
        sys.exit(3)
    build_bundle("1.0.0")
    build_bundle("2.1.0")

