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




    'Mary Peterson'




```python
# generate another name
faker.name()
```




    'Samuel Nguyen'




```python
# generate an address
faker.address()
```




    '66360 Aguilar Skyway Apt. 156\nDawsonview, NE 36387'




```python
# generate another address
faker.address()
```




    '577 Michael Springs\nNorth Thomasland, NC 57297'




```python
# generate some random text
faker.text()
```




    'Story effort work staff major. There girl foreign. Economic practice either common person generation. Population list most people decision himself call.'



## Name Related Data


```python
faker.name()
```




    'Kimberly Miller DVM'




```python
faker.first_name()
```




    'William'




```python
faker.last_name()
```




    'Potts'



## Faking Jobs


```python
faker.job()
```




    'Tourist information centre manager'




```python
faker.job()
```




    'Radio broadcast assistant'




```python
for _ in range(5):
    print(faker.job())
```

    Logistics and distribution manager
    Patent attorney
    Designer, multimedia
    Holiday representative
    Psychologist, forensic


## Faking Locale Data


```python
faker = Faker('cz_CZ')

for i in range(3):
    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()
    
    print(f'{name}, {address}, {phone}')
```

    Radka Krejčová, Pikovická 5
    135 29 Česká Skalice, 790 939 153
    Iva Malá, Vašátkova 973
    355 57 Český Dub, 732 872 338
    Žaneta Moravcová, Na Cikánce 5
    411 12 Zruč nad Sázavou, 722 413 421


## Faking Currencies


```python
faker = Faker()
```


```python
faker.currency()
```




    ('VUV', 'Vanuatu vatu')




```python
faker.currency_name()
```




    'Burmese kyat'




```python
faker.currency_code()
```




    'SYP'



## Faking words


```python
faker.word()
```




    'school'




```python
faker.words(10)
```




    ['agency',
     'production',
     'wide',
     'tell',
     'themselves',
     'close',
     'hear',
     'these',
     'cold',
     'ahead']




```python
my_words = ['forrest', 'blue', 'cloud', 'sky', 'wood', 'falcon']
faker.words(3, my_words, True)
```




    ['forrest', 'blue', 'falcon']



## Faking profiles


```python
profile1 = faker.simple_profile()
print(profile1)
```

    {'username': 'rhuynh', 'name': 'Rebecca Bryant', 'sex': 'F', 'address': '49969 Hill Light Apt. 617\nMichaelton, MT 10598', 'mail': 'patrickmartin@hotmail.com', 'birthdate': datetime.date(1918, 1, 12)}



```python
import dumper
dumper.dump(profile1)
```

    <dict at 0x7fb0998fb580>:
      username: 'rhuynh'
      name: 'Rebecca Bryant'
      sex: 'F'
      address: '49969 Hill Light Apt. 617\nMichaelton, MT 10598'
      mail: 'patrickmartin@hotmail.com'
      birthdate: <str at 0x7fb09b4ab760>: 'datetime.date(1918, 1, 12)'



```python
profile2 = faker.simple_profile('F')
dumper.dump(profile2)
```

    <dict at 0x7fb09b4f7880>:
      username: 'christopherrodgers'
      name: 'Donna Berry'
      sex: 'F'
      address: '42662 Orr Ridges Suite 300\nNorth Alexisview, MA 98751'
      mail: 'hcrawford@hotmail.com'
      birthdate: <str at 0x7fb09b4abda0>: 'datetime.date(1990, 3, 4)'


## Faking Numbers


```python
faker.random_int()
```




    6029




```python
faker.random_int(18, 64)
```




    48




```python
faker.random_digit()
```




    5



## Faking hashes and uids


```python
faker.md5()
```




    'd03a2a604b262b4d157d944ecb8303c0'




```python
faker.sha1()
```




    '3197bcdec7121a375b88a6af9ba57838c5176552'




```python
faker.sha256()
```




    '9a748899c8d85a270e193fa712dc57f5d1807058b379c0db9cc7118c7f12a12d'




```python
faker.uuid4()
```




    '959bdf47-6819-425d-b512-d5a49597d989'



## Faking internet related data


```python
faker.email()
```




    'hopkinsvanessa@example.org'




```python
faker.safe_email()
```




    'davischarles@example.net'




```python
faker.free_email()
```




    'sanchezleah@yahoo.com'




```python
faker.company_email()
```




    'ashleewilliams@brown-wolfe.net'




```python
faker.hostname()
```




    'desktop-76.harris-ortiz.com'




```python
faker.domain_name()
```




    'smith.biz'




```python
faker.domain_word()
```




    'morrison-horton'




```python
faker.tld()
```




    'com'




```python
faker.ipv4()
```




    '188.141.18.11'




```python
faker.ipv6()
```




    '9b68:7c19:307:3214:87d1:b29:26c8:b835'




```python
faker.slug()
```




    'decision-air-adult'




```python
faker.image_url()
```




    'https://www.lorempixel.com/640/339'



## Faking date and time

faker.date_of_birth()


```python
faker.century()
```




    'III'




```python
faker.year()
```




    '1983'




```python
faker.month()
```




    '08'




```python
faker.month_name()
```




    'December'




```python
faker.day_of_week()
```




    'Friday'




```python
faker.day_of_month()
```




    '12'




```python
faker.timezone()
```




    'America/Panama'




```python
faker.am_pm()
```




    'AM'



## Specific Date Time


```python
faker.date_time_this_century()
```




    datetime.datetime(2018, 2, 2, 7, 29, 55)




```python
faker.date_time_this_decade()
```




    datetime.datetime(2020, 1, 20, 12, 29, 55)




```python
faker.date_time_this_year()
```




    datetime.datetime(2021, 6, 14, 22, 1, 24)




```python
faker.date_time_this_month()
```




    datetime.datetime(2021, 10, 20, 11, 47, 42)




```python
faker.date_this_century()
```




    datetime.date(2016, 3, 10)




```python
faker.date_this_decade()
```




    datetime.date(2020, 10, 6)




```python
faker.date_this_year()
```




    datetime.date(2021, 9, 7)




```python
faker.date_this_month()
```




    datetime.date(2021, 10, 19)




```python
TOTAL_SECONDS = 60*60*24*2 # two days

series = faker.time_series(start_date='-12d', end_date='now', precision=TOTAL_SECONDS)

for val in series:
    print(val[0])
```

    2021-10-09 15:09:25
    2021-10-11 15:09:25
    2021-10-13 15:09:25
    2021-10-15 15:09:25
    2021-10-17 15:09:25
    2021-10-19 15:09:25


## More Date Time


```python
faker.unix_time()
```




    498578330




```python
faker.date_time()
```




    datetime.datetime(1986, 11, 5, 4, 17, 14)




```python
faker.iso8601()
```




    '1986-05-21T22:10:26'




```python
faker.date()
```




    '2016-04-14'




```python
faker.time()
```




    '07:36:49'




```python
print(f"Datetime between: {faker.date_time_between(start_date='-15y', end_date='now')}")
print(f"Date between: {faker.date_between()}")
```

    Datetime between: 2007-07-08 04:32:13
    Date between: 1999-11-03



```python
faker.future_datetime()
```




    datetime.datetime(2021, 11, 14, 0, 37, 51)




```python
faker.future_date()
```




    datetime.date(2021, 11, 5)




```python
faker.past_datetime()
```




    datetime.datetime(2021, 10, 9, 21, 7, 21)




```python
faker.past_date()
```




    datetime.date(2021, 10, 3)



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
            <firstname>Christopher</firstname>
            <lastname>Gay</lastname>
            <occupation>Scientist, research (maths)</occupation>
        </user>
        
        <user id="2">
            <firstname>George</firstname>
            <lastname>Macias</lastname>
            <occupation>Television/film/video producer</occupation>
        </user>
        
        <user id="3">
            <firstname>Shelby</firstname>
            <lastname>Phelps</lastname>
            <occupation>Make</occupation>
        </user>
        
        <user id="4">
            <firstname>Jacqueline</firstname>
            <lastname>Mcdonald</lastname>
            <occupation>Freight forwarder</occupation>
        </user>
        
        <user id="5">
            <firstname>Melissa</firstname>
            <lastname>Banks</lastname>
            <occupation>Recycling officer</occupation>
        </user>
        
        <user id="6">
            <firstname>Elizabeth</firstname>
            <lastname>Snyder</lastname>
            <occupation>Forensic scientist</occupation>
        </user>
        
        <user id="7">
            <firstname>Juan</firstname>
            <lastname>Barnes</lastname>
            <occupation>Lobbyist</occupation>
        </user>
        
        <user id="8">
            <firstname>Rodney</firstname>
            <lastname>Macdonald</lastname>
            <occupation>Theatre director</occupation>
        </user>
        
        <user id="9">
            <firstname>Michael</firstname>
            <lastname>Mendez</lastname>
            <occupation>Careers information officer</occupation>
        </user>
        
        <user id="10">
            <firstname>Laura</firstname>
            <lastname>Melton</lastname>
            <occupation>Operations geologist</occupation>
        </user>
        
    </users>



```python
# write output to file
print(output, file=open('users.xml', 'w'))
```


```python

```
