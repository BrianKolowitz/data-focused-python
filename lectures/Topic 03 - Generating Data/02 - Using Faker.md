---
layout: default
title: 02 - Using Faker
parent: Topic 03 - Generating Data
grand_parent: Lectures
nav_order: 2
---
# Using Faker
[Source](https://zetcode.com/python/faker/)

## Basic Usage


```python
# import the library
from faker import Faker
```


```python
# create an instance
faker = Faker()
```


```python
# generate a name
faker.name()
```




    'Vincent Allen'




```python
# generate another name
faker.name()
```




    'Dawn Harvey'




```python
# generate an address
faker.address()
```




    '11351 Elizabeth Canyon\nLake Sarah, NE 29707'




```python
# generate another address
faker.address()
```




    '1006 Jessica Mills\nBrewerview, MO 39072'




```python
# generate some random text
faker.text()
```




    'Help politics watch space study beautiful. If focus firm again.\nPay up subject. Will particularly have be article clear season. Participant huge name notice.'



## Name Related Data


```python
faker.name()
```




    'Amy Roberson'




```python
faker.first_name()
```




    'Antonio'




```python
faker.last_name()
```




    'Odom'



## Faking Jobs


```python
faker.job()
```




    'Microbiologist'




```python
faker.job()
```




    'Health promotion specialist'




```python
for _ in range(5):
    print(faker.job())
```

    Surveyor, insurance
    Engineer, chemical
    Cytogeneticist
    Drilling engineer
    Production assistant, radio


## Faking Locale Data


```python
faker = Faker('cz_CZ')

for i in range(3):
    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()
    
    print(f'{name}, {address}, {phone}')
```

    Miroslava Kratochvílová, Komenského Nám. 91
    595 83 Kojetín, 601 108 913
    Kryštof Bartoš, Lednická 347
    649 34 Horní Jelení, 723 227 473
    Bohuslav Urban, Na Staré Vinici 50
    609 26 Hostomice, 603 178 388


## Faking Currencies


```python
faker = Faker()
```


```python
faker.currency()
```




    ('GNF', 'Guinean franc')




```python
faker.currency_name()
```




    'Jersey pound'




```python
faker.currency_code()
```




    'AWG'



## Faking words


```python
faker.word()
```




    'care'




```python
faker.words(10)
```




    ['its',
     'pattern',
     'concern',
     'road',
     'couple',
     'common',
     'value',
     'our',
     'either',
     'world']




```python
my_words = ['forrest', 'blue', 'cloud', 'sky', 'wood', 'falcon']
faker.words(3, my_words, True)
```




    ['blue', 'cloud', 'wood']



## Faking profiles


```python
profile1 = faker.simple_profile()
print(profile1)
```

    {'username': 'churchjames', 'name': 'Victoria Ryan MD', 'sex': 'F', 'address': '90570 Hannah Stream\nSouth Shelly, TN 77015', 'mail': 'kelli28@yahoo.com', 'birthdate': datetime.date(1949, 7, 30)}



```python
import dumper
dumper.dump(profile1)
```

    <dict at 0x7ffcc004d380>:
      username: 'churchjames'
      name: 'Victoria Ryan MD'
      sex: 'F'
      address: '90570 Hannah Stream\nSouth Shelly, TN 77015'
      mail: 'kelli28@yahoo.com'
      birthdate: <str at 0x7ffcc00503a0>: 'datetime.date(1949, 7, 30)'



```python
profile2 = faker.simple_profile('F')
dumper.dump(profile2)
```

    <dict at 0x7ffcc0047200>:
      username: 'qjohnston'
      name: 'Jessica Gillespie'
      sex: 'F'
      address: '69654 Megan Rest\nPatriciafurt, MD 35261'
      mail: 'jessicasmith@hotmail.com'
      birthdate: <str at 0x7ffcc00509e0>: 'datetime.date(1949, 4, 3)'


## Faking Numbers


```python
faker.random_int()
```




    1717




```python
faker.random_int(18, 64)
```




    31




```python
faker.random_digit()
```




    1



## Faking hashes and uids


```python
faker.md5()
```




    '1e7bfd5eb691a36a94af457b383f375e'




```python
faker.sha1()
```




    '0c83ab884516f9ef6f877a4d077a16630354b001'




```python
faker.sha256()
```




    'b239734a398a4c8005beefefd98a772c896dc5966f6233d74a398988d98714d3'




```python
faker.uuid4()
```




    'b914121e-63e4-4610-a1df-2555719ba7b8'



## Faking internet related data


```python
faker.email()
```




    'kellylester@example.org'




```python
faker.safe_email()
```




    'powellbenjamin@example.com'




```python
faker.free_email()
```




    'mphillips@gmail.com'




```python
faker.company_email()
```




    'seancarroll@murray.info'




```python
faker.hostname()
```




    'srv-25.williamson-johnson.com'




```python
faker.domain_name()
```




    'wilson.org'




```python
faker.domain_word()
```




    'clark'




```python
faker.tld()
```




    'org'




```python
faker.ipv4()
```




    '31.17.120.149'




```python
faker.ipv6()
```




    'e4d1:cfad:4a05:b049:cb63:5889:8094:c571'




```python
faker.slug()
```




    'occur-bed-work-yet'




```python
faker.image_url()
```




    'https://placekitten.com/727/516'



## Faking date and time

faker.date_of_birth()


```python
faker.century()
```




    'XV'




```python
faker.year()
```




    '1991'




```python
faker.month()
```




    '09'




```python
faker.month_name()
```




    'November'




```python
faker.day_of_week()
```




    'Sunday'




```python
faker.day_of_month()
```




    '01'




```python
faker.timezone()
```




    'America/Paramaribo'




```python
faker.am_pm()
```




    'AM'



## Specific Date Time


```python
faker.date_time_this_century()
```




    datetime.datetime(2018, 2, 9, 20, 51, 37)




```python
faker.date_time_this_decade()
```




    datetime.datetime(2020, 1, 12, 23, 48, 1)




```python
faker.date_time_this_year()
```




    datetime.datetime(2021, 6, 11, 20, 16, 29)




```python
faker.date_time_this_month()
```




    datetime.datetime(2021, 10, 6, 18, 59, 38)




```python
faker.date_this_century()
```




    datetime.date(2013, 10, 11)




```python
faker.date_this_decade()
```




    datetime.date(2021, 4, 1)




```python
faker.date_this_year()
```




    datetime.date(2021, 8, 28)




```python
faker.date_this_month()
```




    datetime.date(2021, 10, 20)




```python
TOTAL_SECONDS = 60*60*24*2 # two days

series = faker.time_series(start_date='-12d', end_date='now', precision=TOTAL_SECONDS)

for val in series:
    print(val[0])
```

    2021-10-16 15:13:18
    2021-10-18 15:13:18
    2021-10-20 15:13:18
    2021-10-22 15:13:18
    2021-10-24 15:13:18
    2021-10-26 15:13:18


## More Date Time


```python
faker.unix_time()
```




    1251085387




```python
faker.date_time()
```




    datetime.datetime(1976, 7, 17, 20, 43, 28)




```python
faker.iso8601()
```




    '1982-11-03T07:46:42'




```python
faker.date()
```




    '1990-08-27'




```python
faker.time()
```




    '12:55:01'




```python
print(f"Datetime between: {faker.date_time_between(start_date='-15y', end_date='now')}")
print(f"Date between: {faker.date_between()}")
```

    Datetime between: 2007-07-11 14:37:20
    Date between: 1993-01-12



```python
faker.future_datetime()
```




    datetime.datetime(2021, 11, 9, 6, 55, 23)




```python
faker.future_date()
```




    datetime.date(2021, 11, 18)




```python
faker.past_datetime()
```




    datetime.datetime(2021, 9, 29, 8, 18, 48)




```python
faker.past_date()
```




    datetime.date(2021, 10, 23)



## Generating XML Data


```python
from jinja2 import Environment, FileSystemLoader
```


```python
class User:
    def __init__(self, first_name, last_name, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation

```


```python
faker = Faker()
```


```python
users = []
```


```python
for _ in range(10):
    first_name = faker.first_name()
    last_name = faker.last_name()
    occupation = faker.job()
    
    user = User(first_name, last_name, occupation)
    
    users.append(user)
```


```python
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('users.xml.j2')
output = template.render(users=users)
```


```python
print(output)
```

    <?xml version="1.0" encoding="UTF-8"?>
    <users>
        
        <user id="1">
            <firstname>Cheryl</firstname>
            <lastname>Howard</lastname>
            <occupation>Community arts worker</occupation>
        </user>
        
        <user id="2">
            <firstname>Jessica</firstname>
            <lastname>Miller</lastname>
            <occupation>Magazine features editor</occupation>
        </user>
        
        <user id="3">
            <firstname>Alexandra</firstname>
            <lastname>Hill</lastname>
            <occupation>Ceramics designer</occupation>
        </user>
        
        <user id="4">
            <firstname>Lindsay</firstname>
            <lastname>Holland</lastname>
            <occupation>Economist</occupation>
        </user>
        
        <user id="5">
            <firstname>Kevin</firstname>
            <lastname>Michael</lastname>
            <occupation>Nurse, children's</occupation>
        </user>
        
        <user id="6">
            <firstname>Amanda</firstname>
            <lastname>Bush</lastname>
            <occupation>IT trainer</occupation>
        </user>
        
        <user id="7">
            <firstname>Candice</firstname>
            <lastname>Oliver</lastname>
            <occupation>Quantity surveyor</occupation>
        </user>
        
        <user id="8">
            <firstname>Brian</firstname>
            <lastname>Powell</lastname>
            <occupation>Advice worker</occupation>
        </user>
        
        <user id="9">
            <firstname>Sarah</firstname>
            <lastname>Graham</lastname>
            <occupation>Heritage manager</occupation>
        </user>
        
        <user id="10">
            <firstname>Frank</firstname>
            <lastname>Acevedo</lastname>
            <occupation>Archivist</occupation>
        </user>
        
    </users>



```python
# write output to file
print(output, file=open('users.xml', 'w'))
```


```python

```
