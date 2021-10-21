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
print(person)
```

    {}



```python
person['age'] = 28
```


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

    {'age': 41, 'employeed': 'Full Time'}



```python
person['age'] = random.randrange(100)
print(person)
```

    {'age': 80}



```python
# in healthcare kids and elderly have special coverage so let's exclude both groups
person['age'] = random.randint(18, 65)
print(person)
```

    {'age': 55, 'employeed': 'Full Time'}



```python
person['employment'] = 'Full Time'
print(person)
```

    {'age': 55, 'employeed': 'Part Time', 'employment': 'Full Time'}



```python
# let's set employment status
employment_status = ['Full Time', 'Part Time', 'Contract', 'Seasonal', 'Unemployed', 'Retired']
person['employment'] = random.choice(employment_status)
print(person)
```

    {'age': 55, 'employeed': 'Part Time', 'employment': 'Contract'}



```python
person['employment'] = random.choice(employment_status)
print(person)
```

    {'age': 55, 'employeed': 'Part Time', 'employment': 'Contract'}



```python
person['employment'] = random.choices(employment_status, [.5, .2, .1, .1, .05, .05])[0]
print(person)
```

    {'age': 55, 'employeed': 'Part Time', 'employment': 'Retired'}



```python
person['employment'] = random.choices(employment_status, [.5, .2, .1, .1, .05, .05])[0]
print(person)
```

    {'age': 55, 'employeed': 'Part Time', 'employment': 'Full Time'}



```python
def generate_employment():
    employment_status = ['Full Time', 'Part Time', 'Contract', 'Seasonal', 'Unemployed', 'Retired']
    employment = random.choices(employment_status, [.5, .2, .1, .1, .05, .05])[0]
    return employment
    
```


```python
# let's construct some fake addresses
def generate_address():
    street_number = random.randint(1, 100)
    street_name= random.choice(['Main', 'Bluff', 'Federal'])
    city = random.choice(['Pittsburgh', 'Cleveland' ])

    city_details = { 'Pittsburgh' : { 'zip': 15106, 'state': 'PA' },
                    'Cleveland' : { 'zip': 44101, 'state': 'OH' } }
    state = city_details[city]['zip']
    zip_code = city_details[city]['state']
    
    address = f"{street_number} {street_name}\n{city}, {state} {zip_code}"
    return address
```


```python
address = generate_address()
print(address)
```

    Pittsburgh
    14 Federal
    Pittsburgh, 15106 PA



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
print(person)
```

    {'name': 'Ben Smith', 'address': '91 Bluff\nPittsburgh, 15106 PA', 'employment': 'Full Time'}



```python
person = generate_person()
print(person)
```

    {'name': 'John Jones', 'address': '35 Federal\nCleveland, 44101 OH', 'employment': 'Retired'}



```python
person = generate_person()
print(person)
```

    {'name': 'John Doe', 'address': '86 Main\nCleveland, 44101 OH', 'employment': 'Contract'}



```python

```
