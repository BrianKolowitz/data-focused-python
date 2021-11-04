---
layout: default
title: 05 - Working with CSV files and JSON data
parent: Topic 05 - Processing files
grand_parent: Lectures
nav_order: 7
---
# Working with CSV files and JSON data
[Source](https://automatetheboringstuff.com/2e/chapter16/)

## The CSV Module


```python
import csv
```


```python
exampleFile = open('../automate_online-materials/example.csv')
```

## reader Objects


```python
exampleReader = csv.reader(exampleFile)
```


```python
exampleData = list(exampleReader)
```


```python
exampleData
```




    [['4/5/2014 13:34', 'Apples', '73'],
     ['4/5/2014 3:41', 'Cherries', '85'],
     ['4/6/2014 12:46', 'Pears', '14'],
     ['4/8/2014 8:59', 'Oranges', '52'],
     ['4/10/2014 2:07', 'Apples', '152'],
     ['4/10/2014 18:10', 'Bananas', '23'],
     ['4/10/2014 2:40', 'Strawberries', '98']]




```python
exampleData[0][0]
```




    '4/5/2014 13:34'




```python
exampleData[0][1]
```




    'Apples'



### Reading data from reader Objects in a for Loop


```python
exampleReader = csv.reader(exampleFile)
```


```python
for row in exampleReader:
    print(f"Row #{exampleReader.line_num} {row}")
```

    Row #1 ['4/5/2014 13:34', 'Apples', '73']
    Row #2 ['4/5/2014 3:41', 'Cherries', '85']
    Row #3 ['4/6/2014 12:46', 'Pears', '14']
    Row #4 ['4/8/2014 8:59', 'Oranges', '52']
    Row #5 ['4/10/2014 2:07', 'Apples', '152']
    Row #6 ['4/10/2014 18:10', 'Bananas', '23']
    Row #7 ['4/10/2014 2:40', 'Strawberries', '98']


## writer Objects


```python
outputFile = open('output.csv', 'w', newline='')
```


```python
outputWriter = csv.writer(outputFile)
```


```python
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
```




    21




```python
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
```




    32




```python
outputFile.close()
```


```python
!cat output.csv
```

    spam,eggs,bacon,ham
    "Hello, world!",eggs,bacon,ham


### The delimiter and lineterminator Keyword Arguments


```python
csvFile = open('example.tsv', 'w', newline='')
```


```python
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
```


```python
csvWriter.writerow(['apples', 'oranges', 'grapes'])
```




    23




```python
csvWriter.writerow(['eggs', 'bacon', 'ham'])
```




    16




```python
outputFile.close()
```


```python
!cat example.tsv
```

    apples	oranges	grapes
    
    eggs	bacon	ham
    


## DictReader and DictWriter CSV Objects



```python
exampleFile = open('../automate_online-materials/exampleWithHeader.csv')
```


```python
exampleDictReader = csv.DictReader(exampleFile)
```


```python
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
```

    4/5/2014 13:34 Apples 73
    4/5/2014 3:41 Cherries 85
    4/6/2014 12:46 Pears 14
    4/8/2014 8:59 Oranges 52
    4/10/2014 2:07 Apples 152
    4/10/2014 18:10 Bananas 23
    4/10/2014 2:40 Strawberries 98


If you tried to use DictReader objects with example.csv, which doesn’t have column headers in the first row, the DictReader object would use '4/5/2015 13:34', 'Apples', and '73' as the dictionary keys. To avoid this, you can supply the DictReader() function with a second argument containing made-up header names:


```python
exampleFile = open('../automate_online-materials/example.csv')
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])

```

    4/5/2014 13:34 Apples 73
    4/5/2014 3:41 Cherries 85
    4/6/2014 12:46 Pears 14
    4/8/2014 8:59 Oranges 52
    4/10/2014 2:07 Apples 152
    4/10/2014 18:10 Bananas 23
    4/10/2014 2:40 Strawberries 98


DictWriter objects use dictionaries to create CSV files.


```python
outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
```


```python
outputDictWriter.writeheader()
```




    16




```python
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
```




    20




```python
outputFile.close()
```


```python
!cat output.csv
```

    Name,Pet,Phone
    Alice,cat,555-1234
    Bob,,555-9999
    Carol,dog,555-5555


## The JSON Module

### Reading JSON with the loads() Function

To translate a string containing JSON data into a Python value, pass it to the json.loads() function. (The name means “load string,” not “loads.”) Enter the following into the interactive shell:


```python
import json
```


```python
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
```


```python
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue
```




    {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}



### Writing JSON with the dumps() Function
The json.dumps() function (which means “dump string,” not “dumps”) will translate a Python value into a string of JSON-formatted data. Enter the following into the interactive shell:


```python
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
```


```python
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData
```




    '{"isCat": true, "miceCaught": 0, "name": "Zophie", "felineIQ": null}'




```python

```
