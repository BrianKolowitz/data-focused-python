---
layout: default
title: 08 - Introducing Linters Into Your Application
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 8
---
# Introducing Linters 
[Source](https://realpython.com/python-testing/)

A linter will look at your code and comment on it. It could give you tips about mistakes you’ve made, correct trailing spaces, and even predict bugs you may have introduced.

## Passive Linting With flake8

A popular linter that comments on the style of your code in relation to the PEP 8 specification is flake8.

You can install flake8 using pip:

```bash
pip install flake8
```

You can then run flake8 over a single file, a folder, or a pattern:


```python
!flake8 lint_example.py
```

    lint_example.py:2:3: E111 indentation is not a multiple of 4
    lint_example.py:4:1: E302 expected 2 blank lines, found 1
    lint_example.py:7:1: W293 blank line contains whitespace
    lint_example.py:10:4: E111 indentation is not a multiple of 4
    lint_example.py:11:4: E111 indentation is not a multiple of 4
    lint_example.py:11:44: W292 no newline at end of file


`flake8` is configurable on the command line or inside a configuration file in your project. If you wanted to ignore certain rules, like `E302` shown above, you can set them in the configuration. flake8 will inspect a `.flake8` file in the project folder or a `setup.cfg` file. If you decided to use `Tox`, you can put the `flake8` configuration section inside `tox.ini`.

This example ignores the `.git` and `__pycache__` directories as well as the `E302` rule. Also, it sets the max line length to ***90*** instead of ***80*** characters. You will likely find that the default constraint of 79 characters for line-width is very limiting for tests, as they contain long method names, string literals with test values, and other pieces of data that can be longer. It is common to set the line length for tests to up to 120 characters:

```ini
[flake8]
ignore = E302
exclude = .git,__pycache__
max-line-length = 90
```

Alternatively, you can provide these options on the command line:


```python
!flake8 --ignore E302 --exclude .git,__pycache__ --max-line-length=90 lint_example.py
```

    lint_example.py:2:3: E111 indentation is not a multiple of 4
    lint_example.py:7:1: W293 blank line contains whitespace
    lint_example.py:10:4: E111 indentation is not a multiple of 4
    lint_example.py:11:4: E111 indentation is not a multiple of 4
    lint_example.py:11:44: W292 no newline at end of file


A full list of configuration options is available on the [Documentation Website](http://flake8.pycqa.org/en/latest/user/options.html).

# Aggressive Linting with a Code Formatter
[Source](https://realpython.com/python-testing/)

`flake8` is a passive linter: it recommends changes, but you have to go and change the code. A more aggressive approach is a code formatter. Code formatters will change your code automatically to meet a collection of style and layout practices.

`black` is a very unforgiving formatter. It doesn’t have any configuration options, and it has a very specific style. This makes it great as a drop-in tool to put in your test pipeline.

You can install black via pip:

```bash
pip install black
```

Then to run black at the command line, provide the file or directory you want to format:

```bash
black test.py
```


```python

```
