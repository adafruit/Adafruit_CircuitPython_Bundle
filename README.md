# Adafruit CircuitPython Library Bundle

[![Doc Status](https://readthedocs.org/projects/circuitpython/badge/?version=latest)](https://circuitpython.readthedocs.io/en/latest/docs/drivers.html)
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

## CPython
**DO NOT** use this to install libraries on a Linux computer, such as the Raspberry Pi, with regular Python (aka CPython). Instead, use the python3 version of `pip` to install the libraries you want to use. It will automatically install dependencies for you. For example:

`pip3 install adafruit-circuitpython-lis3dh`

# Development

After you clone this repository you must run `git submodule init`
and then `git submodule update`.

## Updating libraries
To update the libraries run `update-submodules.sh`. The script will fetch the
latest code and update to the newest tag (not master).

To find libraries with commits that haven't been included in a release do:

    git submodule foreach "git log --oneline HEAD...origin/master"

## Adding a library
Determine the best location within `libraries` (`libraries/drivers/` or
`libraries/helpers/`)for the new library and then run:

    git submodule add <git url> libraries/<target directory>

The target directory should omit any CircuitPython specific prefixes such as
`adafruit-circuitpython` to simplify the listing.

## Removing a library
Only do this if you are replacing the module with an equivalent:

    git submodule deinit libraries/<target directory>
    git rm libraries/<target directory>

## Building the bundle
To build this bundle locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

    source .env/bin/activate

Then run the build:

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-bundle --library_location libraries --library_depth 2
