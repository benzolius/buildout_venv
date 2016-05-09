buildout_venv
=============

Python initialization scripts for virtualenv and buildout

Requirements:
~~~~~~~~~~~~~

GNU/Linux
wget
Python 2.7-3.5


Advantages:
-----------

You can install any Python package in the buildout environment or in the
virtual environment without affecting the operating system.
Nor virtualenv nor buildout will be installed in the system.


install_venv.py
---------------

Installs a virtual Python environment in a folder below the current one '../venv'.
The Python interpreter will be: ../venv/bin/python

init_buildout.py
----------------

Warning: This script was not updated for the changes in install_venv.py

Initialize a buildout environment working with the virtual environment created
by install_venv.py
The Python interpreter script will be: ../buildout/bin/py27

compilePython folder
--------------------

Contains initialization scripts and files in order to compile Python from sources by
buildout
Please have a look at README in that folder
