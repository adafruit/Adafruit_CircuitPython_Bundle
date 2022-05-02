Developing Libraries in the Bundle
==================================

Adafruit CircuitPython libraries are generally installable on a CPython interpreter with `pip` (or other package
managers). The "Blinka" libraries are compatibility layers to fill in missing pieces that are expected from
CircuitPython. Unfortunately, some of these compatibility layers may not work in all environments.

Unless you are working with all of the libaries at the same time, the easiest workflow for development is to fork an
individual library and make your changes there before submitting a PR back to the adafruit repository. If, however, you
want to programmatically modify all libraries in this bundle, it may be more efficient to do development within this
repository.

Code Hygiene
------------

Adafruit libraries are not currently fully typed. If you would like to improve the typing coverage, we suggest
`installing mypy`_. You can then run mypy from the command line or from within your editor / IDE.

.. _installing mypy: https://mypy.readthedocs.io/en/stable/getting_started.html#installing-and-running-mypy


