#!/usr/bin/env python
import os
import sys
import subprocess

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(REPO_DIR)
try:
    os.symlink('/'.join((REPO_DIR, 'default', 'buildout.cfg')), '../buildout/buildout.cfg')
except OSError as ex:
    if 'File exists' not in str(ex):
        print (str(ex))

WORKING_DIR = '/'.join((os.path.dirname(REPO_DIR), 'buildout'))
os.chdir(WORKING_DIR)

VIRTUAL_PYTHON = 'venv/bin/python'

try:
    output = subprocess.check_output([VIRTUAL_PYTHON, '--version'], stderr=subprocess.STDOUT)
    print ('Python interpreter version of virtualenv: {0}'.format(output))
except OSError as ex:
    print ('Virtualenv is not installed in this folder')
    print ("Please install it by running ./install_venv.py")
    sys.exit(0)

print ('\n==========================================================================================\n')
print ('Usually here should appear only one line asserting the initialized buildout version:')
print ('\n==========================================================================================\n')

# Handle buildout
try:
    output = subprocess.check_output(['bin/buildout', '--version'], stderr=subprocess.STDOUT)
    print ('Initialized {0}'.format(output))
except OSError as ex:
    if os.path.isfile('downloads/bootstrap.py') and os.stat('downloads/bootstrap.py').st_size:
        print ('downloads/bootstrap.py already downloaded')
    else:
        print ('Downloading bootstrap.py')
        subprocess.call(['wget', '--no-check-certificate', 'http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py', '-O', 'downloads/bootstrap.py'])

    print 'Initializing buildout'
    subprocess.call([VIRTUAL_PYTHON, 'downloads/bootstrap.py'])
    subprocess.call(['bin/buildout'])

print ('\n==========================================================================================\n')
print ('Please run the script again, if everything is ok, then it should print version numbers only')
print ('and you can use the script ../buildout/bin/py27 in your source as a Python interpreter')
print ('\n==========================================================================================\n')
