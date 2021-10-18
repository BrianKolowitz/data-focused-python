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

    total 5392
    -rw-r--r--   1 bk  staff     7863 Oct 16 10:47 00 - Getting Started.ipynb
    -rw-r--r--   1 bk  staff     6101 Oct 16 10:41 00 - Getting Started.md
    -rw-r--r--   1 bk  staff     7400 Oct 16 10:48 01.a - Terminal Application.ipynb
    -rw-r--r--   1 bk  staff     4798 Oct 16 10:41 01.a - Terminal Application.md
    -rw-r--r--   1 bk  staff    10581 Oct 16 10:49 01.b - Argparse.ipynb
    -rw-r--r--   1 bk  staff     5714 Oct 16 10:41 01.b - Argparse.md
    -rw-r--r--   1 bk  staff    16013 Oct 17 11:10 02.a - Generating Synthetic Healthcare Data.ipynb
    -rw-r--r--   1 bk  staff    13100 Oct 16 10:41 02.a - Generating Synthetic Healthcare Data.md
    -rw-r--r--   1 bk  staff  1755081 Oct 17 11:51 02.b - Generating Other Synthetic Data.ipynb
    -rw-r--r--   1 bk  staff    30228 Oct 16 10:41 02.b - Generating Other Synthetic Data.md
    drwxr-xr-x  22 bk  staff      704 Aug 26 15:35 02.b - Generating Other Synthetic Data_files
    -rw-r--r--   1 bk  staff     4197 Oct 17 11:53 02.c - Using Synthea.ipynb
    -rw-r--r--  




    0



     1 bk  staff     2640 Oct 16 10:41 02.c - Using Synthea.md
    -rw-r--r--   1 bk  staff    59673 Oct 17 20:03 03 - Getting Data from a Database.ipynb
    -rw-r--r--   1 bk  staff    12361 Oct 17 12:29 03 - Getting Data from a Database.md
    -rw-r--r--   1 bk  staff    21541 Oct 17 20:04 04 - FHIR SQL.ipynb
    -rw-r--r--   1 bk  staff    10939 Oct 17 12:29 04 - FHIR SQL.md
    -rw-r--r--   1 bk  staff    21305 Oct 17 20:21 04 - Python Testing.ipynb
    -rw-r--r--   1 bk  staff     9428 Oct 16 10:41 04 - Python Testing.md
    -rw-r--r--   1 bk  staff    10016 Aug 26 15:35 05 - Start a process in Python.ipynb
    -rw-r--r--   1 bk  staff     6217 Oct 16 10:41 05 - Start a process in Python.md
    -rw-r--r--   1 bk  staff      139 Aug 26 15:35 Domains.txt
    -rw-r--r--   1 bk  staff     6584 Aug 26 15:35 Symbolic_regression_classification_generator.py
    -rw-r--r--   1 bk  staff   207041 Aug 26 15:35 US_Cities.txt
    drwxr-xr-x   8 bk  staff      256 Oct 17 20:21 __pycache__
    -rw-r--r--   1 bk  staff      149 Aug 26 15:35 argparse_1.py
    -rw-r--r--   1 bk  staff      202 Aug 26 15:35 argparse_2.py
    -rw-r--r--   1 bk  staff      299 Aug 26 15:35 argparse_3.py
    -rw-r--r--   1 bk  staff      309 Aug 26 15:35 argparse_4.py
    -rw-r--r--   1 bk  staff      219 Aug 26 15:35 argparse_5.py
    -rw-r--r--   1 bk  staff      580 Aug 26 15:35 argparse_6.py
    -rw-r--r--   1 bk  staff   253952 Oct 17 12:55 census.db
    -rw-r--r--   1 bk  staff    12288 Oct 17 18:21 employees.db
    -rw-r--r--   1 bk  staff    90112 Oct 17 20:03 fhir.db
    drwxr-xr-x   7 bk  staff      224 Aug 26 15:35 images
    -rw-r--r--   1 bk  staff      952 Aug 26 15:35 inclass-2019-05-23.py
    -rw-r--r--   1 bk  staff      299 Aug 26 15:35 inclass-test.py
    -rw-r--r--   1 bk  staff      372 Aug 26 15:35 terminal_1.py
    -rw-r--r--   1 bk  staff      370 Aug 26 15:35 terminal_2.py
    -rw-r--r--   1 bk  staff     8192 Oct 17 20:02 test.db
    -rw-r--r--   1 bk  staff      198 Aug 26 15:35 test_class.py
    -rw-r--r--   1 bk  staff      100 Aug 26 15:35 test_sample.py
    -rw-r--r--   1 bk  staff      143 Aug 26 15:35 test_sysexit.py
    -rw-r--r--   1 bk  staff       90 Oct 17 20:17 test_tmpdir.py
    -rw-r--r--   1 bk  staff      294 Oct 17 20:21 test_tmppath.py


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

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_38017/359612823.py in <module>
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

    total 5392
    -rw-r--r--   1 bk  staff     7863 Oct 16 10:47 00 - Getting Started.ipynb
    -rw-r--r--   1 bk  staff     6101 Oct 16 10:41 00 - Getting Started.md
    -rw-r--r--   1 bk  staff     7400 Oct 16 10:48 01.a - Terminal Application.ipynb
    -rw-r--r--   1 bk  staff     4798 Oct 16 10:41 01.a - Terminal Application.md
    -rw-r--r--   1 bk  staff    10581 Oct 16 10:49 01.b - Argparse.ipynb
    -rw-r--r--   1 bk  staff     5714 Oct 16 10:41 01.b - Argparse.md
    -rw-r--r--   1 bk  staff    16013 Oct 17 11:10 02.a - Generating Synthetic Healthcare Data.ipynb
    -rw-r--r--   1 bk  staff    13100 Oct 16 10:41 02.a - Generating Synthetic Healthcare Data.md
    -rw-r--r--   1 bk  staff  1755081 Oct 17 11:51 02.b - Generating Other Synthetic Data.ipynb
    -rw-r--r--   1 bk  staff    30228 Oct 16 10:41 02.b - Generating Other Synthetic Data.md
    drwxr-xr-x  22 bk  staff      704 Aug 26 15:35 02.b - Generating Other Synthetic Data_files
    -rw-r--r--   1 bk  staff     4197 Oct 17 11:53 02.c - Using Synthea.ipynb
    -rw-r--r--   1 bk  staff     2640 Oct 16 10:41 02.c - Using Synthea.md
    -rw-r--r--   1 bk  staff    59673 Oct 17 20:03 03 - Getting Data from a Database.ipynb
    -rw-r--r--   1 bk  staff    12361 Oct 17 12:29 03 - Getting Data from a Database.md
    -rw-r--r--   1 bk  staff    21541 Oct 17 20:04 04 - FHIR SQL.ipynb
    -rw-r--r--   1 bk  staff    10939 Oct 17 12:29 04 - FHIR SQL.md
    -rw-r--r--   1 bk  staff    21305 Oct 17 20:21 04 - Python Testing.ipynb
    -rw-r--r--   1 bk  staff     9428 Oct 16 10:41 04 - Python Testing.md
    -rw-r--r--   1 bk  staff    10016 Aug 26 15:35 05 - Start a process in Python.ipynb
    -rw-r--r--   1 bk  staff     6217 Oct 16 10:41 05 - Start a process in Python.md
    -rw-r--r--   1 bk  staff      139 Aug 26 15:35 Domains.txt
    -rw-r--r--   1 bk  staff     6584 Aug 26 15:35 Symbolic_regression_classification_generator.py
    -rw-r--r--   1 bk  staff   207041 Aug 26 15:35 US_Cities.txt
    drwxr-xr-x   8 bk  staff      256 Oct 17 20:21 __pycache__
    -rw-r--r--   1 bk  staff      149 Aug 26 15:35 argparse_1.py
    -rw-r--r--   1 bk  staff      202 Aug 26 15:35 argparse_2.py
    -rw-r--r--   1 bk  staff      299 Aug 26 15:35 argparse_3.py
    -rw-r--r--   1 bk  staff      309 Aug 26 15:35 argparse_4.py
    -rw-r--r--   1 bk  staff      219 Aug 26 15:35 argparse_5.py
    -rw-r--r--   1 bk  staff      580 Aug 26 15:35 argparse_6.py
    -rw-r--r--   1 bk  staff   253952 Oct 17 12:55 census.db
    -rw-r--r--   1 bk  staff    12288 Oct 17 18:21 employees.db
    -rw-r--r--   1 bk  staff    90112 Oct 17 20:03 fhir.db
    drwxr-xr-x   7 bk  staff      224 Aug 26 15:35 images
    -rw-r--r--   1 bk  staff      952 Aug 26 15:35 inclass-2019-05-23.py
    -rw-r--r--   1 bk  staff      299 Aug 26 15:35 inclass-test.py
    -rw-r--r--   1 bk  staff      372 Aug 26 15:35 terminal_1.py
    -rw-r--r--   1 bk  staff      370 Aug 26 15:35 terminal_2.py
    -rw-r--r--   1 bk  staff     8192 Oct 17 20:02 test.db
    -rw-r--r--   1 bk  staff      198 Aug 26 15:35 test_class.py
    -rw-r--r--   1 bk  staff      100 Aug 26 15:35 test_sample.py
    -rw-r--r--   1 bk  staff      143 Aug 26 15:35 test_sysexit.py
    -rw-r--r--   1 bk  staff       90 Oct 17 20:17 test_tmpdir.py
    -rw-r--r--   1 bk  staff      294 Oct 17 20:21 test_tmppath.py
    



```python

```
