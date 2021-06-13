========
Overview
========

Get docker images, Rum containers and Gather containers stats.

Installation
============

::

  1. git clone git@github.com:eyallev25/docker_api_exercise.git

  2. pip3 install -r requirements.txt

Running
============

  python3 tests/support/docker_utils.py


Docker
=============
To run docker:

  docker build -t my-python-app

  docker run -v /var/run/docker.sock:/var/run/docker.sock -it --rm --name my-running-app my-python-app

Usage
=====

To run the all tests run::

  pytest

  OR

  tox


To run all the tests in CI environment (output a nice HTML report in
``output/pytest``) run::

  tox -e ci


Resources List
===========

  1. https://github.com/ionelmc/cookiecutter-pylibrary
  2. https://docker-py.readthedocs.io/en/stable/

improvements
===========
  1. Error handling - docker.errors.APIError.
  2. A better understanding of python docker API.
  3. Build as a package and reading from config file - modulated probably a class structured.
  4. A better documentation.
  5. Adding pytest Fixtures to tests.
  6. Adding tests.


