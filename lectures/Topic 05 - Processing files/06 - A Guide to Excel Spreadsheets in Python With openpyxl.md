---
layout: default
title: 06 - A Guide to Excel Spreadsheets in Python With openpyxl
parent: Topic 05 - Processing files
grand_parent: Lectures
nav_order: 8
---
# A Guide to Excel Spreadsheets in Python With openpyxl
[Source](https://realpython.com/openpyxl-excel-spreadsheets-python/)

Excel spreadsheets are one of those things you might have to deal with at some point. Either it’s because your boss loves them or because marketing needs them, you might have to learn how to work with spreadsheets, and that’s when knowing openpyxl comes in handy!

Spreadsheets are a very intuitive and user-friendly way to manipulate large datasets without any prior technical background. That’s why they’re still so commonly used today.

In this article, you’ll learn how to use openpyxl to:

* Manipulate Excel spreadsheets with confidence
* Extract information from spreadsheets
* Create simple or more complex spreadsheets, including adding styles, charts, and so on

## Practical Use Cases

First things first, when would you need to use a package like openpyxl in a real-world scenario? You’ll see a few examples below, but really, there are hundreds of possible scenarios where this knowledge could come in handy.

### Importing New Products Into a Database

You are responsible for tech in an online store company, and your boss doesn’t want to pay for a cool and expensive CMS system.

Every time they want to add new products to the online store, they come to you with an Excel spreadsheet with a few hundred rows and, for each of them, you have the product name, description, price, and so forth.

Now, to import the data, you’ll have to iterate over each spreadsheet row and add each product to the online store.

### Exporting Database Data Into a Spreadsheet

Say you have a Database table where you record all your users’ information, including name, phone number, email address, and so forth.

Now, the Marketing team wants to contact all users to give them some discounted offer or promotion. However, they don’t have access to the Database, or they don’t know how to use SQL to extract that information easily.

What can you do to help? Well, you can make a quick script using openpyxl that iterates over every single User record and puts all the essential information into an Excel spreadsheet.

That’s gonna earn you an extra slice of cake at your company’s next birthday party!

### Appending Information to an Existing Spreadsheet

You may also have to open a spreadsheet, read the information in it and, according to some business logic, append more data to it.

For example, using the online store scenario again, say you get an Excel spreadsheet with a list of users and you need to append to each row the total amount they’ve spent in your store.

This data is in the Database and, in order to do this, you have to read the spreadsheet, iterate through each row, fetch the total amount spent from the Database and then write back to the spreadsheet.

Not a problem for openpyxl!

## Learning Some Basic Excel Terminology
Here’s a quick list of basic terms you’ll see when you’re working with Excel spreadsheets:

| Term | Explanation |
| --- | --- |
| Spreadsheet or Workbook | A Spreadsheet is the main file you are creating or working with. |
| Worksheet or Sheet | A Sheet is used to split different kinds of content within the same spreadsheet. A Spreadsheet can have one or more Sheets. |
| Column | A Column is a vertical line, and it’s represented by an uppercase letter: A. |
| Row | A Row is a horizontal line, and it’s represented by a number: 1. |
| Cell | A Cell is a combination of Column and Row, represented by both an uppercase letter and a number: A1. |

## Getting Started With openpyxl

Now that you’re aware of the benefits of a tool like openpyxl, let’s get down to it and start by installing the package. For this tutorial, you should use Python 3.7 and openpyxl 2.6.2. To install the package, you can do the following:

```python
pip install openpyxl
```

After you install the package, you should be able to create a super simple spreadsheet with the following code:


```python
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename="hello_world.xlsx")
```

## A Simple Approach to Reading an Excel Spreadsheet

Finally, let’s start reading some spreadsheets! To begin with, open our sample spreadsheet:


```python
from openpyxl import load_workbook
workbook = load_workbook(filename="sample.xlsx")
workbook.sheetnames
```




    ['Sheet1']




```python
sheet = workbook.active
sheet
```




    <Worksheet "Sheet1">




```python
sheet.title
```




    'Sheet1'



In the code above, you first open the spreadsheet sample.xlsx using load_workbook(), and then you can use workbook.sheetnames to see all the sheets you have available to work with. After that, workbook.active selects the first available sheet and, in this case, you can see that it selects Sheet 1 automatically. Using these methods is the default way of opening a spreadsheet, and you’ll see it many times during this tutorial.

Now, after opening a spreadsheet, you can easily retrieve data from it like this:


```python
sheet["A1"]
```




    <Cell 'Sheet1'.A1>




```python
sheet["A1"].value
```




    'marketplace'




```python
sheet["F10"].value
```




    "G-Shock Men's Grey Sport Watch"



To return the actual value of a cell, you need to do .value. Otherwise, you’ll get the main Cell object. You can also use the method .cell() to retrieve a cell using index notation. Remember to add .value to get the actual value and not a Cell object:


```python
sheet.cell(row=10, column=6)
```




    <Cell 'Sheet1'.F10>




```python
sheet.cell(row=10, column=6).value
```




    "G-Shock Men's Grey Sport Watch"



You can see that the results returned are the same, no matter which way you decide to go with. However, in this tutorial, you’ll be mostly using the first approach: ["A1"].

> Note: Even though in Python you’re used to a zero-indexed notation, with spreadsheets you’ll always use a one-indexed notation where the first row or column always has index 1.

The above shows you the quickest way to open a spreadsheet. However, you can pass additional parameters to change the way a spreadsheet is loaded.**

### Additional Reading Options

There are a few arguments you can pass to load_workbook() that change the way a spreadsheet is loaded. The most important ones are the following two Booleans:

1. `read_only` loads a spreadsheet in read-only mode allowing you to open very large Excel files.
2. `data_only` ignores loading formulas and instead loads only the resulting values.

## Importing Data From a Spreadsheet

Now that you’ve learned the basics about loading a spreadsheet, it’s about time you get to the fun part: the iteration and actual usage of the values within the spreadsheet.

This section is where you’ll learn all the different ways you can iterate through the data, but also how to convert that data into something usable and, more importantly, how to do it in a Pythonic way.

### Iterating Through the Data

There are a few different ways you can iterate through the data depending on your needs.

You can slice the data with a combination of columns and rows:


```python
sheet["A1:C2"]
```




    ((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>),
     (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>))




```python
# Get all cells from column A
cells = sheet["A"]
print(cells[:10])
```

    (<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.A2>, <Cell 'Sheet1'.A3>, <Cell 'Sheet1'.A4>, <Cell 'Sheet1'.A5>, <Cell 'Sheet1'.A6>, <Cell 'Sheet1'.A7>, <Cell 'Sheet1'.A8>, <Cell 'Sheet1'.A9>, <Cell 'Sheet1'.A10>)



```python
# Get all cells for a range of columns
cells = sheet["A:B"]
```


```python
# Get all cells from row 5
sheet[5]
```




    (<Cell 'Sheet1'.A5>,
     <Cell 'Sheet1'.B5>,
     <Cell 'Sheet1'.C5>,
     <Cell 'Sheet1'.D5>,
     <Cell 'Sheet1'.E5>,
     <Cell 'Sheet1'.F5>,
     <Cell 'Sheet1'.G5>,
     <Cell 'Sheet1'.H5>,
     <Cell 'Sheet1'.I5>,
     <Cell 'Sheet1'.J5>,
     <Cell 'Sheet1'.K5>,
     <Cell 'Sheet1'.L5>,
     <Cell 'Sheet1'.M5>,
     <Cell 'Sheet1'.N5>,
     <Cell 'Sheet1'.O5>)




```python
# Get all cells for a range of rows
sheet[5:6]
```




    ((<Cell 'Sheet1'.A5>,
      <Cell 'Sheet1'.B5>,
      <Cell 'Sheet1'.C5>,
      <Cell 'Sheet1'.D5>,
      <Cell 'Sheet1'.E5>,
      <Cell 'Sheet1'.F5>,
      <Cell 'Sheet1'.G5>,
      <Cell 'Sheet1'.H5>,
      <Cell 'Sheet1'.I5>,
      <Cell 'Sheet1'.J5>,
      <Cell 'Sheet1'.K5>,
      <Cell 'Sheet1'.L5>,
      <Cell 'Sheet1'.M5>,
      <Cell 'Sheet1'.N5>,
      <Cell 'Sheet1'.O5>),
     (<Cell 'Sheet1'.A6>,
      <Cell 'Sheet1'.B6>,
      <Cell 'Sheet1'.C6>,
      <Cell 'Sheet1'.D6>,
      <Cell 'Sheet1'.E6>,
      <Cell 'Sheet1'.F6>,
      <Cell 'Sheet1'.G6>,
      <Cell 'Sheet1'.H6>,
      <Cell 'Sheet1'.I6>,
      <Cell 'Sheet1'.J6>,
      <Cell 'Sheet1'.K6>,
      <Cell 'Sheet1'.L6>,
      <Cell 'Sheet1'.M6>,
      <Cell 'Sheet1'.N6>,
      <Cell 'Sheet1'.O6>))



You’ll notice that all of the above examples return a tuple. If you want to refresh your memory on how to handle tuples in Python, check out the article on Lists and Tuples in Python.

There are also multiple ways of using normal Python generators to go through the data. The main methods you can use to achieve this are:

* `.iter_rows()`
* `.iter_cols()`

Both methods can receive the following arguments:

* `min_row`
* `max_row`
* `min_col`
* `max_col`

These arguments are used to set boundaries for the iteration:


```python
for row in sheet.iter_rows(min_row=1,
                           max_row=2,
                           min_col=1,
                           max_col=3):
    print(row)
```

    (<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>)
    (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>)



```python
for column in sheet.iter_cols(min_row=1,
                              max_row=2,
                              min_col=1,
                              max_col=3):
    print(column)
```

    (<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.A2>)
    (<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>)
    (<Cell 'Sheet1'.C1>, <Cell 'Sheet1'.C2>)


You’ll notice that in the first example, when iterating through the rows using .iter_rows(), you get one tuple element per row selected. While when using .iter_cols() and iterating through columns, you’ll get one tuple per column instead.

One additional argument you can pass to both methods is the Boolean values_only. When it’s set to True, the values of the cell are returned, instead of the Cell object:


```python
for value in sheet.iter_rows(min_row=1,
                             max_row=2,
                             min_col=1,
                             max_col=3,
                             values_only=True):
    print(value)
```

    ('marketplace', 'customer_id', 'review_id')
    ('US', 3653882, 'R3O9SGZBVQBV76')


If you want to iterate through the whole dataset, then you can also use the attributes .rows or .columns directly, which are shortcuts to using .iter_rows() and .iter_cols() without any arguments:


```python
for row in sheet.rows:
    print(row)
    break
```

    (<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>, <Cell 'Sheet1'.D1>, <Cell 'Sheet1'.E1>, <Cell 'Sheet1'.F1>, <Cell 'Sheet1'.G1>, <Cell 'Sheet1'.H1>, <Cell 'Sheet1'.I1>, <Cell 'Sheet1'.J1>, <Cell 'Sheet1'.K1>, <Cell 'Sheet1'.L1>, <Cell 'Sheet1'.M1>, <Cell 'Sheet1'.N1>, <Cell 'Sheet1'.O1>)


## Manipulate Data Using Python’s Default Data Structures

Now that you know the basics of iterating through the data in a workbook, let’s look at smart ways of converting that data into Python structures.

As you saw earlier, the result from all iterations comes in the form of tuples. However, since a tuple is nothing more than an immutable list, you can easily access its data and transform it into other structures.

For example, say you want to extract product information from the sample.xlsx spreadsheet and into a dictionary where each key is a product ID.

A straightforward way to do this is to iterate over all the rows, pick the columns you know are related to product information, and then store that in a dictionary. Let’s code this out!

First of all, have a look at the headers and see what information you care most about:


```python
for value in sheet.iter_rows(min_row=1,
                             max_row=1,
                             values_only=True):
    print(value)
```

    ('marketplace', 'customer_id', 'review_id', 'product_id', 'product_parent', 'product_title', 'product_category', 'star_rating', 'helpful_votes', 'total_votes', 'vine', 'verified_purchase', 'review_headline', 'review_body', 'review_date')


This code returns a list of all the column names you have in the spreadsheet. To start, grab the columns with names:

* product_id
* product_parent
* product_title
* product_category

If the columns are next to each other so you can use the min_column and max_column to easily get the data you want:


```python
for value in sheet.iter_rows(min_row=2,
                             max_row=10,
                             min_col=4,
                             max_col=7,
                             values_only=True):
    print(value)
```

    ('B00FALQ1ZC', 937001370, 'Invicta Women\'s 15150 "Angel" 18k Yellow Gold Ion-Plated Stainless Steel and Brown Leather Watch', 'Watches')
    ('B00D3RGO20', 484010722, "Kenneth Cole New York Women's KC4944 Automatic Silver Automatic Mesh Bracelet Analog Watch", 'Watches')
    ('B00DKYC7TK', 361166390, 'Ritche 22mm Black Stainless Steel Bracelet Watch Band Strap Pebble Time/Pebble Classic', 'Watches')
    ('B000EQS1JW', 958035625, "Citizen Men's BM8180-03E Eco-Drive Stainless Steel Watch with Green Canvas Band", 'Watches')
    ('B00A6GFD7S', 765328221, "Orient ER27009B Men's Symphony Automatic Stainless Steel Black Dial Mechanical Watch", 'Watches')
    ('B00EYSOSE8', 230493695, "Casio Men's GW-9400BJ-1JF G-Shock Master of G Rangeman Digital Solar Black Carbon Fiber Insert Watch", 'Watches')
    ('B00WM0QA3M', 549298279, "Fossil Women's ES3851 Urban Traveler Multifunction Stainless Steel Watch - Rose", 'Watches')
    ('B00A4EYBR0', 844009113, 'INFANTRY Mens Night Vision Analog Quartz Wrist Watch with Nato Nylon Watchband-Red.', 'Watches')
    ('B00MAMPGGE', 263720892, "G-Shock Men's Grey Sport Watch", 'Watches')



```python
import json
from openpyxl import load_workbook

workbook = load_workbook(filename="sample.xlsx")
sheet = workbook.active

products = {}

# Using the values_only because you want to return the cells' values
for row in sheet.iter_rows(min_row=2,
                           min_col=4,
                           max_col=7,
                           values_only=True):
    product_id = row[0]
    product = {
        "parent": row[1],
        "title": row[2],
        "category": row[3]
    }
    products[product_id] = product
```


```python
print(json.dumps(products[list(products.keys())[0]]))
```

    {"parent": 937001370, "title": "Invicta Women's 15150 \"Angel\" 18k Yellow Gold Ion-Plated Stainless Steel and Brown Leather Watch", "category": "Watches"}


## Convert Data Into Python Classes

To finalize the reading section of this tutorial, let’s dive into Python classes and see how you could improve on the example above and better structure the data.

For this, you’ll be using the new Python [Data Classes](https://realpython.com/python-data-classes/) that are available from Python 3.7. If you’re using an older version of Python, then you can use the default [Classes](https://realpython.com/python3-object-oriented-programming/#classes-in-python) instead.

So, first things first, let’s look at the data you have and decide what you want to store and how you want to store it.

As you saw right at the start, this data comes from Amazon, and it’s a list of product reviews. You can check the [list of all the columns and their meaning](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt) on Amazon.

There are two significant elements you can extract from the data available:

1. Products
2. Reviews

A **Product** has:

* ID
* Title
* Parent
* Category

The **Review** has a few more fields:

* ID
* Customer ID
* Stars
* Headline
* Body
*  Date

You can ignore a few of the review fields to make things a bit simpler.

So, a straightforward implementation of these two classes could be written in a separate file classes.py:


```python
import datetime
from dataclasses import dataclass

@dataclass
class Product:
    id: str
    parent: str
    title: str
    category: str

@dataclass
class Review:
    id: str
    customer_id: str
    stars: int
    headline: str
    body: str
    date: datetime.datetime
```

After defining your data classes, you need to convert the data from the spreadsheet into these new structures.

Before doing the conversion, it’s worth looking at our header again and creating a mapping between columns and the fields you need:


```python
for value in sheet.iter_rows(min_row=1,
                             max_row=1,
                             values_only=True):
    print(value)
```

    ('marketplace', 'customer_id', 'review_id', 'product_id', 'product_parent', 'product_title', 'product_category', 'star_rating', 'helpful_votes', 'total_votes', 'vine', 'verified_purchase', 'review_headline', 'review_body', 'review_date')



```python
for cell in sheet[1]:
    print(cell.value)
```

    marketplace
    customer_id
    review_id
    product_id
    product_parent
    product_title
    product_category
    star_rating
    helpful_votes
    total_votes
    vine
    verified_purchase
    review_headline
    review_body
    review_date


Let’s create a file mapping.py where you have a list of all the field names and their column location (zero-indexed) on the spreadsheet:


```python
# Product fields
PRODUCT_ID = 3
PRODUCT_PARENT = 4
PRODUCT_TITLE = 5
PRODUCT_CATEGORY = 6

# Review fields
REVIEW_ID = 2
REVIEW_CUSTOMER = 1
REVIEW_STARS = 7
REVIEW_HEADLINE = 12
REVIEW_BODY = 13
REVIEW_DATE = 14
```

You don’t necessarily have to do the mapping above. It’s more for readability when parsing the row data, so you don’t end up with a lot of magic numbers lying around.

Finally, let’s look at the code needed to parse the spreadsheet data into a list of product and review objects:


```python
from datetime import datetime
from openpyxl import load_workbook
from classes import Product, Review
from mapping import PRODUCT_ID, PRODUCT_PARENT, PRODUCT_TITLE, \
    PRODUCT_CATEGORY, REVIEW_DATE, REVIEW_ID, REVIEW_CUSTOMER, \
    REVIEW_STARS, REVIEW_HEADLINE, REVIEW_BODY

# Using the read_only method since you're not gonna be editing the spreadsheet
workbook = load_workbook(filename="sample.xlsx", read_only=True)
sheet = workbook.active

products = []
reviews = []

# Using the values_only because you just want to return the cell value
for row in sheet.iter_rows(min_row=2, values_only=True):
    product = Product(id=row[PRODUCT_ID],
                      parent=row[PRODUCT_PARENT],
                      title=row[PRODUCT_TITLE],
                      category=row[PRODUCT_CATEGORY])
    products.append(product)

    # You need to parse the date from the spreadsheet into a datetime format
    spread_date = row[REVIEW_DATE]
    parsed_date = datetime.strptime(spread_date, "%Y-%m-%d")

    review = Review(id=row[REVIEW_ID],
                    customer_id=row[REVIEW_CUSTOMER],
                    stars=row[REVIEW_STARS],
                    headline=row[REVIEW_HEADLINE],
                    body=row[REVIEW_BODY],
                    date=parsed_date)
    reviews.append(review)

print(products[0])
print(reviews[0])
```

    Product(id='B00FALQ1ZC', parent=937001370, title='Invicta Women\'s 15150 "Angel" 18k Yellow Gold Ion-Plated Stainless Steel and Brown Leather Watch', category='Watches')
    Review(id='R3O9SGZBVQBV76', customer_id=3653882, stars=5, headline='Five Stars', body='Absolutely love this watch! Get compliments almost every time I wear it. Dainty.', date=datetime.datetime(2015, 8, 31, 0, 0))


That’s it! Now you should have the data in a very simple and digestible class format, and you can start thinking of storing this in a Database or any other type of data storage you like.

Using this kind of OOP strategy to parse spreadsheets makes handling the data much simpler later on.

## Appending New Data

Before you start creating very complex spreadsheets, have a quick look at an example of how to append data to an existing spreadsheet.

Go back to the first example spreadsheet you created (hello_world.xlsx) and try opening it and appending some data to it, like this:


```python
from openpyxl import load_workbook

# Start by opening the spreadsheet and selecting the main sheet
workbook = load_workbook(filename="hello_world.xlsx")
sheet = workbook.active

# Write what you want into a specific cell
sheet["C1"] = "writing ;)"

# Save the spreadsheet
workbook.save(filename="hello_world_append.xlsx")
```

## Writing Excel Spreadsheets With openpyxl

There are a lot of different things you can write to a spreadsheet, from simple text or number values to complex formulas, charts, or even images.

Let’s start creating some spreadsheets!

### Creating a Simple Spreadsheet

Previously, you saw a very quick example of how to write “Hello world!” into a spreadsheet, so you can start with that:


```python
from openpyxl import Workbook

filename = "hello_world.xlsx"

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename=filename)
```

The highlighted lines in the code above are the most important ones for writing. In the code, you can see that:

* Line 5 shows you how to create a new empty workbook.
* Lines 8 and 9 show you how to add data to specific cells.
* Line 11 shows you how to save the spreadsheet when you’re done.

Even though these lines above can be straightforward, it’s still good to know them well for when things get a bit more complicated.

> Note: You’ll be using the hello_world.xlsx spreadsheet for some of the upcoming examples, so keep it handy.

## Conclusion

There's so much more the openpyxl library can do. To learn more visit the developer [documentation](https://openpyxl.readthedocs.io/en/stable/) or continue the learning [here](https://realpython.com/openpyxl-excel-spreadsheets-python/#reading-excel-spreadsheets-with-openpyxl)


```python

```
