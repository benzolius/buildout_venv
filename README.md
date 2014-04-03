buildout_venv
=============

Python initialization scripts for virtualenv and buildout

Requirements:
~~~~~~~~~~~~~

Python 2.7


Advantages:
-----------

You can install any Python package in the buildout environment or in the
virtual environment without affecting the operating system.
Nor virtualenv nor buildout will be installed in the system.


install_venv.py
---------------

Installs a virtual Python environment in a sibling folder 'buildout/venv'.
The Python interpreter will be: ../buildout/venv/bin/python

init_buildout.py
----------------

Initialize a buildout environment working with the virtual environment created
by install_venv.py
The Python interpreter script will be: ../buildout/bin/py27
