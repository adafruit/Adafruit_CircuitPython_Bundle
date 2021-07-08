#! /bin/bash

# SPDX-FileCopyrightText: 2016 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# This script updates all submodules to the latest tag (hopefully release).

# 'init' to make sure any new libraries are incorporated.
git submodule init
git submodule update
git submodule foreach git fetch --all

# Regular release tags are 'x.x.x'. Exclude tags that are alpha or beta releases
# They will contain a '-' in the tag, such as '3.0.0-beta.5'
# --exclude must be before --tags.
git submodule foreach "tag=\$(git rev-list --exclude='*-*' --tags --max-count=1); git checkout -q \$tag"
