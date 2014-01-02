#!/usr/bin/python

""" Exercise 46 """

str="""
Pip: It is a package management system for installing and managing the software
packages written in Python.
Pip has command-line interface for package install-uninstall
pip install <python-package-name>
pip uninstall <python-package-name>
pip install -r requirements.txt - where the text file can have a full list of
pckages to be installed or managed through the Pip.

Index for managing the Python Packages: Python Package Index
.egg files: An archive format for python packages

1. Install the setuptools:
$ wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python
- The above command installs the setuptools to the system python
- Confirm that the easy_install command has now become available after the SetupTools installation
2. Install the pip using easy_install
$ easy_install pip

VirtualEnv: These are used to create isolated python environments to avoid dependency and version
conflicts - automatically taking care of the permission issues.
1. Install virtualenv and virtualenvwrapper using pip
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper
virtualenvwrapper: It offers some nice commands to manage and handle your python virtual envs

2. Set the WORKON_HOME env variable. This is the directory in which the python virtual environments
are to be stored.
$ export WORKON_HOME='~/.virtualenvs'
$ mkdir $WORKON_HOME
Put the export command in the ~/.bashrc file as well.

3. To use virtualenvwrapper, we need to import its functions in the ~/.bashrc
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

4. Load the new ~/.bashrc to also include the virtualenvwrapper functionality
$ source ~/.bashrc 

5. Set up the new virtual python env! 
$ mkvirtualenv test
--> The env will be created and now the prompt contains the env name at the beginning!
$ deactivate 
--> This takes you out of the current virtual python env
$ workon test
--> Takes you back to the python virtual env that you want to wotk on
$ rmvirtualenv test
--> To delte and remove the virtualenv "test" completely

NOTE: Never call Pip with sudo in the virtual env - since that will invoke the system Pip!

Distribute, Disutils, SetupTools (and related hell)
1. Distutils: Standard tool used for packaging python packages.
Its included in python installations.
It lacks some fancy features - so things started to complicate.
2. SetupTools: Fork of distutils + a bunch of other features. (Installed in Section1 above)
SetupTools is not included in standard libraries of python installations.
3. Distribute: A fork of SetupTools because some people were impatient!
Distribute has been forked back into SetupTools - so you dn't need distribute after SetupTools
installation.
4. Distutils2: Fork of distutils - but has added features from SetupTools and distribute.
Distutils2 will probably kill off the disutils project making SetupTools look like an idiot.

Nose: It is a framework that extends the unittest framework to make testing easier.
1. Install nose using pip - letting it handle all the dependencies and everything.
$ sudo pip install nose
2. Third parties have nose-plugin
The pip install nose - installs the nose libraries and the "nosetests" script which can be used 
to discover and run tests.
 	
References:
1. Pip: https://pypi.python.org/pypi/setuptools
2. VirtualEnv: http://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu
3. Pip: http://guide.python-distribute.org/ (Hitchhiker's Guide to Python Packaging)
4. Distutils etc.: http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2
5. Nose: https://nose.readthedocs.org/en/latest/
"""
print str

"""
Test Run:
Run the program once to ensure no errors are in the program
$ ./e46.py

"""

