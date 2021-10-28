---
layout: default
title: 10 - Testing for Security Flaws in Your Application
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 10
---
# Testing for Security Flaws in Your Application
[Source](https://realpython.com/python-testing/)

Another test you will want to run on your application is checking for common security mistakes or vulnerabilities.

You can install bandit from PyPI using pip:

```bash
pip install bandit
```

You can then pass the name of your application module with the -r flag, and it will give you a summary:

```bash
bandit -r my_sum
```

As with flake8, the rules that bandit flags are configurable, and if there are any you wish to ignore, you can add the following section to your setup.cfg file with the options:

```ini
[bandit]
exclude: /test
tests: B101,B102,B301
```

You can run some of the examples from https://github.com/PyCQA/bandit/tree/master/examples by executing:

```bash
bandit -r bandit_examples

```


```python
!bandit -r bandit_examples
```

    [main]	INFO	profile include tests: None
    [main]	INFO	profile exclude tests: None
    [main]	INFO	cli include tests: None
    [main]	INFO	cli exclude tests: None
    [main]	INFO	running on Python 3.9.7
    [tester]	ERROR	Bandit internal error running: blacklist on file bandit_examples/imports-with-importlib.py at line 12: list index out of rangeTraceback (most recent call last):
      File "/Users/bk/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/bandit/core/tester.py", line 52, in run_tests
        result = test(context, test._config)
      File "/Users/bk/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/bandit/core/blacklisting.py", line 50, in blacklist
        name = context.call_args[0]
    IndexError: list index out of range
    
    [tester]	ERROR	Bandit internal error running: blacklist on file bandit_examples/imports-with-importlib.py at line 13: list index out of rangeTraceback (most recent call last):
      File "/Users/bk/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/bandit/core/tester.py", line 52, in run_tests
        result = test(context, test._config)
      File "/Users/bk/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/bandit/core/blacklisting.py", line 50, in blacklist
        name = context.call_args[0]
    IndexError: list index out of range
    
    [tester]	ERROR	Bandit internal error running: blacklist on file bandit_examples/imports-with-importlib.py at line 14: list index out of rangeTraceback (most recent call last):
      File "/Users/bk/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/bandit/core/tester.py", line 52, in run_tests
        result = test(context, test._config)
      File "/Users/bk/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/bandit/core/blacklisting.py", line 50, in blacklist
        name = context.call_args[0]
    IndexError: list index out of range
    
    [tester]	ERROR	Bandit internal error running: blacklist on file bandit_examples/imports-with-importlib.py at line 15: list index out of rangeTraceback (most recent call last):
      File "/Users/bk/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/bandit/core/tester.py", line 52, in run_tests
        result = test(context, test._config)
      File "/Users/bk/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/bandit/core/blacklisting.py", line 50, in blacklist
        name = context.call_args[0]
    IndexError: list index out of range
    
    [95mRun started:2021-10-28 19:11:44.040296[0m
    [95m
    Test results:[0m
    [93m>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
       Severity: Medium   Confidence: High
       Location: bandit_examples/eval.py:3
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b307-eval[0m
    2	
    3	print(eval("1+1"))
    4	print(eval("os.getcwd()"))
    
    --------------------------------------------------
    [93m>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
       Severity: Medium   Confidence: High
       Location: bandit_examples/eval.py:4
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b307-eval[0m
    3	print(eval("1+1"))
    4	print(eval("os.getcwd()"))
    5	print(eval("os.chmod('%s', 0777)" % 'test.txt'))
    
    --------------------------------------------------
    [93m>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
       Severity: Medium   Confidence: High
       Location: bandit_examples/eval.py:5
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b307-eval[0m
    4	print(eval("os.getcwd()"))
    5	print(eval("os.chmod('%s', 0777)" % 'test.txt'))
    6	
    
    --------------------------------------------------
    [93m>> Issue: [B309:blacklist] Use of HTTPSConnection on older versions of Python prior to 2.7.9 and 3.4.3 do not provide security, see https://wiki.openstack.org/wiki/OSSN/OSSN-0033
       Severity: Medium   Confidence: High
       Location: bandit_examples/httplib_https.py:2
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b309-httpsconnection[0m
    1	import httplib
    2	c = httplib.HTTPSConnection("example.com")
    3	
    
    --------------------------------------------------
    [93m>> Issue: [B309:blacklist] Use of HTTPSConnection on older versions of Python prior to 2.7.9 and 3.4.3 do not provide security, see https://wiki.openstack.org/wiki/OSSN/OSSN-0033
       Severity: Medium   Confidence: High
       Location: bandit_examples/httplib_https.py:5
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b309-httpsconnection[0m
    4	import http.client
    5	c = http.client.HTTPSConnection("example.com")
    6	
    
    --------------------------------------------------
    [93m>> Issue: [B309:blacklist] Use of HTTPSConnection on older versions of Python prior to 2.7.9 and 3.4.3 do not provide security, see https://wiki.openstack.org/wiki/OSSN/OSSN-0033
       Severity: Medium   Confidence: High
       Location: bandit_examples/httplib_https.py:8
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b309-httpsconnection[0m
    7	import six
    8	six.moves.http_client.HTTPSConnection("example.com")
    
    --------------------------------------------------
    [94m>> Issue: [B403:blacklist] Consider possible security implications associated with pickle module.
       Severity: Low   Confidence: High
       Location: bandit_examples/imports-with-importlib.py:3
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle[0m
    2	a = importlib.import_module('os')
    3	b = importlib.import_module('pickle')
    4	c = importlib.__import__('sys')
    
    --------------------------------------------------
    [94m>> Issue: [B404:blacklist] Consider possible security implications associated with subprocess module.
       Severity: Low   Confidence: High
       Location: bandit_examples/imports-with-importlib.py:5
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b404-import-subprocess[0m
    4	c = importlib.__import__('sys')
    5	d = importlib.__import__('subprocess')
    6	
    
    --------------------------------------------------
    [94m>> Issue: [B403:blacklist] Consider possible security implications associated with pickle module.
       Severity: Low   Confidence: High
       Location: bandit_examples/imports.py:2
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b403-import-pickle[0m
    1	import os
    2	import pickle
    3	import sys
    
    --------------------------------------------------
    [94m>> Issue: [B404:blacklist] Consider possible security implications associated with subprocess module.
       Severity: Low   Confidence: High
       Location: bandit_examples/imports.py:4
       More Info: https://bandit.readthedocs.io/en/latest/blacklists/blacklist_imports.html#b404-import-subprocess[0m
    3	import sys
    4	import subprocess
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:4
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    3	# bad
    4	query = "SELECT * FROM foo WHERE id = '%s'" % identifier
    5	query = "INSERT INTO foo VALUES ('a', 'b', '%s')" % value
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:5
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    4	query = "SELECT * FROM foo WHERE id = '%s'" % identifier
    5	query = "INSERT INTO foo VALUES ('a', 'b', '%s')" % value
    6	query = "DELETE FROM foo WHERE id = '%s'" % identifier
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:6
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    5	query = "INSERT INTO foo VALUES ('a', 'b', '%s')" % value
    6	query = "DELETE FROM foo WHERE id = '%s'" % identifier
    7	query = "UPDATE foo SET value = 'b' WHERE id = '%s'" % identifier
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:7
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    6	query = "DELETE FROM foo WHERE id = '%s'" % identifier
    7	query = "UPDATE foo SET value = 'b' WHERE id = '%s'" % identifier
    8	query = """WITH cte AS (SELECT x FROM foo)
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:8
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    7	query = "UPDATE foo SET value = 'b' WHERE id = '%s'" % identifier
    8	query = """WITH cte AS (SELECT x FROM foo)
    9	SELECT x FROM cte WHERE x = '%s'""" % identifier
    10	# bad alternate forms
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:11
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    10	# bad alternate forms
    11	query = "SELECT * FROM foo WHERE id = '" + identifier + "'"
    12	query = "SELECT * FROM foo WHERE id = '{}'".format(identifier)
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:12
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    11	query = "SELECT * FROM foo WHERE id = '" + identifier + "'"
    12	query = "SELECT * FROM foo WHERE id = '{}'".format(identifier)
    13	query = f"SELECT * FROM foo WHERE id = {tmp}"
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:13
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    12	query = "SELECT * FROM foo WHERE id = '{}'".format(identifier)
    13	query = f"SELECT * FROM foo WHERE id = {tmp}"
    14	
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Medium
       Location: bandit_examples/sql_statements-py36.py:16
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    15	# bad
    16	cur.execute("SELECT * FROM foo WHERE id = '%s'" % identifier)
    17	cur.execute("INSERT INTO foo VALUES ('a', 'b', '%s')" % value)
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Medium
       Location: bandit_examples/sql_statements-py36.py:17
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    16	cur.execute("SELECT * FROM foo WHERE id = '%s'" % identifier)
    17	cur.execute("INSERT INTO foo VALUES ('a', 'b', '%s')" % value)
    18	cur.execute("DELETE FROM foo WHERE id = '%s'" % identifier)
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Medium
       Location: bandit_examples/sql_statements-py36.py:18
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    17	cur.execute("INSERT INTO foo VALUES ('a', 'b', '%s')" % value)
    18	cur.execute("DELETE FROM foo WHERE id = '%s'" % identifier)
    19	cur.execute("UPDATE foo SET value = 'b' WHERE id = '%s'" % identifier)
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Medium
       Location: bandit_examples/sql_statements-py36.py:19
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    18	cur.execute("DELETE FROM foo WHERE id = '%s'" % identifier)
    19	cur.execute("UPDATE foo SET value = 'b' WHERE id = '%s'" % identifier)
    20	# bad alternate forms
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Medium
       Location: bandit_examples/sql_statements-py36.py:21
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    20	# bad alternate forms
    21	cur.execute("SELECT * FROM foo WHERE id = '" + identifier + "'")
    22	cur.execute("SELECT * FROM foo WHERE id = '{}'".format(identifier))
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Medium
       Location: bandit_examples/sql_statements-py36.py:22
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    21	cur.execute("SELECT * FROM foo WHERE id = '" + identifier + "'")
    22	cur.execute("SELECT * FROM foo WHERE id = '{}'".format(identifier))
    23	cur.execute(f"SELECT * FROM foo WHERE id {tmp}")
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Medium
       Location: bandit_examples/sql_statements-py36.py:23
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    22	cur.execute("SELECT * FROM foo WHERE id = '{}'".format(identifier))
    23	cur.execute(f"SELECT * FROM foo WHERE id {tmp}")
    24	
    
    --------------------------------------------------
    [93m>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
       Severity: Medium   Confidence: Low
       Location: bandit_examples/sql_statements-py36.py:37
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html[0m
    36	
    37	a()("SELECT %s FROM foo" % val)
    38	
    
    --------------------------------------------------
    [95m
    Code scanned:[0m
    	Total lines of code: 59
    	Total lines skipped (#nosec): 0
    [95m
    Run metrics:[0m
    	Total issues (by severity):
    		Undefined: 0.0
    		Low: 4.0
    		Medium: 22.0
    		High: 0.0
    	Total issues (by confidence):
    		Undefined: 0.0
    		Low: 9.0
    		Medium: 7.0
    		High: 10.0
    [95mFiles skipped (0):[0m



```python

```
