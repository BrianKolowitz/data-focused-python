---
layout: default
title: 05 - Start a process in Python
parent: Week 01 - Language basics, Generating Data, Storing Data
grand_parent: Lectures
nav_order: 10
---

# Start a process in Python
[Start a process in Python](https://www.bogotobogo.com/python/python_subprocess_module.php)

Sometimes you might want to spawn a process from python and interact with the data. You might use a process to generate some files that your python application will read, or read the output of the process within your application. Doing so is relatively simple in python using the subprocess library,.

## subprocess.Popen

You can start a process in Python using the Popen function call. Open a pipe to or from command. The return value is an open file object connected to the pipe, which can be read or written depending on whether mode is 'r' (default) or 'w'.


```python
from subprocess import Popen, PIPE
process = Popen(['cat', 'scores.csv'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout.decode('utf-8'))
```

    date,home_team,home_score,away_team,away_score
    2019-05-01,Pirates,0,Cubs,10
    2019-05-15,Reds,7,Pirates,0
    


The ```process.communicate()``` call reads input and output from the process.  stdout is the process output. stderr will be written only if an error occurs.  If you want to wait for the program to finish you can call ```Popen.wait()```.


```python
from subprocess import Popen, PIPE
 
process = Popen(['cat', 'scores.csv'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
status = process.wait()
print(stdout.decode('utf-8'))
```

    date,home_team,home_score,away_team,away_score
    2019-05-01,Pirates,0,Cubs,10
    2019-05-15,Reds,7,Pirates,0
    


## subprocess.call

Subprocess has a method call() which can be used to start a program. This is basically just like the Popen class and takes all of the same arguments, but it simply wait until the command completes and gives us the return code.


```python
import subprocess
subprocess.call(['ls','-l'])
```




    0



```bash
total 181
drwxr-xr-x    2 root root  4096 Mar  3  2012 bin
drwxr-xr-x    4 root root  1024 Oct 26  2012 boot
```

The command line arguments are passed as a list of strings, which avoids the need for escaping quotes or other special characters that might be interpreted by the shell.

## subprocess.check_call()

The ```check_call()``` function works like ```call()``` except that the exit code is checked, and if it indicates an error happened then a ```CalledProcessError``` exception is raised.


```python
import subprocess
subprocess.check_call(['false'])
```


    ---------------------------------------------------------------------------

    CalledProcessError                        Traceback (most recent call last)

    <ipython-input-5-436d6a2ac26e> in <module>()
          1 import subprocess
    ----> 2 subprocess.check_call(['false'])
    

    ~/anaconda/lib/python3.6/subprocess.py in check_call(*popenargs, **kwargs)
        289         if cmd is None:
        290             cmd = popenargs[0]
    --> 291         raise CalledProcessError(retcode, cmd)
        292     return 0
        293 


    CalledProcessError: Command '['false']' returned non-zero exit status 1.


## subprocess.check_output()

The standard input and output channels for the process started by call() are bound to the parent's input and output. That means the calling program cannot capture the output of the command. To capture the output, we can use check_output() for later processing.


```python
import subprocess
output = subprocess.check_output(['ls','-l'])
print(output.decode('utf-8'))
```

    total 488
    -rw-r--r--  1 kolobj  staff   2821 Mar 19 13:04 00 - Anaconda & PyCharm Setup.ipynb
    -rw-r--r--  1 kolobj  staff   1724 Mar 23 09:17 00 - Anaconda & PyCharm Setup.md
    -rw-r--r--  1 kolobj  staff   8084 Mar 20 19:08 01.a - Terminal Application.ipynb
    -rw-r--r--  1 kolobj  staff   4651 Mar 23 09:17 01.a - Terminal Application.md
    -rw-r--r--  1 kolobj  staff  10913 Mar 20 19:47 01.b - Argparse.ipynb
    -rw-r--r--  1 kolobj  staff   5670 Mar 23 09:17 01.b - Argparse.md
    -rw-r--r--  1 kolobj  staff  16220 Mar 20 20:04 02 - Generating Synthetic Data.ipynb
    -rw-r--r--  1 kolobj  staff  12974 Mar 23 09:17 02 - Generating Synthetic Data.md
    -rw-r--r--  1 kolobj  staff   5772 Mar 23 09:29 03 - Start a process in Python.ipynb
    -rw-r--r--  1 kolobj  staff   3324 Mar 23 09:17 03 - Start a process in Python.md
    -rw-r--r--  1 kolobj  staff  14276 Mar 21 09:27 04 - Python Testing.ipynb
    -rw-r--r--  1 kolobj  staff   9337 Mar 23 09:17 04 - Python Testing.md
    drwxr-xr-x  7 kolobj  staff    224 Mar 20 20:23 __pycache__
    -rw-r--r--  1 kolobj  staff    149 Mar 19 13:04 argparse_1.py
    -rw-r--r--  1 kolobj  staff    202 Mar 19 13:04 argparse_2.py
    -rw-r--r--  1 kolobj  staff    299 Mar 19 13:04 argparse_3.py
    -rw-r--r--  1 kolobj  staff    309 Mar 19 13:04 argparse_4.py
    -rw-r--r--  1 kolobj  staff    219 Mar 19 13:04 argparse_5.py
    -rw-r--r--  1 kolobj  staff    580 Mar 19 13:04 argparse_6.py
    -rw-r--r--  1 kolobj  staff     45 Mar 19 13:04 file.txt
    drwxr-xr-x  7 kolobj  staff    224 Mar 19 13:04 images
    -rw-r--r--  1 kolobj  staff    644 Mar 19 13:04 mock.csv
    -rw-r--r--  1 kolobj  staff  45673 Mar 19 13:04 python.png
    -rw-r--r--  1 kolobj  staff    107 Mar 19 13:04 scores.csv
    -rw-r--r--  1 kolobj  staff    219 Mar 19 13:04 scores.json
    -rw-r--r--  1 kolobj  staff    547 Mar 19 13:04 scores.xml
    -rw-r--r--  1 kolobj  staff    762 Mar 19 13:04 scores.xsd
    -rw-r--r--  1 kolobj  staff    520 Mar 19 13:04 scores2.xml
    -rw-r--r--  1 kolobj  staff    406 Mar 20 19:01 terminal_1.py
    -rw-r--r--  1 kolobj  staff    404 Mar 19 13:04 terminal_2.py
    -rw-r--r--  1 kolobj  staff      0 Mar 19 13:04 test.txt
    -rw-r--r--  1 kolobj  staff    198 Mar 19 13:04 test_class.py
    -rw-r--r--  1 kolobj  staff    100 Mar 20 20:22 test_sample.py
    -rw-r--r--  1 kolobj  staff    143 Mar 19 13:04 test_sysexit.py
    -rw-r--r--  1 kolobj  staff     87 Mar 19 13:04 test_tmpdir.py
    -rw-r--r--  1 kolobj  staff    281 Mar 19 13:04 test_tmppath.py
    

