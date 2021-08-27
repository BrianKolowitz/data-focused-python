---
layout: default
title: 00 - Getting Started
parent: Week 01 - Language basics, Generating Data, Storing Data
grand_parent: Lectures
nav_order: 1
---
# Getting Started

Welcome to Data Focused Python. In this guide we'll walk through all the steps you need to get started with the course. Python has a robust community which is great, but it also means there's going to be many options from python distribution to IDEs to libraries. There's no right or wrong selection, only the one that works best for you.

## Requirements

* Python 3.7

## Instructor Recommendations

You can use any combination of technology that you're most familiar with, but here's a short list or recommended options.

* Python Distribution - [Anaconda Python](https://www.anaconda.com/distribution/)
* Python IDE - [PyCharm](https://www.jetbrains.com/pycharm/)

## Setup

Depending on your configuration (Windows, MacOS, Linux, etc.) your setup will vary. There's no shortage of guides on the internet that you can follow. Here's [one](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html) direct from Jetbrains the creators of PyCharm.

## Your First Python Program

Now that you have everything setup, you'll want to dive in and create your first program. Jetbrains has a great tutorial that describes how to [Create and Running Your First Python Project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html#Creating_and_Running_Your_First_language_Project.xml). Once you're comfortable creating programs you might want to learn how to [Debug Your First Python Application](https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html#Debugging_Your_First_Python_Application.xml), [Test Your First Python Application](https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#Testing_Your_First__language__Application.xml), or even [Creat and Running Your First Django Project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-django-project.html).

[Django](https://www.djangoproject.com) is a great way to build web applications in python, but debugging, testing, and creating web applications are not required components of this course. However, these are useful skills to pick up as you become more familiar with building solutions in python.

## Cloning the Course Materials

After you're comfortable working with your Python IDE to create basic python programs, you'll want to clone the course materials from [GitHub](https://github.com/BrianKolowitz/data-focused-python). Before you can clone the repository, you'll have to install [git](https://git-scm.com/) on your local machine. [Git](https://en.wikipedia.org/wiki/Git) is a distributed version control system that's great for managing projects with distributed team members. There's a lot of great resources on how to use git. Here's 2 of my favorite interactive tutorials:

* [Try Git](https://try.github.io/levels/1/challenges/1)
* [Learn Git Branching](https://learngitbranching.js.org/)

We won't be doing any branching in this course, but I think it's important to know so I've included the link.

Once you've installed git and are somewhat comfortable with the command line tool, you can read about how to [Clone a Repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) from GitHub. 

It's as easy as:

```bash
git clone https://github.com/BrianKolowitz/data-focused-python.git
```

However, I personally like to [Add SSH Keys to GitHub](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) and clone using this command:

```bash
git clone git@github.com:BrianKolowitz/data-focused-python.git
```

## Running the Notebooks

Once the course git repository has been cloned locally you can run the course notebooks and follow along in class or try them at home. 

First, change the directory to the data-focused-python directory of your clonned repository,.

```bash
cd data-focused-python
```

Then start Jupyter

```bash
jupyter notebook
```

The [Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. If you've installed [Anaconda](https://www.anaconda.com/distribution/), [Jupyter](https://jupyter.org/index.html) is packaged as part of the distribution.

## Running the Python Interpreter

Python itself is an [interpreted programming language](https://en.wikipedia.org/wiki/Interpreted_language) which means the source code you type gets executed by the interpreter at runtime. You can start the python interpreter from any command line by executing:

```bash
python
```

I encourage you to try it out. You can follow along the official python docs [here](https://docs.python.org/3.7/tutorial/interpreter.html)

## Running the IPython Interpreter

[IPython](https://ipython.org/) builds on the Python interpreter adding advanced read-eval-print-loop (REPL) functionality [among other features](https://plot.ly/python/ipython-vs-python/#targetText=IPython%20is%20an%20interactive%20command%2Dline%20terminal%20for%20Python.&targetText=IPython%20offers%20an%20enhanced%20read,certainly%20not%20the%20only%20one).

## Executing Python Files

Using the Python interpreter is great for small problems, testing libraries, etc. but all of your code lives in memory inside the python interpreter. When the interpreter stops your code is gone forever. In order to get around this limitation you can create python script files and execute the files using the interpreter.

Create a file on your harddrive called ```hello.py```. Copy and paste this code into the file and save it.

```python
print('Hello class')
print('Welcome to 95-888')
```

You can then execute the file by typing this command into your terminal.

```bash
python hello.py
```
