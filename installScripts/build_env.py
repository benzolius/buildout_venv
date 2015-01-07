#!/usr/bin/env python
import os
import subprocess

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO_DIR)

try:
    os.symlink('/'.join((REPO_DIR, 'default/buildout.cfg')), '../buildout/buildout.cfg')
except OSError as ex:
    if 'File exists' not in str(ex):
        print (str(ex))

subprocess.call(['../initbuildout/install_venv.py'])
subprocess.call(['../initbuildout/init_buildout.py'])
