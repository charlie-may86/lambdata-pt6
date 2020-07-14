# Cntributor's Guide

# Installlation

Git clone and navigate into the repo from the command line:

```sh
git clone REMOTE_ADDRESS
cd /path/to/repo
```

create / activate a virtual enviroment

```sh
pipenv --python 3.7 # creates a new virtual env for the first time, also creates Pipfile
pipenv install # installs all the packages inside the Pipfile
pipenv shell # activates the virtual env

```

Run example script:
```sh
python -m my_lambdata.hello
```