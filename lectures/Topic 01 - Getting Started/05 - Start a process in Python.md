---
layout: default
title: 05 - Start a process in Python
parent: Topic 01 - Getting Started
grand_parent: Lectures
nav_order: 5
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

    


The ```process.communicate()``` call reads input and output from the process.  stdout is the process output. stderr will be written only if an error occurs.  If you want to wait for the program to finish you can call ```Popen.wait()```.


```python
from subprocess import Popen, PIPE
 
process = Popen(['cat', 'scores.csv'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
status = process.wait()
print(stdout.decode('utf-8'))
```

    


## subprocess.call

Subprocess has a method call() which can be used to start a program. This is basically just like the Popen class and takes all of the same arguments, but it simply wait until the command completes and gives us the return code.


```python
import subprocess
subprocess.call(['ls','-l'])
```

    total 192
    -rw-r--r--  1 bk  staff   7977 Oct 21 09:46 01 - Getting Started.ipynb
    -rw-r--r--  1 bk  staff   7400 Oct 17 20:44 02 - Terminal Application.ipynb
    -rw-r--r--  1 bk  staff  10581 Oct 17 20:44 03 - Argparse.ipynb
    -rw-r--r--  1 bk  staff  14711 Oct 17 20:44 04 - Start a process in Python.ipynb
    -rw-r--r--  1 bk  staff    149 Aug 26 15:35 argparse_1.py
    -rw-r--r--  1 bk  staff    202 Aug 26 15:35 argparse_2.py
    -rw-r--r--  1 bk  staff    299 Aug 26 15:35 argparse_3.py
    -rw-r--r--  1 bk  staff    309 Aug 26 15:35 argparse_4.py
    -rw-r--r--  1 bk  staff    219 Aug 26 15:35 argparse_5.py
    -rw-r--r--  1 bk  staff    580 Aug 26 15:35 argparse_6.py
    -rw-r--r--  1 bk  staff    372 Aug 26 15:35 terminal_1.py
    -rw-r--r--  1 bk  staff    370 Aug 26 15:35 terminal_2.py
    -rw-r--r--  1 bk  staff    198 Aug 26 15:35 test_class.py
    -rw-r--r--  1 bk  staff    100 Aug 26 15:35 test_sample.py
    -rw-r--r--  1 bk  staff    143 Aug 26 15:35 test_sysexit.py
    -rw-r--r--  1 bk  staff     90 Oct 17 20:44 test_tmpdir.p




    0



    y
    -rw-r--r--  1 bk  staff    294 Oct 17 20:44 test_tmppath.py


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

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_91211/359612823.py in <module>
          1 import subprocess
    ----> 2 subprocess.check_call(['false'])
    

    ~/opt/miniconda3/envs/cmu39/lib/python3.9/subprocess.py in check_call(*popenargs, **kwargs)
        371         if cmd is None:
        372             cmd = popenargs[0]
    --> 373         raise CalledProcessError(retcode, cmd)
        374     return 0
        375 


    CalledProcessError: Command '['false']' returned non-zero exit status 1.


## subprocess.check_output()

The standard input and output channels for the process started by call() are bound to the parent's input and output. That means the calling program cannot capture the output of the command. To capture the output, we can use check_output() for later processing.


```python
import subprocess
output = subprocess.check_output(['ls','-l'])
print(output.decode('utf-8'))
```

    total 192
    -rw-r--r--  1 bk  staff   7977 Oct 21 09:46 01 - Getting Started.ipynb
    -rw-r--r--  1 bk  staff   7400 Oct 17 20:44 02 - Terminal Application.ipynb
    -rw-r--r--  1 bk  staff  10581 Oct 17 20:44 03 - Argparse.ipynb
    -rw-r--r--  1 bk  staff  14711 Oct 17 20:44 04 - Start a process in Python.ipynb
    -rw-r--r--  1 bk  staff    149 Aug 26 15:35 argparse_1.py
    -rw-r--r--  1 bk  staff    202 Aug 26 15:35 argparse_2.py
    -rw-r--r--  1 bk  staff    299 Aug 26 15:35 argparse_3.py
    -rw-r--r--  1 bk  staff    309 Aug 26 15:35 argparse_4.py
    -rw-r--r--  1 bk  staff    219 Aug 26 15:35 argparse_5.py
    -rw-r--r--  1 bk  staff    580 Aug 26 15:35 argparse_6.py
    -rw-r--r--  1 bk  staff    372 Aug 26 15:35 terminal_1.py
    -rw-r--r--  1 bk  staff    370 Aug 26 15:35 terminal_2.py
    -rw-r--r--  1 bk  staff    198 Aug 26 15:35 test_class.py
    -rw-r--r--  1 bk  staff    100 Aug 26 15:35 test_sample.py
    -rw-r--r--  1 bk  staff    143 Aug 26 15:35 test_sysexit.py
    -rw-r--r--  1 bk  staff     90 Oct 17 20:44 test_tmpdir.py
    -rw-r--r--  1 bk  staff    294 Oct 17 20:44 test_tmppath.py
    



```python

```
