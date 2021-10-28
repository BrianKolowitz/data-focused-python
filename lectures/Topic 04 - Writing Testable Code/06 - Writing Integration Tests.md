---
layout: default
title: 06 - Writing Integration Tests
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 6
---
# Writing Integration Tests
[Source](https://realpython.com/python-testing/)

So far, you’ve been learning mainly about unit testing. Unit testing is a great way to build predictable and stable code. But at the end of the day, your application needs to work when it starts!

Integration testing is the testing of multiple components of the application to check that they work together. Integration testing might require acting like a consumer or user of the application by:

* Calling an HTTP REST API
* Calling a Python API
* Calling a web service
* Running a command line

Each of these types of integration tests can be written in the same way as a unit test, following the Input, Execute, and Assert pattern. The most significant difference is that integration tests are checking more components at once and therefore will have more side effects than a unit test. Also, integration tests will require more fixtures to be in place, like a database, a network socket, or a configuration file.

This is why it’s good practice to separate your unit tests and your integration tests. The creation of fixtures required for an integration like a test database and the test cases themselves often take a lot longer to execute than unit tests, so you may only want to run integration tests before you push to production instead of once on every commit.

A simple way to separate unit and integration tests is simply to put them in different folders:

```text
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    ├── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        ├── __init__.py
        └── test_integration.py
```

There are many ways to execute only a select group of tests. The specify source directory flag, -s, can be added to unittest discover with the path containing the tests:


```python
!python -m unittest discover -s project/tests/integration
```

    
    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s
    
    OK


## Testing Data-Driven Applications

Many integration tests will require backend data like a database to exist with certain values. For example, you might want to have a test that checks that the application displays correctly with more than 100 customers in the database, or the order page works even if the product names are displayed in Japanese.

These types of integration tests will depend on different test fixtures to make sure they are repeatable and predictable.

A good technique to use is to store the test data in a folder within your integration testing folder called fixtures to indicate that it contains test data. Then, within your tests, you can load the data and run the test.

Here’s an example of that structure if the data consisted of JSON files:

```text
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    └── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        |
        ├── fixtures/
        |   └── test_basic.json
        |   
        |
        ├── __init__.py
        └── test_integration.py
```

Within your test case, you can use the `.setUp()` method to load the test data from a fixture file in a known path and execute many tests against that test data. Remember you can have multiple test cases in a single Python file, and the `unittest` discovery will execute both. You can have one test case for each set of test data:

```python
# test_integration.py
import unittest

from my_app.app import App


class TestBasic(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = App(database='tests/integration/fixtures/test_basic.json')

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 3)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id=10)
        self.assertEqual(customer['name'], "Org XYZ")
        self.assertEqual(customer['address'], "10 Red Road, Reading")

if __name__ == '__main__':
    unittest.main()
```

You can run the tests from the project folder by typing the following command from the terminal:

```bash
python -m unittest discover -s tests/integration
```


```python

```
