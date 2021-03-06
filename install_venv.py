#!/usr/bin/env python
import os
import sys
import subprocess

PYTHON = sys.executable

print ('\n==========================================================================================\n')
print ('Python version: {0}'.format(sys.version))
print ('\n==========================================================================================\n')


os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    os.makedirs('downloads')
    print ('Created downloads folder')
except OSError as ex:
    if 'File exists' not in str(ex):
        print (str(ex))

# os.chdir('buildout')
# print ('Change directory to buildout')

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
        try:
            subprocess.call(['wget', '--no-check-certificate', 'https://raw.github.com/pypa/virtualenv/master/virtualenv.py', '-O', 'downloads/virtualenv.py'])
        except Exception as ex:
            print (str(ex))
            print ('Trying by curl:')
            try:
                subprocess.call('curl -sL https://raw.github.com/pypa/virtualenv/master/virtualenv.py > downloads/virtualenv.py', shell=True)
            except Exception as ex:
                print (str(ex))

    print('Installing virtualenv')
    subprocess.call([PYTHON, 'downloads/virtualenv.py', '--clear', 'venv'])

# Print setuptools version
try:
    output = subprocess.check_output(['venv/bin/easy_install', '--version'], stderr=subprocess.STDOUT)
    print ('Setuptools version of virtualenv: {0}'.format(output))
except OSError as ex:
    print('Setuptools will be installed by get-pip.py')

# Handle pip for virtualenv
try:
    output = subprocess.check_output(['venv/bin/pip', '--version'], stderr=subprocess.STDOUT)
    print ('Pip version of virtualenv: {0}'.format(output))
except OSError as ex:
    if os.path.isfile('downloads/get-pip.py') and os.stat('downloads/get-pip.py').st_size:
        print ('downloads/get-pip.py already downloaded')
    else:
        print ('Downloading get-pip.py')
        try:
            subprocess.call(['wget', '--no-check-certificate', 'https://bootstrap.pypa.io/get-pip.py', '-O', 'downloads/get-pip.py'])
        except Exception as ex:
            print (str(ex))
            print ('Trying by curl:')
            try:
                subprocess.call('curl -sL https://bootstrap.pypa.io/get-pip.py > downloads/get-pip.py', shell=True)
            except Exception as ex:
                print (str(ex))

    print ('Installing pip')
    print ('Running: venv/bin/python downloads/get-pip.py')
    subprocess.call(['venv/bin/python', 'downloads/get-pip.py'])

# Disabling the SSL CERTIFICATION for git
subprocess.call(['git', 'config', '--global', 'http.sslVerify', 'false'])

print ('\n==========================================================================================\n')
print ('Please run the script again, if everything is ok, then it should print version numbers only')
print ('\n==========================================================================================\n')
