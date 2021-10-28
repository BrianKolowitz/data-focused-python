---
layout: default
title: 01 - Python Code Quality Tools and Best Practices
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 1
---
# Python Code Quality
Tools and Best Practices
[Source](https://realpython.com/python-code-quality/)

## What is Code Quality?

Of course you want quality code, who wouldn’t? But to improve code quality, we have to define what it is.

A quick Google search yields many results defining code quality. As it turns out, the term can mean many different things to people.

One way of trying to define code quality is to look at one end of the spectrum: high-quality code. Hopefully, you can agree on the following high-quality code identifiers:

* It does what it is supposed to do.
* It does not contain defects or problems.
* It is easy to read, maintain, and extend.

These three identifiers, while simplistic, seem to be generally agreed upon. In an effort to expand these ideas further, let’s delve into why each one matters in the realm of software.

## Why Does Code Quality Matter?
To determine why high-quality code is important, let’s revisit those identifiers. We’ll see what happens when code doesn’t meet them.

### It does not do what it is supposed to do

Meeting requirements is the basis of any product, software or otherwise. We make software to do something. If in the end, it doesn’t do it… well it’s definitely not high quality. If it doesn’t meet basic requirements, it’s hard to even call it low quality.

### It does contain defects and problems

If something you’re using has issues or causes you problems, you probably wouldn’t call it high-quality. In fact, if it’s bad enough, you may stop using it altogether.

For the sake of not using software as an example, let’s say your vacuum works great on regular carpet. It cleans up all the dust and cat hair. One fateful night the cat knocks over a plant, spilling dirt everywhere. When you try to use the vacuum to clean the pile of dirt, it breaks, spewing the dirt everywhere.

While the vacuum worked under some circumstances, it didn’t efficiently handle the occasional extra load. Thus, you wouldn’t call it a high-quality vacuum cleaner.

That is a problem we want to avoid in our code. If things break on edge cases and defects cause unwanted behavior, we don’t have a high-quality product.

### It is difficult to read, maintain, or extend

Imagine this: a customer requests a new feature. The person who wrote the original code is gone. The person who has replaced them now has to make sense of the code that’s already there. That person is you.

If the code is easy to comprehend, you’ll be able to analyze the problem and come up with a solution much quicker. If the code is complex and convoluted, you’ll probably take longer and possibly make some wrong assumptions.

It’s also nice if it’s easy to add the new feature without disrupting previous features. If the code is not easy to extend, your new feature could break other things.

No one wants to be in the position where they have to read, maintain, or extend low-quality code. It means more headaches and more work for everyone.

It’s bad enough that you have to deal with low-quality code, but don’t put someone else in the same situation. You can improve the quality of code that you write.

If you work with a team of developers, you can start putting into place methods to ensure better overall code quality. Assuming that you have their support, of course.

## How to Improve Python Code Quality

There are a few things to consider on our journey for high-quality code. First, this journey is not one of pure objectivity. There are some strong feelings of what high-quality code looks like.

While everyone can hopefully agree on the identifiers mentioned above, the way they get achieved is a subjective road. The most opinionated topics usually come up when you talk about achieving readability, maintenance, and extensibility.

So keep in mind that while this article will try to stay objective throughout, there is a very-opinionated world out there when it comes to code.

So, let’s start with the most opinionated topic: code style.

### Style Guides

Ah, yes. The age-old question: [spaces or tabs](https://blog.codinghorror.com/death-to-the-space-infidels/)?

Regardless of your personal view on how to represent whitespace, it’s safe to assume that you at least want consistency in code.

A style guide serves the purpose of defining a consistent way to write your code. Typically this is all cosmetic, meaning it doesn’t change the logical outcome of the code. Although, some stylistic choices do avoid common logical mistakes.

Style guides serve to help facilitate the goal of making code easy to read, maintain, and extend.

As far as Python goes, there is a well-accepted standard. It was written, in part, by the author of the Python programming language itself.

[PEP 8](http://pep8.org/) provides coding conventions for Python code. It is fairly common for Python code to follow this style guide. It’s a great place to start since it’s already well-defined.

A sister Python Enhancement Proposal, [PEP 257](https://www.python.org/dev/peps/pep-0257/) describes conventions for Python’s docstrings, which are strings intended to [document](https://realpython.com/documenting-python-code/) modules, classes, functions, and methods. As an added bonus, if docstrings are consistent, there are tools capable of generating documentation directly from the code.

All these guides do is define a way to style code. But how do you enforce it? And what about defects and problems in the code, how can you detect those? That’s where linters come in.

## Linters

### What is a Linter?

First, let’s talk about lint. Those tiny, annoying little defects that somehow get all over your clothes. Clothes look and feel much better without all that lint. Your code is no different. Little mistakes, stylistic inconsistencies, and dangerous logic don’t make your code feel great.

But we all make mistakes. You can’t expect yourself to always catch them in time. Mistyped [variable](https://realpython.com/python-variables/) names, forgetting a closing bracket, incorrect tabbing in Python, calling a function with the wrong number of arguments, the list goes on and on. Linters help to identify those problem areas.

Additionally, most [editors and IDEs](https://realpython.com/python-ides-code-editors-guide/) have the ability to run linters in the background as you type. This results in an environment capable of highlighting, underlining, or otherwise identifying problem areas in the code before you run it. It is like an advanced spell-check for code. It underlines issues in squiggly red lines much like your favorite word processor does.

Linters analyze code to detect various categories of lint. Those categories can be broadly defined as the following:

1. Logical Lint
    1. Code errors
    2. Code with potentially unintended results
    3. Dangerous code patterns
2. Stylistic Lint
    1. Code not conforming to defined conventions

There are also code analysis tools that provide other insights into your code. While maybe not linters by definition, these tools are usually used side-by-side with linters. They too hope to improve the quality of the code.

Finally, there are tools that automatically format code to some specification. These automated tools ensure that our inferior human minds don’t mess up conventions.

### What Are My Linter Options For Python?

Before delving into your options, it’s important to recognize that some “linters” are just multiple linters packaged nicely together. Some popular examples of those combo-linters are the following:

**Flake8**: Capable of detecting both logical and stylistic lint. It adds the style and complexity checks of pycodestyle to the logical lint detection of PyFlakes. It combines the following linters:

* PyFlakes
* pycodestyle (formerly pep8)
* Mccabe

**Pylama**: A code audit tool composed of a large number of linters and other tools for analyzing code. It combines the following:

* pycodestyle (formerly pep8)
* pydocstyle (formerly pep257)
* PyFlakes
* Mccabe
* Pylint
* Radon
* gjslint

Here are some stand-alone linters categorized with brief descriptions:


| Linter | Category | Description |
| --- | --- | --- |
| Pylint | Logical & Stylistic | Checks for errors, tries to enforce a coding standard, looks for code smells |
| PyFlakes | Logical | Analyzes programs and detects various errors |
| pycodestyle | Stylistic | Checks against some of the style conventions in PEP 8 |
| pydocstyle | Stylistic | Checks compliance with Python docstring conventions |
| Bandit | Logical | Analyzes code to find common security issues |
| MyPy | Logical | Checks for optionally-enforced static types |

And here are some code analysis and formatting tools:

| Tool | Category | Description |
| --- | --- | --- |
| Mccabe | Analytical | Checks McCabe complexity |
| Radon | Analytical | Analyzes code for various metrics (lines of code, complexity, and so on) |
| Black | Formatter | Formats Python code without compromise |
| Isort | Formatter | Formats imports by sorting alphabetically and separating into sections |

### Comparing Python Linters

Let’s get a better idea of what different linters are capable of catching and what the output looks like. To do this, I ran the same code through a handful of different linters with the default settings.

See [code_with_lint.py](code_with_lint.py) for an example of a file with multiple stylistic issues.

The comparison below shows the linters I used and their runtime for analyzing the above file. I should point out that these aren’t all entirely comparable as they serve different purposes. PyFlakes, for example, does not identify stylistic errors like Pylint does.

## Pylint

Pylint is one of the oldest linters (circa 2006) and is still well-maintained. Some might call this software battle-hardened. It’s been around long enough that contributors have fixed most major bugs and the core features are well-developed.

The common complaints against Pylint are that it is slow, too verbose by default, and takes a lot of configuration to get it working the way you want. Slowness aside, the other complaints are somewhat of a double-edged sword. Verbosity can be because of thoroughness. Lots of configuration can mean lots of adaptability to your preferences.


```python
!pylint code_with_lint.py
```

    ************* Module code_with_lint
    code_with_lint.py:12:0: W0311: Bad indentation. Found 3 spaces, expected 4 (bad-indentation)
    code_with_lint.py:15:0: W0311: Bad indentation. Found 3 spaces, expected 4 (bad-indentation)
    code_with_lint.py:16:0: W0311: Bad indentation. Found 3 spaces, expected 4 (bad-indentation)
    code_with_lint.py:17:0: W0311: Bad indentation. Found 3 spaces, expected 4 (bad-indentation)
    code_with_lint.py:18:0: W0311: Bad indentation. Found 3 spaces, expected 4 (bad-indentation)
    code_with_lint.py:19:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:22:0: W0311: Bad indentation. Found 3 spaces, expected 4 (bad-indentation)
    code_with_lint.py:27:0: W0311: Bad indentation. Found 3 spaces, expected 4 (bad-indentation)
    code_with_lint.py:28:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:29:0: W0311: Bad indentation. Found 11 spaces, expected 12 (bad-indentation)
    code_with_lint.py:29:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
    code_with_lint.py:30:0: W0311: Bad indentation. Found 11 spaces, expected 12 (bad-indentation)
    code_with_lint.py:31:0: W0311: Bad indentation. Found 15 spaces, expected 16 (bad-indentation)
    code_with_lint.py:32:0: W0311: Bad indentation. Found 11 spaces, expected 12 (bad-indentation)
    code_with_lint.py:33:0: W0311: Bad indentation. Found 15 spaces, expected 16 (bad-indentation)
    code_with_lint.py:33:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
    code_with_lint.py:35:0: W0311: Bad indentation. Found 11 spaces, expected 12 (bad-indentation)
    code_with_lint.py:35:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
    code_with_lint.py:38:0: W0311: Bad indentation. Found 3 spaces, expected 4 (bad-indentation)
    code_with_lint.py:39:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:40:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:41:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:42:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:43:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:44:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:45:0: C0304: Final newline missing (missing-final-newline)
    code_with_lint.py:45:0: W0311: Bad indentation. Found 7 spaces, expected 8 (bad-indentation)
    code_with_lint.py:6:0: W0622: Redefining built-in 'pow' (redefined-builtin)
    code_with_lint.py:6:0: W0401: Wildcard import math (wildcard-import)
    code_with_lint.py:9:0: C0103: Constant name "some_global_var" doesn't conform to UPPER_CASE naming style (invalid-name)
    code_with_lint.py:15:3: W0621: Redefining name 'some_global_var' from outer scope (line 9) (redefined-outer-name)
    code_with_lint.py:11:0: C0103: Argument name "x" doesn't conform to snake_case naming style (invalid-name)
    code_with_lint.py:11:0: C0103: Argument name "y" doesn't conform to snake_case naming style (invalid-name)
    code_with_lint.py:18:3: W0101: Unreachable code (unreachable)
    code_with_lint.py:15:3: W0612: Unused variable 'some_global_var' (unused-variable)
    code_with_lint.py:21:0: C0103: Argument name "x" doesn't conform to snake_case naming style (invalid-name)
    code_with_lint.py:21:0: C0103: Argument name "y" doesn't conform to snake_case naming style (invalid-name)
    code_with_lint.py:27:6: C0121: Comparison 'x != None' should be 'x is not None' (singleton-comparison)
    code_with_lint.py:30:11: R1705: Unnecessary "else" after "return" (no-else-return)
    code_with_lint.py:21:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
    code_with_lint.py:37:0: C0115: Missing class docstring (missing-class-docstring)
    code_with_lint.py:42:7: W0621: Redefining name 'time' from outer scope (line 7) (redefined-outer-name)
    code_with_lint.py:42:14: E0601: Using variable 'time' before assignment (used-before-assignment)
    code_with_lint.py:43:7: C0415: Import outside toplevel (datetime.datetime) (import-outside-toplevel)
    code_with_lint.py:38:3: R1711: Useless return at end of function or method (useless-return)
    code_with_lint.py:38:49: W0613: Unused argument 'verbose' (unused-argument)
    code_with_lint.py:41:7: W0612: Unused variable 'list_comprehension' (unused-variable)
    code_with_lint.py:44:7: W0612: Unused variable 'date_and_time' (unused-variable)
    code_with_lint.py:37:0: R0903: Too few public methods (0/2) (too-few-public-methods)
    code_with_lint.py:5:0: W0611: Unused import io (unused-import)
    code_with_lint.py:6:0: W0614: Unused import acos from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import acosh from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import asin from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import asinh from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import atan from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import atan2 from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import atanh from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import ceil from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import comb from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import copysign from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import cos from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import cosh from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import degrees from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import dist from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import e from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import erf from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import erfc from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import exp from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import expm1 from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import fabs from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import factorial from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import floor from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import fmod from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import frexp from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import fsum from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import gamma from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import gcd from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import hypot from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import inf from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import isclose from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import isfinite from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import isinf from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import isnan from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import isqrt from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import lcm from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import ldexp from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import lgamma from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import log from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import log10 from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import log1p from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import log2 from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import modf from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import nan from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import nextafter from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import perm from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import pow from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import prod from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import radians from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import remainder from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import sin from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import sinh from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import sqrt from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import tan from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import tanh from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import tau from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import trunc from wildcard import (unused-wildcard-import)
    code_with_lint.py:6:0: W0614: Unused import ulp from wildcard import (unused-wildcard-import)
    code_with_lint.py:7:0: W0611: Unused time imported from time (unused-import)
    
    ----------------------------------------------------------------------
    Your code has been rated at -31.48/10 (previous run: -31.48/10, +0.00)
    
    [0m

## PyFlakes

Pyflakes “makes a simple promise: it will never complain about style, and it will try very, very hard to never emit false positives”. This means that Pyflakes won’t tell you about missing docstrings or argument names not conforming to a naming style. It focuses on logical code issues and potential errors.

The benefit here is speed. PyFlakes runs in a fraction of the time Pylint takes.


```python
!python -m pyflakes code_with_lint.py
```

    code_with_lint.py:5:1 'io' imported but unused
    code_with_lint.py:6:1 'from math import *' used; unable to detect undefined names
    code_with_lint.py:15:4 local variable 'some_global_var' is assigned to but never used
    code_with_lint.py:41:43 'pi' may be undefined, or defined from star imports: math
    code_with_lint.py:41:8 local variable 'list_comprehension' is assigned to but never used
    code_with_lint.py:42:15 local variable 'time' defined in enclosing scope on line 7 referenced before assignment
    code_with_lint.py:42:8 local variable 'time' is assigned to but never used
    code_with_lint.py:44:8 local variable 'date_and_time' is assigned to but never used


## pycodestyle (formerly pep8)

Used to check some style conventions from [PEP8](http://pep8.org/). Naming conventions are not checked and neither are docstrings. The errors and warnings it does catch are categorized in this [table](https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes).


```python
!pycodestyle code_with_lint.py
```

    code_with_lint.py:11:1: E302 expected 2 blank lines, found 1
    code_with_lint.py:12:4: E111 indentation is not a multiple of 4
    code_with_lint.py:15:4: E111 indentation is not a multiple of 4
    code_with_lint.py:16:4: E111 indentation is not a multiple of 4
    code_with_lint.py:16:14: E225 missing whitespace around operator
    code_with_lint.py:17:4: E111 indentation is not a multiple of 4
    code_with_lint.py:18:4: E111 indentation is not a multiple of 4
    code_with_lint.py:19:8: E111 indentation is not a multiple of 4
    code_with_lint.py:21:1: E302 expected 2 blank lines, found 1
    code_with_lint.py:22:4: E111 indentation is not a multiple of 4
    code_with_lint.py:27:4: E111 indentation is not a multiple of 4
    code_with_lint.py:27:9: E711 comparison to None should be 'if cond is not None:'
    code_with_lint.py:28:8: E111 indentation is not a multiple of 4
    code_with_lint.py:29:12: E111 indentation is not a multiple of 4
    code_with_lint.py:29:24: E703 statement ends with a semicolon
    code_with_lint.py:30:12: E111 indentation is not a multiple of 4
    code_with_lint.py:31:16: E111 indentation is not a multiple of 4
    code_with_lint.py:32:12: E111 indentation is not a multiple of 4
    code_with_lint.py:33:16: E111 indentation is not a multiple of 4
    code_with_lint.py:33:23: E201 whitespace after '('
    code_with_lint.py:35:12: E111 indentation is not a multiple of 4
    code_with_lint.py:37:1: E302 expected 2 blank lines, found 1
    code_with_lint.py:38:4: E111 indentation is not a multiple of 4
    code_with_lint.py:38:57: E251 unexpected spaces around keyword / parameter equals
    code_with_lint.py:38:59: E251 unexpected spaces around keyword / parameter equals
    code_with_lint.py:39:8: E111 indentation is not a multiple of 4
    code_with_lint.py:39:27: E221 multiple spaces before operator
    code_with_lint.py:39:30: E222 multiple spaces after operator
    code_with_lint.py:40:8: E111 indentation is not a multiple of 4
    code_with_lint.py:40:21: E221 multiple spaces before operator
    code_with_lint.py:40:30: E222 multiple spaces after operator
    code_with_lint.py:41:8: E111 indentation is not a multiple of 4
    code_with_lint.py:41:80: E501 line too long (82 > 79 characters)
    code_with_lint.py:42:8: E111 indentation is not a multiple of 4
    code_with_lint.py:43:8: E111 indentation is not a multiple of 4
    code_with_lint.py:44:8: E111 indentation is not a multiple of 4
    code_with_lint.py:45:8: E111 indentation is not a multiple of 4
    code_with_lint.py:45:14: W292 no newline at end of file


### flake8

Flake8 is a Python library that wraps PyFlakes, pycodestyle and Ned Batchelder's McCabe script. It is a great toolkit for checking your code base against coding style (PEP8), programming errors (like “library imported but unused” and “Undefined name”) and to check cyclomatic complexity.


```python
!flake8 code_with_lint.py
```

    code_with_lint.py:5:1: F401 'io' imported but unused
    code_with_lint.py:6:1: F403 'from math import *' used; unable to detect undefined names
    code_with_lint.py:11:1: E302 expected 2 blank lines, found 1
    code_with_lint.py:12:4: E111 indentation is not a multiple of 4
    code_with_lint.py:15:4: F841 local variable 'some_global_var' is assigned to but never used
    code_with_lint.py:15:4: E111 indentation is not a multiple of 4
    code_with_lint.py:16:4: E111 indentation is not a multiple of 4
    code_with_lint.py:16:14: E225 missing whitespace around operator
    code_with_lint.py:17:4: E111 indentation is not a multiple of 4
    code_with_lint.py:18:4: E111 indentation is not a multiple of 4
    code_with_lint.py:19:8: E111 indentation is not a multiple of 4
    code_with_lint.py:21:1: E302 expected 2 blank lines, found 1
    code_with_lint.py:22:4: E111 indentation is not a multiple of 4
    code_with_lint.py:27:4: E111 indentation is not a multiple of 4
    code_with_lint.py:27:9: E711 comparison to None should be 'if cond is not None:'
    code_with_lint.py:28:8: E111 indentation is not a multiple of 4
    code_with_lint.py:29:12: E111 indentation is not a multiple of 4
    code_with_lint.py:29:24: E703 statement ends with a semicolon
    code_with_lint.py:30:12: E111 indentation is not a multiple of 4
    code_with_lint.py:31:16: E111 indentation is not a multiple of 4
    code_with_lint.py:32:12: E111 indentation is not a multiple of 4
    code_with_lint.py:33:16: E111 indentation is not a multiple of 4
    code_with_lint.py:33:23: E201 whitespace after '('
    code_with_lint.py:35:12: E111 indentation is not a multiple of 4
    code_with_lint.py:37:1: E302 expected 2 blank lines, found 1
    code_with_lint.py:38:4: E111 indentation is not a multiple of 4
    code_with_lint.py:38:57: E251 unexpected spaces around keyword / parameter equals
    code_with_lint.py:38:59: E251 unexpected spaces around keyword / parameter equals
    code_with_lint.py:39:8: E111 indentation is not a multiple of 4
    code_with_lint.py:39:27: E221 multiple spaces before operator
    code_with_lint.py:39:30: E222 multiple spaces after operator
    code_with_lint.py:40:8: E111 indentation is not a multiple of 4
    code_with_lint.py:40:21: E221 multiple spaces before operator
    code_with_lint.py:40:30: E222 multiple spaces after operator
    code_with_lint.py:41:8: F841 local variable 'list_comprehension' is assigned to but never used
    code_with_lint.py:41:8: E111 indentation is not a multiple of 4
    code_with_lint.py:41:43: F405 'pi' may be undefined, or defined from star imports: math
    code_with_lint.py:41:80: E501 line too long (82 > 79 characters)
    code_with_lint.py:42:8: F841 local variable 'time' is assigned to but never used
    code_with_lint.py:42:8: E111 indentation is not a multiple of 4
    code_with_lint.py:42:15: F823 local variable 'time' defined in enclosing scope on line 7 referenced before assignment
    code_with_lint.py:43:8: E111 indentation is not a multiple of 4
    code_with_lint.py:44:8: F841 local variable 'date_and_time' is assigned to but never used
    code_with_lint.py:44:8: E111 indentation is not a multiple of 4
    code_with_lint.py:45:8: E111 indentation is not a multiple of 4
    code_with_lint.py:45:14: W292 no newline at end of file


## When Can I Check My Code Quality?

You can check your code’s quality:

* As you write it
* When it’s checked in
* When you’re running your tests

It’s useful to have linters run against your code frequently. If automation and consistency aren’t there, it’s easy for a large team or project to lose sight of the goal and start creating lower quality code. It happens slowly, of course. Some poorly written logic or maybe some code with formatting that doesn’t match the neighboring code. Over time, all that lint piles up. Eventually, you can get stuck with something that’s buggy, hard to read, hard to fix, and a pain to maintain.

To avoid that, check code quality often!

### As You Write

You can use linters as you write code, but configuring your environment to do so may take some extra work. It’s generally a matter of finding the plugin for your IDE or editor of choice. In fact, most IDEs will already have linters built in.

Here’s some general info on Python linting for various editors:

* Sublime Text
* VS Code
* Atom
* Vim
* Emacs

### Before You Check In Code

If you’re using Git, Git hooks can be set up to run your linters before committing. Other version control systems have similar methods to run scripts before or after some action in the system. You can use these methods to block any new code that doesn’t meet quality standards.

While this may seem drastic, forcing every bit of code through a screening for lint is an important step towards ensuring continued quality. Automating that screening at the front gate to your code may be the best way to avoid lint-filled code.

### When Running Tests

You can also place linters directly into whatever system you may use for continuous integration. The linters can be set up to fail the build if the code doesn’t meet quality standards.

Again, this may seem like a drastic step, especially if there are already lots of linter errors in the existing code. To combat this, some continuous integration systems will allow you the option of only failing the build if the new code increases the number of linter errors that were already present. That way you can start improving quality without doing a whole rewrite of your existing code base.

## Conclusion

High-quality code does what it’s supposed to do without breaking. It is easy to read, maintain, and extend. It functions without problems or defects and is written so that it’s easy for the next person to work with.

Hopefully it goes without saying that you should strive to have such high-quality code. Luckily, there are methods and tools to help improve code quality.

Style guides will bring consistency to your code. PEP8 is a great starting point for Python. Linters will help you identify problem areas and inconsistencies. You can use linters throughout the development process, even automating them to flag lint-filled code before it gets too far.

Having linters complain about style also avoids the need for style discussions during code reviews. Some people may find it easier to receive candid feedback from these tools instead of a team member. Additionally, some team members may not want to “nitpick” style during code reviews. Linters avoid the politics, save time, and complain about any inconsistency.

In addition, all the linters mentioned in this article have various command line options and configurations that let you tailor the tool to your liking. You can be as strict or as loose as you want, which is an important thing to realize.

Improving code quality is a process. You can take steps towards improving it without completely disallowing all nonconformant code. Awareness is a great first step. It just takes a person, like you, to first realize how important high-quality code is.


```python

```
