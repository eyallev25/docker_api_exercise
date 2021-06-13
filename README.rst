========
Overview
========

Get docker images, Rum containers and Gather containers stats.

Installation
============

::

  git clone git@github.com:eyallev25/docker_api_exercise.git

  pip3 install -r requirements.txt


Docker
=============
To run docker:

  docker build -t my-python-app

  docker run -v /var/run/docker.sock:/var/run/docker.sock -it --rm --name my-running-app my-python-app

Usage
=====

To run the all tests run::

  python3 tests/support/docker_utils.py

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
  2. Better understanding of python docker API.
  3. Better project modulation - probably a class structured.
  4. Better documentation.


