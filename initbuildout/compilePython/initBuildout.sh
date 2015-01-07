#!/bin/sh

PACKAGE_VERSION="2.7.8"

wget --no-check-certificate https://www.python.org/ftp/python/$PACKAGE_VERSION/Python-$PACKAGE_VERSION.tar.xz
mkdir -p /opt/py/py278
tar xJvf Python-$PACKAGE_VERSION.tar.xz
cd Python-$PACKAGE_VERSION/Modules
patch < ../../Setup.dist.patch
cd ../..
tar czvf Python-$PACKAGE_VERSION.tar.gz Python-$PACKAGE_VERSION

if [ -s "bin/buildout" ]; then
    echo "Buildout was initialized already"
    echo "You can run bin/buildout"
    exit 0
else
    if [ -s "bootstrap.py" ]; then
        echo "bootstrap.py already downloaded"
    else
        echo "Downloading bootstrap.py"
        wget "http://downloads.buildout.org/1/bootstrap.py" -O "bootstrap.py"
    fi
fi

python bootstrap.py
bin/buildout

echo ""
echo "==========================================================="
echo "If there were no errors, it means all is set."
echo "Now you can use the /opt/py/py278/bin/python interpreter."
echo "==========================================================="
echo ""
