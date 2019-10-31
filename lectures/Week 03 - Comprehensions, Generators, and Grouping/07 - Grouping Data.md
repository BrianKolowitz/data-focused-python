---
layout: default
title: 07 - Grouping Data
parent: Week 03 - Comprehensions, Generators, and Grouping
grand_parent: Lectures
nav_order: 8
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

    OrderedDict([('Id', 'c09181f8-6526-4de7-87c7-25c95ccdbdea'),
                 ('BIRTHDATE', '2014-06-06'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-26-1662'),
                 ('DRIVERS', ''),
                 ('PASSPORT', ''),
                 ('PREFIX', ''),
                 ('FIRST', 'Lizbeth716'),
                 ('LAST', 'Hackett68'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'irish'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Denver  Pennsylvania  US'),
                 ('ADDRESS', '742 Parisian Run Suite 87'),
                 ('CITY', 'Pittsburgh'),
                 ('STATE', 'Pennsylvania'),
                 ('ZIP', '15106')])
    OrderedDict([('Id', '8d1c4f3b-3d44-4daf-8962-cc260bad8c87'),
                 ('BIRTHDATE', '1969-05-10'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-64-1895'),
                 ('DRIVERS', 'S99989200'),
                 ('PASSPORT', 'X16155415X'),
                 ('PREFIX', 'Mrs.'),
                 ('FIRST', 'Augustine565'),
                 ('LAST', 'Conroy74'),
                 ('SUFFIX', ''),
                 ('MAIDEN', 'Cremin516'),
                 ('MARITAL', 'M'),
                 ('RACE', 'asian'),
                 ('ETHNICITY', 'asian_indian'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Unityship  Pennsylvania  US'),
                 ('ADDRESS', '931 Watsica Lock'),
                 ('CITY', 'Pittsburgh'),
                 ('STATE', 'Pennsylvania'),
                 ('ZIP', '15106')])



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

    F
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

    {'M', 'F'}



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

    OrderedDict([('Id', 'cb115d2a-56b5-42a7-bf64-0362505df9f2'),
                 ('BIRTHDATE', '1969-05-30'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-28-4068'),
                 ('DRIVERS', 'S99947751'),
                 ('PASSPORT', 'X52116181X'),
                 ('PREFIX', 'Mr.'),
                 ('FIRST', 'Rhett759'),
                 ('LAST', 'Mosciski958'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', 'M'),
                 ('RACE', 'asian'),
                 ('ETHNICITY', 'chinese'),
                 ('GENDER', 'M'),
                 ('BIRTHPLACE',
                  "Macau  Macao Special Administrative Region of the People's "
                  'Republic of China  CN'),
                 ('ADDRESS', '370 Gleichner Parade'),
                 ('CITY', 'Pittsburgh'),
                 ('STATE', 'Pennsylvania'),
                 ('ZIP', '15106')])
    OrderedDict([('Id', 'c09181f8-6526-4de7-87c7-25c95ccdbdea'),
                 ('BIRTHDATE', '2014-06-06'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-26-1662'),
                 ('DRIVERS', ''),
                 ('PASSPORT', ''),
                 ('PREFIX', ''),
                 ('FIRST', 'Lizbeth716'),
                 ('LAST', 'Hackett68'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'irish'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Denver  Pennsylvania  US'),
                 ('ADDRESS', '742 Parisian Run Suite 87'),
                 ('CITY', 'Pittsburgh'),
                 ('STATE', 'Pennsylvania'),
                 ('ZIP', '15106')])


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

    dict_keys(['F', 'M'])



```python
pprint(patients_by_gender['F'][0:2])
```

    [OrderedDict([('Id', 'c09181f8-6526-4de7-87c7-25c95ccdbdea'),
                  ('BIRTHDATE', '2014-06-06'),
                  ('DEATHDATE', ''),
                  ('SSN', '999-26-1662'),
                  ('DRIVERS', ''),
                  ('PASSPORT', ''),
                  ('PREFIX', ''),
                  ('FIRST', 'Lizbeth716'),
                  ('LAST', 'Hackett68'),
                  ('SUFFIX', ''),
                  ('MAIDEN', ''),
                  ('MARITAL', ''),
                  ('RACE', 'white'),
                  ('ETHNICITY', 'irish'),
                  ('GENDER', 'F'),
                  ('BIRTHPLACE', 'Denver  Pennsylvania  US'),
                  ('ADDRESS', '742 Parisian Run Suite 87'),
                  ('CITY', 'Pittsburgh'),
                  ('STATE', 'Pennsylvania'),
                  ('ZIP', '15106')]),
     OrderedDict([('Id', '8d1c4f3b-3d44-4daf-8962-cc260bad8c87'),
                  ('BIRTHDATE', '1969-05-10'),
                  ('DEATHDATE', ''),
                  ('SSN', '999-64-1895'),
                  ('DRIVERS', 'S99989200'),
                  ('PASSPORT', 'X16155415X'),
                  ('PREFIX', 'Mrs.'),
                  ('FIRST', 'Augustine565'),
                  ('LAST', 'Conroy74'),
                  ('SUFFIX', ''),
                  ('MAIDEN', 'Cremin516'),
                  ('MARITAL', 'M'),
                  ('RACE', 'asian'),
                  ('ETHNICITY', 'asian_indian'),
                  ('GENDER', 'F'),
                  ('BIRTHPLACE', 'Unityship  Pennsylvania  US'),
                  ('ADDRESS', '931 Watsica Lock'),
                  ('CITY', 'Pittsburgh'),
                  ('STATE', 'Pennsylvania'),
                  ('ZIP', '15106')])]



```python
print(patients_by_gender['F'][0]['LAST'])
```

    Hackett68


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

    [OrderedDict([('Id', 'c09181f8-6526-4de7-87c7-25c95ccdbdea'),
                  ('BIRTHDATE', '2014-06-06'),
                  ('DEATHDATE', ''),
                  ('SSN', '999-26-1662'),
                  ('DRIVERS', ''),
                  ('PASSPORT', ''),
                  ('PREFIX', ''),
                  ('FIRST', 'Lizbeth716'),
                  ('LAST', 'Hackett68'),
                  ('SUFFIX', ''),
                  ('MAIDEN', ''),
                  ('MARITAL', ''),
                  ('RACE', 'white'),
                  ('ETHNICITY', 'irish'),
                  ('GENDER', 'F'),
                  ('BIRTHPLACE', 'Denver  Pennsylvania  US'),
                  ('ADDRESS', '742 Parisian Run Suite 87'),
                  ('CITY', 'Pittsburgh'),
                  ('STATE', 'Pennsylvania'),
                  ('ZIP', '15106')]),
     OrderedDict([('Id', '8d1c4f3b-3d44-4daf-8962-cc260bad8c87'),
                  ('BIRTHDATE', '1969-05-10'),
                  ('DEATHDATE', ''),
                  ('SSN', '999-64-1895'),
                  ('DRIVERS', 'S99989200'),
                  ('PASSPORT', 'X16155415X'),
                  ('PREFIX', 'Mrs.'),
                  ('FIRST', 'Augustine565'),
                  ('LAST', 'Conroy74'),
                  ('SUFFIX', ''),
                  ('MAIDEN', 'Cremin516'),
                  ('MARITAL', 'M'),
                  ('RACE', 'asian'),
                  ('ETHNICITY', 'asian_indian'),
                  ('GENDER', 'F'),
                  ('BIRTHPLACE', 'Unityship  Pennsylvania  US'),
                  ('ADDRESS', '931 Watsica Lock'),
                  ('CITY', 'Pittsburgh'),
                  ('STATE', 'Pennsylvania'),
                  ('ZIP', '15106')])]



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

    OrderedDict([('Id', 'c09181f8-6526-4de7-87c7-25c95ccdbdea'),
                 ('BIRTHDATE', '2014-06-06'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-26-1662'),
                 ('DRIVERS', ''),
                 ('PASSPORT', ''),
                 ('PREFIX', ''),
                 ('FIRST', 'Lizbeth716'),
                 ('LAST', 'Hackett68'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'irish'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Denver  Pennsylvania  US'),
                 ('ADDRESS', '742 Parisian Run Suite 87'),
                 ('CITY', 'Pittsburgh'),
                 ('STATE', 'Pennsylvania'),
                 ('ZIP', '15106')])


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

    OrderedDict([('Id', 'c09181f8-6526-4de7-87c7-25c95ccdbdea'),
                 ('BIRTHDATE', '2014-06-06'),
                 ('DEATHDATE', ''),
                 ('SSN', '999-26-1662'),
                 ('DRIVERS', ''),
                 ('PASSPORT', ''),
                 ('PREFIX', ''),
                 ('FIRST', 'Lizbeth716'),
                 ('LAST', 'Hackett68'),
                 ('SUFFIX', ''),
                 ('MAIDEN', ''),
                 ('MARITAL', ''),
                 ('RACE', 'white'),
                 ('ETHNICITY', 'irish'),
                 ('GENDER', 'F'),
                 ('BIRTHPLACE', 'Denver  Pennsylvania  US'),
                 ('ADDRESS', '742 Parisian Run Suite 87'),
                 ('CITY', 'Pittsburgh'),
                 ('STATE', 'Pennsylvania'),
                 ('ZIP', '15106')])



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

    F WHITE
    F ASIAN
    F BLACK
    M ASIAN
    M WHITE



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

    {'M', 'F'} {'white', 'black', 'asian'}



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

    F WHITE IRISH
    F WHITE AMERICAN
    F WHITE GERMAN
    F WHITE ITALIAN
    F WHITE SCOTTISH
    F ASIAN ASIAN_INDIAN
    F BLACK DOMINICAN
    M ASIAN CHINESE
    M WHITE ITALIAN


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

    F WHITE IRISH
    F WHITE AMERICAN
    F WHITE GERMAN
    F WHITE ITALIAN
    F WHITE SCOTTISH
    F ASIAN ASIAN_INDIAN
    F BLACK DOMINICAN
    M ASIAN CHINESE
    M WHITE ITALIAN



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

    F WHITE IRISH
    F WHITE AMERICAN
    F WHITE GERMAN
    F WHITE ITALIAN
    F WHITE SCOTTISH
    F ASIAN ASIAN_INDIAN
    F BLACK DOMINICAN
    M ASIAN CHINESE
    M WHITE ITALIAN



```python
# lets try it out on a few examples
```


```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['GENDER'])
print_keys(grouped_patients)
```

    F
    M



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['RACE'])
print_keys(grouped_patients)
```

    WHITE
    ASIAN
    BLACK



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['GENDER', 'RACE'])
print_keys(grouped_patients)
```

    F WHITE
    F ASIAN
    F BLACK
    M ASIAN
    M WHITE



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['RACE', 'GENDER'])
print_keys(grouped_patients)
```

    WHITE F
    WHITE M
    ASIAN F
    ASIAN M
    BLACK F



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['ETHNICITY'])
print_keys(grouped_patients)
```

    IRISH
    ASIAN_INDIAN
    CHINESE
    AMERICAN
    DOMINICAN
    GERMAN
    ITALIAN
    SCOTTISH



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['RACE', 'ETHNICITY'])
print_keys(grouped_patients)
```

    WHITE IRISH
    WHITE AMERICAN
    WHITE GERMAN
    WHITE ITALIAN
    WHITE SCOTTISH
    ASIAN ASIAN_INDIAN
    ASIAN CHINESE
    BLACK DOMINICAN



```python
grouped_patients = group_file_by_list('../data/csv/patients.csv', ['RACE', 'ETHNICITY', 'BIRTHPLACE', 'GENDER'])
print_keys(grouped_patients)
```

    WHITE IRISH DENVER  PENNSYLVANIA  US F
    WHITE IRISH EAST EARLSHIP  PENNSYLVANIA  US F
    WHITE AMERICAN READINGSHIP  PENNSYLVANIA  US F
    WHITE GERMAN BROWNSVILLE  PENNSYLVANIA  US F
    WHITE ITALIAN UPPER ALLENSHIP  PENNSYLVANIA  US F
    WHITE ITALIAN BIRDSBORO  PENNSYLVANIA  US M
    WHITE SCOTTISH LEHMANSHIP  PENNSYLVANIA  US F
    ASIAN ASIAN_INDIAN UNITYSHIP  PENNSYLVANIA  US F
    ASIAN CHINESE MACAU  MACAO SPECIAL ADMINISTRATIVE REGION OF THE PEOPLE'S REPUBLIC OF CHINA  CN M
    BLACK DOMINICAN PHILADELPHIA  PENNSYLVANIA  US F



```python

```
