---
layout: default
title: 07 - Testing in Multiple Environments
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 7
---
# Writing Integration Tests
[Source](https://realpython.com/python-testing/)

So far, you’ve been testing against a single version of Python using a virtual environment with a specific set of dependencies. You might want to check that your application works on multiple versions of Python, or multiple versions of a package. Tox is an application that automates testing in multiple environments.

## Installing Tox
Tox is available on PyPI as a package to install via pip:

```bash
pip install tox
```

Now that you have Tox installed, it needs to be configured.

## Configuring Tox for Your Dependencies

Tox is configured via a configuration file in your project directory. The Tox configuration file contains the following:

* The command to run in order to execute tests
* Any additional packages required before executing
* The target Python versions to test against

Instead of having to learn the Tox configuration syntax, you can get a head start by running the quickstart application:

```bash
tox-quickstart
```

The Tox configuration tool will ask you those questions and create a file similar to the following in `tox.ini`:

```ini
[tox]
envlist = py27, py36

[testenv]
deps =

commands =
    python -m unittest discover
```

Before you can run Tox, it requires that you have a setup.py file in your application folder containing the steps to install your package. If you don’t have one, you can follow this [guide](https://packaging.python.org/tutorials/packaging-projects/#setup-py) on how to create a `setup.py` before you continue.

Alternatively, if your project is not for distribution on PyPI, you can skip this requirement by adding the following line in the `tox.ini` file under the [tox] heading:

```ini
[tox]
envlist = py27, py36
skipsdist=True
```

If you don’t create a setup.py, and your application has some dependencies from PyPI, you’ll need to specify those on a number of lines under the `[testenv]` section. For example, Django would require the following:

```ini`
[testenv]
deps = django
```

Once you have completed that stage, you’re ready to run the tests.

You can now execute Tox, and it will create two virtual environments: one for Python 2.7 and one for Python 3.6. The Tox directory is called `.tox/`. Within the `.tox/` directory, Tox will execute `python -m unittest discover` against each virtual environment.

You can run this process by calling Tox at the command line:

```bash
tox
```

Tox will output the results of your tests against each environment. The first time it runs, Tox takes a little bit of time to create the virtual environments, but once it has, the second execution will be a lot faster.

## Executing Tox

The output of Tox is quite straightforward. It creates an environment for each version, installs your dependencies, and then runs the test commands.

There are some additional command line options that are great to remember.

Run only a single environment, such as Python 3.6:

```bash
tox -e py36
```

Recreate the virtual environments, in case your dependencies have changed or site-packages is corrupt:

```bash
tox -r
```

Run Tox with less verbose output:

```bash
tox -q
```

Running Tox with more verbose output:

```bash
tox -v
```

More information on Tox can be found at the [Tox Documentation Website](https://tox.readthedocs.io/en/latest/).

See the `tox_example` folder for a complete example.


```python

```
