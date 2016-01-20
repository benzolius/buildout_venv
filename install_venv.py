#!/usr/bin/env python
import os
import sys
import subprocess

TARGET_VERSION = '3.4'
PYTHON = sys.executable
PIP = 'pip-8.0.0'

print ('\n==========================================================================================\n')
print ('Python version: {0}'.format(sys.version))
print ('\n==========================================================================================\n')

print ('Please change the value of TARGET_VERSION and PYTHON in this script, if you would like to run with other Python version\n')
if not sys.version.startswith(TARGET_VERSION):
    sys.exit(0)


os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    os.makedirs('downloads')
    print ('Created downloads folder')
except OSError as ex:
    if 'File exists' not in str(ex):
        print (str(ex))

#os.chdir('buildout')
#print ('Change directory to buildout')

print ('\n==========================================================================================\n')
print ('Usually here should appear only 3 lines asserting version numbers:')
print ('\n==========================================================================================\n')

# Handle virtualenv
try:
    output = subprocess.check_output(['venv/bin/python', '--version'], stderr=subprocess.STDOUT)
    print ('Python interpreter version of virtualenv: {0}'.format(output))
except OSError as ex:
    if os.path.isfile('downloads/virtualenv.py') and os.stat('downloads/virtualenv.py').st_size:
        print ('downloads/virtualenv.py already downloaded')
    else:
        print ('Downloading virtualenv.py')
        subprocess.call(['wget', '--no-check-certificate', 'https://raw.github.com/pypa/virtualenv/master/virtualenv.py', '-O', 'downloads/virtualenv.py'])

    print('Installing virtualenv')
    subprocess.call([PYTHON, 'downloads/virtualenv.py', '--clear', 'venv'])

# Handle setuptools for virtualenv
try:
    output = subprocess.check_output(['venv/bin/easy_install', '--version'], stderr=subprocess.STDOUT)
    print ('Setuptools version of virtualenv: {0}'.format(output))
except OSError as ex:
    print('Installing setuptools')
    subprocess.call(['wget', '--no-check-certificate', 'https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py', '-O', 'downloads/ez_setup.py'])
    subprocess.call(['venv/bin/python', 'downloads/ez_setup.py', '--insecure'])

# Handle pip for virtualenv
try:
    output = subprocess.check_output(['venv/bin/pip', '--version'], stderr=subprocess.STDOUT)
    print ('Pip version of virtualenv: {0}'.format(output))
except OSError as ex:
    if os.path.isfile(PIP.join(('downloads/', '.tar.gz'))) and os.stat(PIP.join(('downloads/', '.tar.gz'))).st_size:
        print (PIP.join(('downloads/', '.tar.gz already downloaded')))
    else:
        print ('Downloading pip')
        subprocess.call(['wget', '--no-check-certificate', PIP.join(('https://pypi.python.org/packages/source/p/pip/', '.tar.gz')), '-O', PIP.join(('downloads/', '.tar.gz'))])

    print ('Installing pip')
    subprocess.call(['tar', 'xzvf', ''.join(('downloads/', PIP, '.tar.gz'))])
    os.chdir(PIP)
    print ('Change directory to {0}'.format(PIP))
    print ('Running: ../venv/bin/python setup.py install')
    subprocess.call(['../venv/bin/python', 'setup.py', 'install'])
    os.chdir('..')
    subprocess.call(['rm', '-rf', PIP])

# Disabling the SSL CERTIFICATION for git
subprocess.call(['git', 'config', '--global', 'http.sslVerify', 'false'])

print ('\n==========================================================================================\n')
print ('Please run the script again, if everything is ok, then it should print version numbers only')
print ('\n==========================================================================================\n')
