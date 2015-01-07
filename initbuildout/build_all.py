#!/usr/bin/env python
import os
import sys
import argparse
import subprocess

PYTHON = sys.executable

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--project_dir',
                    help='the project directory')
arguments = parser.parse_args()

project_dir = arguments.project_dir

user = os.getlogin()

if project_dir:
    # Create log directory for the application
    log_dir = '/'.join(('/var/log', project_dir))
    try:
        subprocess.call(['sudo', 'mkdir', log_dir])
    except OSError as ex:
        if 'File exists' not in str(ex):
            print (str(ex))

    try:
        subprocess.call(['sudo', 'chown', ':'.join((user, user)), log_dir])
    except OSError as ex:
        print (str(ex))
else:
    project_dir = 'initbuildout'


REPO_PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKING_DIR = '/'.join((REPO_PARENT_DIR, project_dir))
os.chdir(WORKING_DIR)

subprocess.call([PYTHON, '../initbuildout/install_venv.py'])

try:
    os.symlink('/'.join((WORKING_DIR, 'default/buildout.cfg')), '../buildout/buildout.cfg')
except OSError as ex:
    if 'File exists' not in str(ex):
        print (str(ex))

subprocess.call([PYTHON, '../initbuildout/init_buildout.py'])
