---
layout: default
title: 01 - Generating Fake Data
parent: Topic 03 - Generating Data
grand_parent: Lectures
nav_order: 1
---
# Generating Fake Data

It's often useful, especially in healthcare, to generate fake data in order to test your system while protecting the privacy of your production data sets.


```python
## let's generate a fake person
```


```python
person = {}
```


```python
type(person)
```




    dict




```python
print(person)
```

    {}



```python
person['age'] = 28
```


```python
type(person['age'])
```




    int




```python
print(person)
```

    {'age': 28}



```python
# let's generate a random age
import random
person['age'] = random.randrange(100)
print(person)
```

    {'age': 24}



```python
random.randrange?
```


    [0;31mSignature:[0m [0mrandom[0m[0;34m.[0m[0mrandrange[0m[0;34m([0m[0mstart[0m[0;34m,[0m [0mstop[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0mstep[0m[0;34m=[0m[0;36m1[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Choose a random item from range(start, stop[, step]).
    
    This fixes the problem with randint() which includes the
    endpoint; in Python this is usually not what you want.
    [0;31mFile:[0m      ~/opt/miniconda3/envs/cmu39/lib/python3.9/random.py
    [0;31mType:[0m      method




```python
person['age'] = random.randrange(100)
print(person)
```

    {'age': 5, 'employment': 40}



```python
# in healthcare kids and elderly have special coverage so let's exclude both groups
person['age'] = random.randint(18, 65)
print(person)
```

    {'age': 31}



```python
person['employment'] = 'Full Time'
print(type(person['employment']))
print(person)
```

    <class 'str'>
    {'age': 5, 'employment': 'Full Time'}



```python
# let's set employment status
employment_status = ['Full Time', 'Part Time', 'Contract', 'Seasonal', 'Unemployed', 'Retired']
person['employment'] = random.choice(employment_status)
print(person)
```

    {'age': 5, 'employment': 'Seasonal'}



```python
person['employment'] = random.choice(employment_status)
print(person)
```

    {'age': 5, 'employment': 'Full Time'}



```python
choice = random.choices(employment_status, [.5, .2, .1, .1, .05, .05])
print(f"Choice has type {type(choice)} and len {len(choice)}")
print(choice)

person['employment'] = choice[0]
print(person)
```

    Choice has type <class 'list'> and len 1
    ['Full Time']
    {'age': 5, 'employment': 'Full Time'}



```python
person['employment'] = random.choices(employment_status, [.5, .2, .1, .1, .05, .05],k=1)[0]
print(person)
```

    {'age': 5, 'employment': 'Part Time'}



```python
def generate_employment():
    employment_status = ['Full Time', 'Part Time', 'Contract', 'Seasonal', 'Unemployed', 'Retired']
    employment = random.choices(employment_status, [.5, .2, .1, .1, .05, .05])[0]
    return employment
```


```python
print(generate_employment())
print(generate_employment())
print(generate_employment())
```

    Contract
    Seasonal
    Seasonal



```python
# let's construct some fake addresses
def generate_address():
    street_number = random.randint(1, 1000)
    street_name = random.choice(['Main', 'Bluff', 'Federal'])
#     city = random.choice(['Pittsburgh', 'Cleveland' ])
#     city_details = { 'Pittsburgh' : { 'zip': 15106, 'state': 'PA' },
#                     'Cleveland' : { 'zip': 44101, 'state': 'OH' } }
#     state = city_details[city]['state']
#     zip_code = city_details[city]['zip']

    city_details = random.choice([
        { 'city': 'Pittsburgh', 'zip': 15106, 'state': 'PA' }, 
        { 'city': 'Cleveland', 'zip': 44101, 'state': 'OH' } ])
    
    city = city_details['city']
    state = city_details['state']
    zip_code = city_details['zip']
    
    address = f"{street_number} {street_name}\n{city}, {state} {zip_code}"
    return address
```


```python
address = generate_address()
print(address)
```

    257 Federal
    Pittsburgh, PA 15106



```python
def generate_name():
    first = ['Ben', 'Jen', 'Joan', 'John']
    last = ['Jones', 'Smith', 'Doe']
    return f"{random.choice(first)} {random.choice(last)}"
```


```python
name = generate_name()
print(name)
```

    Jen Doe



```python
def generate_person():
    person = {}
    person['name'] = generate_name()
    person['address'] = generate_address()
    person['employment'] = generate_employment()
    return person
```


```python
person = generate_person()
print(type(person))
print(person)
```

    <class 'dict'>
    {'name': 'Ben Doe', 'address': '905 Main\nCleveland, OH 44101', 'employment': 'Contract'}



```python
person = generate_person()
print(person)
```

    {'name': 'Joan Smith', 'address': '617 Bluff\nPittsburgh, PA 15106', 'employment': 'Seasonal'}



```python
person = generate_person()
print(person)
```

    {'name': 'Jen Doe', 'address': '83 Main\nCleveland, OH 44101', 'employment': 'Retired'}



```python

```
