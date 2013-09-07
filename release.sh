#! /bin/bash

# Create a .pypirc file in the home directory 
echo "[distutils]
index-servers =
	pypi

[pypi]" > ~/.pypirc

echo "username: " "$PYPI_USER" >> ~/.pypirc
echo "password: " "$PYPI_PWD" >> ~/.pypirc

python setup.py sdist bdist_egg upload
rm -f ~/.pypirc
