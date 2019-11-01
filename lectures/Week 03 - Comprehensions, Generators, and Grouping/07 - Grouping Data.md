---
layout: default
title: 07 - Grouping Data
parent: Week 03 - Comprehensions, Generators, and Grouping
grand_parent: Lectures
nav_order: 10
---

# Grouping data using python

In this tutorial we're going to learn how to use basic python funtionality to group datasets.


```python
import csv
from pprint import pprint
```


```python
# recall, opening the file and reading the data
with open('../data/csv/patients.csv') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        pprint(row)
        if i >= 1:
            break
```

    OrderedDict([('Id', 'a1f26fb1-05aa-4991-8cf3-78d5dbc7853a'),
                 ('BIRTHDATE', '1994-08-22'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-81-6585'),
                 ('DRIVERS', 'S99916284'),
                 ('PASSPORT', 'X62883440X'),
                 ('PREFIX', 'Mr.'),
                 ('FIRST', 'Gregory545'),
                 ('LAST', 'Zulauf375'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'italian'),
                 ('GENDER', 'M'),
                 ('BIRTHPLACE', 'Worcester  Massachusetts  US'),
                 ('ADDRESS', '448 Bahringer Junction Apt 97'),
                 ('CITY', 'North Reading'),
                 ('STATE', 'Massachusetts'),
                 ('ZIP', '01864')])
    OrderedDict([('Id', '112942a0-dca9-4a07-983f-9e9cabcc6fe0'),
                 ('BIRTHDATE', '1993-10-28'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-93-5205'),
                 ('DRIVERS', 'S99938900'),
                 ('PASSPORT', 'X13004759X'),
                 ('PREFIX', 'Ms.'),
                 ('FIRST', 'Tena12'),
                 ('LAST', 'Ryan260'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'irish'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Revere  Massachusetts  US'),
                 ('ADDRESS', '880 Bartell Trafficway'),
                 ('CITY', 'Tyngsborough'),
                 ('STATE', 'Massachusetts'),
                 ('ZIP', '')])



```python
# then we're going to parse out a group, e.g. Gender
# recall, opening the file and reading the data
with open('../data/csv/patients.csv') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        patient_gender = row['GENDER']
        print(patient_gender)
        if i >= 2:
            break
```

    M
    F
    M



```python
# how do we know what the unique genders are?
# let's iterate over them and create a set
patient_genders = set()

with open('../data/csv/patients.csv') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        patient_gender = row['GENDER']
        patient_genders.add(patient_gender)
print(patient_genders)
```

    {'F', 'M'}



```python
# okay, we have 2 genders let's create 2 lists
male_patients = []
female_patients = []

with open('../data/csv/patients.csv') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        patient_gender = row['GENDER']
        if patient_gender == 'M':
            male_patients.append(row)
        elif patient_gender == 'F':
            female_patients.append(row)
        else:
            raise Exception('Unknown Gender')

pprint(male_patients[0])
pprint(female_patients[0])
```

    OrderedDict([('Id', 'a1f26fb1-05aa-4991-8cf3-78d5dbc7853a'),
                 ('BIRTHDATE', '1994-08-22'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-81-6585'),
                 ('DRIVERS', 'S99916284'),
                 ('PASSPORT', 'X62883440X'),
                 ('PREFIX', 'Mr.'),
                 ('FIRST', 'Gregory545'),
                 ('LAST', 'Zulauf375'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'italian'),
                 ('GENDER', 'M'),
                 ('BIRTHPLACE', 'Worcester  Massachusetts  US'),
                 ('ADDRESS', '448 Bahringer Junction Apt 97'),
                 ('CITY', 'North Reading'),
                 ('STATE', 'Massachusetts'),
                 ('ZIP', '01864')])
    OrderedDict([('Id', '112942a0-dca9-4a07-983f-9e9cabcc6fe0'),
                 ('BIRTHDATE', '1993-10-28'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-93-5205'),
                 ('DRIVERS', 'S99938900'),
                 ('PASSPORT', 'X13004759X'),
                 ('PREFIX', 'Ms.'),
                 ('FIRST', 'Tena12'),
                 ('LAST', 'Ryan260'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'irish'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Revere  Massachusetts  US'),
                 ('ADDRESS', '880 Bartell Trafficway'),
                 ('CITY', 'Tyngsborough'),
                 ('STATE', 'Massachusetts'),
                 ('ZIP', '')])


## Can we do better?

What's wrong with the code above?

1. Multiple iterations over the file
2. Brittle... not resilient to new genders

What can we do?

1. Use a dictionary to store the groupings
2. Make the code case insensitive


```python
# patients by gender
patients_by_gender = {}

patients_by_gender['F'] = ['patient1', 'patient3']
patients_by_gender['M'] = ['patient2', 'patient4']

pprint(patients_by_gender)
```

    {'F': ['patient1', 'patient3'], 'M': ['patient2', 'patient4']}



```python
print(patients_by_gender.keys())
```

    dict_keys(['F', 'M'])



```python
print(patients_by_gender.values())
```

    dict_values([['patient1', 'patient3'], ['patient2', 'patient4']])



```python
print(patients_by_gender.items())
```

    dict_items([('F', ['patient1', 'patient3']), ('M', ['patient2', 'patient4'])])



```python
# check if a gender is in the dictionary
print('F' in patients_by_gender)
```

    True



```python
print('f' in patients_by_gender)
```

    False



```python
# let's group using a dictionary
patients_by_gender = {}

with open('../data/csv/patients.csv') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        patient_gender = row['GENDER'].upper() # let's store the keys as uppercase
        
        # check to see if the key exists, if not
        if patient_gender not in patients_by_gender:
            # add the key
            patients_by_gender[patient_gender] = [] # create an empty list

        # append the patient as a new row to the correct grouping
        patients_by_gender[patient_gender].append(row)

print(patients_by_gender.keys())
```

    dict_keys(['M', 'F'])



```python
pprint(patients_by_gender['F'][0:2])
```

    [OrderedDict([('Id', '112942a0-dca9-4a07-983f-9e9cabcc6fe0'),
                  ('BIRTHDATE', '1993-10-28'),
                  ('DEATHDATE', ''),
                  ('SSN', '999-93-5205'),
                  ('DRIVERS', 'S99938900'),
                  ('PASSPORT', 'X13004759X'),
                  ('PREFIX', 'Ms.'),
                  ('FIRST', 'Tena12'),
                  ('LAST', 'Ryan260'),
                  ('SUFFIX', ''),
                  ('MAIDEN', ''),
                  ('MARITAL', ''),
                  ('RACE', 'white'),
                  ('ETHNICITY', 'irish'),
                  ('GENDER', 'F'),
                  ('BIRTHPLACE', 'Revere  Massachusetts  US'),
                  ('ADDRESS', '880 Bartell Trafficway'),
                  ('CITY', 'Tyngsborough'),
                  ('STATE', 'Massachusetts'),
                  ('ZIP', '')]),
     OrderedDict([('Id', '893ba78c-4633-4707-a11a-bf7f6c6fc827'),
                  ('BIRTHDATE', '2003-08-16'),
                  ('DEATHDATE', ''),
                  ('SSN', '999-46-3420'),
                  ('DRIVERS', 'S99923748'),
                  ('PASSPORT', ''),
                  ('PREFIX', ''),
                  ('FIRST', 'Casandra937'),
                  ('LAST', 'Reynolds644'),
                  ('SUFFIX', ''),
                  ('MAIDEN', ''),
                  ('MARITAL', ''),
                  ('RACE', 'white'),
                  ('ETHNICITY', 'russian'),
                  ('GENDER', 'F'),
                  ('BIRTHPLACE', 'Boston  Massachusetts  US'),
                  ('ADDRESS', '1048 Botsford Skyway Apt 45'),
                  ('CITY', 'Fairhaven'),
                  ('STATE', 'Massachusetts'),
                  ('ZIP', '02719')])]



```python
print(patients_by_gender['F'][0]['LAST'])
```

    Ryan260


## Let's make the code reusable

1. Create a function
2. Externalize parameters that will change fromt the function

What's common?
1. The csv processing
2. The grouping logic

What's different?
1. The file name
2. The groupby parameters


```python
# define the function
def group_patient(file_name, groupby):
    pass
```


```python
# call the function
patients_by_gender = group_patient('../data/csv/patients.csv', 'GENDER')
print(patients_by_gender)
```

    None



```python
# now let's implement the function
def group_patient(file_name, groupby):
    patients_by_group = {}
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # note : we renamed the variable to _attribute
            patient_attribute = row[groupby].upper()

            # check to see if the key exists, if not
            if patient_attribute not in patients_by_group:
                # add the key
                patients_by_group[patient_attribute] = [] # create an empty list

            # append the patient as a new row to the correct grouping
            patients_by_group[patient_attribute].append(row)
    return patients_by_group
```


```python
patients_by_gender = group_patient('../data/csv/patients.csv', 'GENDER')
pprint(patients_by_gender['F'][0:2])
```

    [OrderedDict([('Id', '112942a0-dca9-4a07-983f-9e9cabcc6fe0'),
                  ('BIRTHDATE', '1993-10-28'),
                  ('DEATHDATE', ''),
                  ('SSN', '999-93-5205'),
                  ('DRIVERS', 'S99938900'),
                  ('PASSPORT', 'X13004759X'),
                  ('PREFIX', 'Ms.'),
                  ('FIRST', 'Tena12'),
                  ('LAST', 'Ryan260'),
                  ('SUFFIX', ''),
                  ('MAIDEN', ''),
                  ('MARITAL', ''),
                  ('RACE', 'white'),
                  ('ETHNICITY', 'irish'),
                  ('GENDER', 'F'),
                  ('BIRTHPLACE', 'Revere  Massachusetts  US'),
                  ('ADDRESS', '880 Bartell Trafficway'),
                  ('CITY', 'Tyngsborough'),
                  ('STATE', 'Massachusetts'),
                  ('ZIP', '')]),
     OrderedDict([('Id', '893ba78c-4633-4707-a11a-bf7f6c6fc827'),
                  ('BIRTHDATE', '2003-08-16'),
                  ('DEATHDATE', ''),
                  ('SSN', '999-46-3420'),
                  ('DRIVERS', 'S99923748'),
                  ('PASSPORT', ''),
                  ('PREFIX', ''),
                  ('FIRST', 'Casandra937'),
                  ('LAST', 'Reynolds644'),
                  ('SUFFIX', ''),
                  ('MAIDEN', ''),
                  ('MARITAL', ''),
                  ('RACE', 'white'),
                  ('ETHNICITY', 'russian'),
                  ('GENDER', 'F'),
                  ('BIRTHPLACE', 'Boston  Massachusetts  US'),
                  ('ADDRESS', '1048 Botsford Skyway Apt 45'),
                  ('CITY', 'Fairhaven'),
                  ('STATE', 'Massachusetts'),
                  ('ZIP', '02719')])]



```python
# but wait... is there anything patient specific???
# let's refactor the code to make it more extensible 
# and easier to read
def group(file_name, groupby):
    grouped_data = {}
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
            attribute = row[groupby].upper()
            if attribute not in grouped_data:
                grouped_data[attribute] = []
            grouped_data[attribute].append(row)
    return grouped_data
```


```python
patients_by_gender = group('../data/csv/patients.csv', 'GENDER')
pprint(patients_by_gender['F'][0])
```

    OrderedDict([('Id', '112942a0-dca9-4a07-983f-9e9cabcc6fe0'),
                 ('BIRTHDATE', '1993-10-28'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-93-5205'),
                 ('DRIVERS', 'S99938900'),
                 ('PASSPORT', 'X13004759X'),
                 ('PREFIX', 'Ms.'),
                 ('FIRST', 'Tena12'),
                 ('LAST', 'Ryan260'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'irish'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Revere  Massachusetts  US'),
                 ('ADDRESS', '880 Bartell Trafficway'),
                 ('CITY', 'Tyngsborough'),
                 ('STATE', 'Massachusetts'),
                 ('ZIP', '')])


## What if we want multiple grouping levels?


```python
# single level grouping by gender
{
    "F": [ 'patient1', 'patient2'],
    "M": [ 'patient3', 'patient4']
}
```




    {'F': ['patient1', 'patient2'], 'M': ['patient3', 'patient4']}




```python
# multi level grouping by gender and race
{
    "F": {
        "WHITE": ['patient1', 'patient2'],
        "HISPANIC": ['patient3'] 
    },
    "M": {
        "WHITE": [],
        "HISPANIC": ['patient4', 'patient5']
    }
}
```




    {'F': {'WHITE': ['patient1', 'patient2'], 'HISPANIC': ['patient3']},
     'M': {'WHITE': [], 'HISPANIC': ['patient4', 'patient5']}}




```python
def group_file(file_name, groupby):
    with open(file_name) as f:
        reader = csv.DictReader(f)
        return group(reader, groupby)
    
def group(iterable, groupby):
    grouped_data = {}
    for item in iterable:
        attribute = item[groupby].upper()
        if attribute not in grouped_data:
            grouped_data[attribute] = []
        grouped_data[attribute].append(item)
    return grouped_data
```


```python
patients_by_gender = group_file('../data/csv/patients.csv', 'GENDER')
pprint(patients_by_gender['F'][0])
```

    OrderedDict([('Id', '112942a0-dca9-4a07-983f-9e9cabcc6fe0'),
                 ('BIRTHDATE', '1993-10-28'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-93-5205'),
                 ('DRIVERS', 'S99938900'),
                 ('PASSPORT', 'X13004759X'),
                 ('PREFIX', 'Ms.'),
                 ('FIRST', 'Tena12'),
                 ('LAST', 'Ryan260'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'irish'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Revere  Massachusetts  US'),
                 ('ADDRESS', '880 Bartell Trafficway'),
                 ('CITY', 'Tyngsborough'),
                 ('STATE', 'Massachusetts'),
                 ('ZIP', '')])



```python
# patients by gender and race
# here we'll use a dictionary to represent the 2nd level
patients_by_gender_and_race = group_file('../data/csv/patients.csv', 'GENDER')
for gender in patients_by_gender_and_race.keys():
    patients_by_gender_and_race[gender] = {}
pprint(patients_by_gender_and_race)
```

    {'F': {}, 'M': {}}



```python
# now let's perform the groupings
patients_by_gender_and_race = group_file('../data/csv/patients.csv', 'GENDER')
# print(patients_by_gender_and_race)
for gender in patients_by_gender.keys():
    patients_by_gender_and_race[gender] = group(patients_by_gender[gender], 'RACE')
```


```python
# finally let's print the unique genders and races
for gender in patients_by_gender_and_race.keys():
    for race in patients_by_gender_and_race[gender].keys():
        print(gender, race)
```

    M WHITE
    F WHITE
    F NATIVE



```python
# as a sanity check let's look over the dataset again
gender = set()
race = set()

with open('../data/csv/patients.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        gender.add(row['GENDER'])
        race.add(row['RACE'])    
print(gender, race)
```

    {'F', 'M'} {'white', 'native'}



```python
# what about 3 levels of grouping?
grouped_patients = group_file('../data/csv/patients.csv', 'GENDER')
for gender in grouped_patients.keys():
    grouped_patients[gender] = group(grouped_patients[gender], 'RACE')
    for race in grouped_patients[gender].keys():
        grouped_patients[gender][race] = group(grouped_patients[gender][race], 'ETHNICITY')
        
# print(grouped_patients)
```


```python
# let's print the unique genders and races
for gender in grouped_patients.keys():
    for race in grouped_patients[gender].keys():
        for ethnicity in grouped_patients[gender][race].keys():
            print(gender, race, ethnicity)
```

    M WHITE ITALIAN
    M WHITE ENGLISH
    M WHITE GERMAN
    F WHITE IRISH
    F WHITE RUSSIAN
    F WHITE AMERICAN
    F NATIVE AMERICAN_INDIAN


## What about 4 levels of grouping?

I think we should refactor again. This time using [recursion](https://realpython.com/python-thinking-recursively/). This time we'll support any number of groupings.


```python
def group_file_by_list(file_name, groupings):
    with open(file_name) as f:
        reader = csv.DictReader(f)
        grouped_data = group(reader, groupings[0])
        if len(groupings) > 1:
            group_by_list(grouped_data.keys(), grouped_data, groupings[1:])
        return grouped_data
    
def group_by_list(iterable, grouped_data, groupings):
    for item in iterable:
        grouped_data[item] = group(grouped_data[item], groupings[0])
        if len(groupings) > 1:
            group_by_list(grouped_data[item].keys(), grouped_data[item], groupings[1:])
    return grouped_data
```


```python
groupings = ['GENDER', 'RACE', 'ETHNICITY']
grouped_patients = group_file_by_list('../data/csv/patients.csv', groupings)
```


```python
for gender in grouped_patients.keys():
    for race in grouped_patients[gender].keys():
        for ethnicity in grouped_patients[gender][race].keys():
            print(gender, race, ethnicity)
```

    M WHITE ITALIAN
    M WHITE ENGLISH
    M WHITE GERMAN
    F WHITE IRISH
    F WHITE RUSSIAN
    F WHITE AMERICAN
    F NATIVE AMERICAN_INDIAN



```python
# let's create a recursive print
def print_keys(d):
    for k, v in d.items():
        print_keys2(v, [k])

def print_keys2(d, l):
    if isinstance(d, dict):
        for k, v in d.items():
            print_keys2(v, l + [k])
    else:
        print(' '.join(l))
        l = []
    
print_keys(grouped_patients)
```

    M WHITE ITALIAN
    M WHITE ENGLISH
    M WHITE GERMAN
    F WHITE IRISH
    F WHITE RUSSIAN
    F WHITE AMERICAN
    F NATIVE AMERICAN_INDIAN



```python
# lets try it out on a few examples
```


```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['GENDER'])
print_keys(grouped_patients)
```

    M
    F



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['RACE'])
print_keys(grouped_patients)
```

    WHITE
    NATIVE



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['GENDER', 'RACE'])
print_keys(grouped_patients)
```

    M WHITE
    F WHITE
    F NATIVE



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['RACE', 'GENDER'])
print_keys(grouped_patients)
```

    WHITE M
    WHITE F
    NATIVE F



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['ETHNICITY'])
print_keys(grouped_patients)
```

    ITALIAN
    IRISH
    RUSSIAN
    AMERICAN_INDIAN
    ENGLISH
    AMERICAN
    GERMAN



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['RACE', 'ETHNICITY'])
print_keys(grouped_patients)
```

    WHITE ITALIAN
    WHITE IRISH
    WHITE RUSSIAN
    WHITE ENGLISH
    WHITE AMERICAN
    WHITE GERMAN
    NATIVE AMERICAN_INDIAN



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['RACE', 'ETHNICITY', 'BIRTHPLACE', 'GENDER'])
print_keys(grouped_patients)
```

    WHITE ITALIAN WORCESTER  MASSACHUSETTS  US M
    WHITE ITALIAN MILFORD  MASSACHUSETTS  US M
    WHITE IRISH REVERE  MASSACHUSETTS  US F
    WHITE IRISH GROTON  MASSACHUSETTS  US F
    WHITE IRISH TAUNTON  MASSACHUSETTS  US F
    WHITE RUSSIAN BOSTON  MASSACHUSETTS  US F
    WHITE ENGLISH BOSTON  MASSACHUSETTS  US M
    WHITE AMERICAN FRAMINGHAM  MASSACHUSETTS  US F
    WHITE GERMAN NANTUCKET  MASSACHUSETTS  US M
    NATIVE AMERICAN_INDIAN HARWICH  MASSACHUSETTS  US F

