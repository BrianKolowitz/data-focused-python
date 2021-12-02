---
layout: default
title: 02 - Running Python
parent: Topic 01 - Getting Started
grand_parent: Lectures
nav_order: 2
---
# Running Python

## Running the course Notebooks

Once the course git repository has been cloned locally you can run the course notebooks and follow along in class or try them at home. 

First, change the directory to the data-focused-python directory of your clonned repository,.

```bash
cd data-focused-python
```

Then start Jupyter from your terminal

```bash
jupyter-lab
```

### What is Jupyter?

The [Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. If you've installed [Anaconda](https://www.anaconda.com/distribution/), [Jupyter](https://jupyter.org/index.html) is packaged as part of the distribution.

I encourage you to review the more detailed [How To Use Jupyter Notebook – An Ultimate Guide](https://www.geeksforgeeks.org/how-to-use-jupyter-notebook-an-ultimate-guide/).

## Running the Python Interpreter

Python itself is an [interpreted programming language](https://en.wikipedia.org/wiki/Interpreted_language) which means the source code you type gets executed by the interpreter at runtime. You can start the python interpreter from any command line by executing the following in your terminal:

```bash
python
```

I encourage you to try it out. You can follow along the official python docs [here](https://docs.python.org/3.7/tutorial/interpreter.html)

## Running the IPython Interpreter

[IPython](https://ipython.org/) builds on the Python interpreter adding advanced read-eval-print-loop (REPL) functionality [among other features](https://plot.ly/python/ipython-vs-python/#targetText=IPython%20is%20an%20interactive%20command%2Dline%20terminal%20for%20Python.&targetText=IPython%20offers%20an%20enhanced%20read,certainly%20not%20the%20only%20one).

You can start the ipython interpreter by executing the following command in your terminal:

```bash
ipython
```


```python
# in anaconda
## find the location of your virtual environment
!which python
```

    /Users/bk/opt/miniconda3/envs/cmu39/bin/python



```python
## run IDLE out of that location
!/Users/bk/opt/miniconda3/envs/cmu39/bin/idle3.9 &
```

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


```python
!python hello.py
```


```python

```
