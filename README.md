# Adafruit's MicroPython Bundle
This repo bundles a bunch of useful MicroPython libraries into an easy to
download zip file. MicroPython boards can ship with the contents of the zip to
make it easy to provide a lot of libraries by default.

# Use
To use the bundle download the zip (not source zip) from the latest release,
unzip it and copy over the subfolders into the root of your MicroPython device.

# Development

After you clone this repository you must run `git submodule --init` on update
also do `git submodule update`.

## Updating libraries
To update the libraries run `update-submodules.sh`. The script will fetch the
latest code and update to the newest tag (not master).

## Adding a library
Determine the best location within `libraries` for the new library and then run:

    git submodule add <git url> libraries/<target directory>

The target directory should omit any micropython specific prefixes such as
`micropython-adafruit` to simplify the listing.

## Building the bundle
To build the bundle run `build-bundle.py` it requires Python 3.5+ and will
produce a zip file in `build`. The file structure of the zip will not be
identical to the source `libraries` directory in order to save space. Libraries
with a single source will not be placed in their own directory.
