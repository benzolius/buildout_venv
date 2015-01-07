#!/usr/bin/env python
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-pl', '--package_list',
                    help='list of packages to be installed, separated by "," character')

arguments = parser.parse_args()
package_list = arguments.package_list
if package_list:
    package_list = package_list.split(',')
else:
    package_list = []

DEBIAN = 'Debian'
REDHAT = 'Red Hat'

package_manager = {DEBIAN: 'aptitude', REDHAT: 'yum'}
packages = {DEBIAN: ['python-dev'], REDHAT: ['python-devel']}

DEBIAN_FAMILY = [DEBIAN, 'Ubuntu']
REDHAT_FAMILY = ['CentOS']


def install(package):
    try:
        subprocess.call(['sudo', package_manager[family], '-y', 'install', package])
    except Exception as ex:
        print str(ex)


# Get distribution and distribution family
try:
    output = subprocess.check_output(['cat', '/etc/issue'])
    distribution = output.split(' ', 1)[0]
    if distribution in DEBIAN_FAMILY:
        family = DEBIAN
    elif distribution in REDHAT_FAMILY:
        family = REDHAT
    else:
        print ('Unknown distribution: {0}'.format(distribution))
        sys.exit(0)

    print ('Distribution: {0}, family: {1}\n'.format(distribution, family))
except Exception as ex:
    print str(ex)

# Install aptitude in order to use -y option in the same way as with yum
if family == DEBIAN:
    try:
        subprocess.call(['sudo', 'apt-get', '--force-yes', '--yes', 'install', 'aptitude'])
    except Exception as ex:
        print str(ex)

package_list = packages[family] + package_list

# Install system packages from the package list
for package in package_list:
    try:
        subprocess.call(['sudo', package_manager[family], '-y', 'install', package])
    except Exception as ex:
        print str(ex)
