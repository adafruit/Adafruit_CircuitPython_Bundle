# Adafruit CircuitPython Library Bundle

[![Doc Status](https://readthedocs.org/projects/circuitpython/badge/?version=latest)](https://circuitpython.readthedocs.io/en/latest/docs/drivers.html) [![Gitter](https://badges.gitter.im/adafruit/circuitpython.svg)](https://gitter.im/adafruit/circuitpython?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Discord](https://img.shields.io/discord/327254708534116352.svg)](https://discord.gg/nBQh6qu)

This repo bundles a bunch of useful CircuitPython libraries into an easy to
download zip file. CircuitPython boards can ship with the contents of the zip to
make it easy to provide a lot of libraries by default.

# Use
To use the bundle download the zip (not source zip) from the
[latest release](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest),
unzip it and copy over the subfolders, such as `lib`, into the root of your
CircuitPython device. Make sure to indicate that it should be merged with the
existing folder when it exists.

# Development

After you clone this repository you must run `git submodule --init` on update
also do `git submodule update`.

## Updating libraries
To update the libraries run `update-submodules.sh`. The script will fetch the
latest code and update to the newest tag (not master).

## Adding a library
Determine the best location within `libraries` for the new library and then run:

    git submodule add <git url> libraries/<target directory>

The target directory should omit any MicroPython or CircuitPython specific
prefixes such as `adafruit-micropython` to simplify the listing.

## Removing a library
Only do this if you are replacing the module with an equivalent:

    git submodule deinit libraries/<target directory>
    git rm libraries/<target directory>

## Building the bundle
To build the bundle run `build-bundle.py` it requires Python 3.5+ and will
produce a zip file in `build`. The file structure of the zip will not be
identical to the source `libraries` directory in order to save space. Libraries
with a single source will not be placed in their own directory.
