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




    'David Morgan'




```python
# generate another name
faker.name()
```




    'Larry Vazquez'




```python
# generate an address
print(faker.address())
```

    083 Potter Divide Apt. 274
    North Rachel, NH 28466



```python
# generate another address
faker.address()
```




    'Unit 7082 Box 1816\nDPO AP 95391'




```python
# generate some random text
faker.text()
```




    'If small tax forget. Concern off student only.\nDecision art travel one piece morning.\nHour himself free. What budget ahead. Reflect suffer under today personal reach art.'



## Name Related Data


```python
faker.name()
```




    'Eric Robinson'




```python
faker.first_name()
```




    'Jerry'




```python
faker.last_name()
```




    'Smith'



## Faking Jobs


```python
faker.job()
```




    'Sales promotion account executive'




```python
faker.job()
```




    'Embryologist, clinical'




```python
for _ in range(5):
    print(faker.job())
```

    Publishing copy
    Lighting technician, broadcasting/film/video
    Teacher, English as a foreign language
    Interpreter
    Counsellor



```python
for i in range(5):
    print(f"{i + 1}. {faker.job()}")
```

    1. Scientist, research (maths)
    2. Academic librarian
    3. Editor, film/video
    4. Art gallery manager
    5. Air traffic controller


## Faking Locale Data


```python
faker = Faker('cz_CZ')

for i in range(3):
    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()
    
    print(f'{name}, {address}, {phone}')
```

    Zdeněk Čermák, Vlčická 3
    495 33 Blšany, 722 592 894
    Martin Mašek, Nad Vernerákem 27
    165 30 Lovosice, 721 376 849
    Štěpánka Bláhová Ph.D., Výravská 7
    261 95 Plesná, 606 921 534



```python
faker.text()
```




    'Pro vzduch těsně bydlet dobře věc. Jedinec řeč dohromady domov. Kvůli liga moci.\nPovažovat zápas komora. Uvědomovat večer prostředí doufat.'



## Faking Currencies


```python
faker = Faker()
```


```python
faker.currency()
```




    ('ZWD', 'Zimbabwean dollar')




```python
faker.currency_name()
```




    'Swazi lilangeni'




```python
faker.currency_code()
```




    'XAF'



## Faking words


```python
faker.word()
```




    'trial'




```python
faker.words(10)
```




    ['purpose',
     'watch',
     'left',
     'education',
     'physical',
     'though',
     'beat',
     'hot',
     'opportunity',
     'center']




```python
my_words = ['forrest', 'blue', 'cloud', 'sky', 'wood', 'falcon']
faker.words(3, my_words, True)
```




    ['blue', 'wood', 'forrest']



## Faking profiles


```python
profile1 = faker.simple_profile()
print(profile1)
```

    {'username': 'vwilliams', 'name': 'Tyler Berger', 'sex': 'M', 'address': '6887 Brown Underpass\nBowmanton, MN 11805', 'mail': 'james25@hotmail.com', 'birthdate': datetime.date(1939, 9, 6)}



```python
import dumper
dumper.dump(profile1)
```

    <dict at 0x7ffcf09faf80>:
      username: 'vwilliams'
      name: 'Tyler Berger'
      sex: 'M'
      address: '6887 Brown Underpass\nBowmanton, MN 11805'
      mail: 'james25@hotmail.com'
      birthdate: <str at 0x7ffcf0a034e0>: 'datetime.date(1939, 9, 6)'



```python
profile2 = faker.simple_profile('F')
dumper.dump(profile2)
```

    <dict at 0x7ffcf09fff00>:
      username: 'ehood'
      name: 'Brittany Jones'
      sex: 'F'
      address: '5163 Smith Lane Suite 735\nHeatherport, MD 13036'
      mail: 'smithsara@yahoo.com'
      birthdate: <str at 0x7ffcf0a03940>: 'datetime.date(1983, 6, 14)'


## Faking Numbers


```python
faker.random_int()
```




    4729




```python
faker.random_int(18, 64)
```




    30




```python
faker.random_digit()
```




    7



## Faking hashes and uids


```python
faker.md5()
```




    '932840fb34c8fd3bbcea0c94c1569144'




```python
faker.sha1()
```




    'fdfd557712dcb6012e5c05f3a4208176bc729fed'




```python
faker.sha256()
```




    'a8fecb6662e6cff9e440011dccb3fd983f07a3f995d9fda3eace5119bf7764b5'




```python
faker.uuid4()
```




    'cfd30aed-6625-4aae-abdd-bac724d9309f'



## Faking internet related data


```python
faker.email()
```




    'phillipsmisty@example.net'




```python
faker.safe_email()
```




    'kelseyhardin@example.net'




```python
faker.free_email()
```




    'jacksondenise@yahoo.com'




```python
faker.company_email()
```




    'lweaver@thomas.biz'




```python
faker.hostname()
```




    'srv-84.williams-miller.com'




```python
faker.domain_name()
```




    'richardson-jones.com'




```python
faker.domain_word()
```




    'parks'




```python
faker.tld()
```




    'com'




```python
faker.ipv4()
```




    '56.135.73.35'




```python
faker.ipv6()
```




    '421c:3737:f872:45f2:cb41:de7f:c16f:3edc'




```python
faker.slug()
```




    'as-present'




```python
faker.image_url()
```




    'https://placeimg.com/864/562/any'



## Faking date and time

faker.date_of_birth()


```python
faker.century()
```




    'IV'




```python
faker.year()
```




    '1997'




```python
faker.month()
```




    '07'




```python
faker.month_name()
```




    'April'




```python
faker.day_of_week()
```




    'Wednesday'




```python
faker.day_of_month()
```




    '28'




```python
faker.timezone()
```




    'Europe/Sofia'




```python
faker.am_pm()
```




    'AM'



## Specific Date Time


```python
faker.date_time_this_century()
```




    datetime.datetime(2011, 9, 28, 23, 57, 17)




```python
faker.date_time_this_decade()
```




    datetime.datetime(2021, 3, 23, 14, 46, 39)




```python
faker.date_time_this_year()
```




    datetime.datetime(2021, 10, 19, 7, 48, 6)




```python
faker.date_time_this_month()
```




    datetime.datetime(2021, 10, 28, 6, 51, 31)




```python
faker.date_this_century()
```




    datetime.date(2009, 8, 9)




```python
faker.date_this_decade()
```




    datetime.date(2020, 4, 13)




```python
faker.date_this_year()
```




    datetime.date(2021, 4, 20)




```python
faker.date_this_month()
```




    datetime.date(2021, 10, 22)




```python
TOTAL_SECONDS = 60*60*24*2 # two days

series = faker.time_series(start_date='-12d', end_date='now', precision=TOTAL_SECONDS)

for val in series:
    print(val[0])
```

    2021-10-16 19:20:16
    2021-10-18 19:20:16
    2021-10-20 19:20:16
    2021-10-22 19:20:16
    2021-10-24 19:20:16
    2021-10-26 19:20:16


## More Date Time


```python
faker.unix_time()
```




    151348603




```python
faker.date_time()
```




    datetime.datetime(2013, 8, 17, 14, 19, 18)




```python
faker.iso8601()
```




    '2013-03-16T04:58:24'




```python
faker.date()
```




    '1988-01-12'




```python
faker.time()
```




    '17:57:23'




```python
print(f"Datetime between: {faker.date_time_between(start_date='-15y', end_date='now')}")
print(f"Date between: {faker.date_between()}")
```

    Datetime between: 2017-04-02 08:44:03
    Date between: 1998-03-24



```python
faker.future_datetime()
```




    datetime.datetime(2021, 11, 13, 5, 5, 44)




```python
faker.future_date()
```




    datetime.date(2021, 11, 20)




```python
faker.past_datetime()
```




    datetime.datetime(2021, 10, 12, 0, 30, 37)




```python
faker.past_date()
```




    datetime.date(2021, 10, 20)



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
            <firstname>Joel</firstname>
            <lastname>Robinson</lastname>
            <occupation>Publishing rights manager</occupation>
        </user>
        
        <user id="2">
            <firstname>Lynn</firstname>
            <lastname>Brady</lastname>
            <occupation>Producer, television/film/video</occupation>
        </user>
        
        <user id="3">
            <firstname>Calvin</firstname>
            <lastname>Mendoza</lastname>
            <occupation>Public librarian</occupation>
        </user>
        
        <user id="4">
            <firstname>Marcus</firstname>
            <lastname>Herring</lastname>
            <occupation>Theatre stage manager</occupation>
        </user>
        
        <user id="5">
            <firstname>Patricia</firstname>
            <lastname>Hamilton</lastname>
            <occupation>Fisheries officer</occupation>
        </user>
        
        <user id="6">
            <firstname>Melanie</firstname>
            <lastname>Lyons</lastname>
            <occupation>Scientist, research (life sciences)</occupation>
        </user>
        
        <user id="7">
            <firstname>Alexander</firstname>
            <lastname>Cruz</lastname>
            <occupation>Production designer, theatre/television/film</occupation>
        </user>
        
        <user id="8">
            <firstname>Blake</firstname>
            <lastname>Anderson</lastname>
            <occupation>Doctor, general practice</occupation>
        </user>
        
        <user id="9">
            <firstname>Bryan</firstname>
            <lastname>Rojas</lastname>
            <occupation>Civil engineer, consulting</occupation>
        </user>
        
        <user id="10">
            <firstname>Dennis</firstname>
            <lastname>Scott</lastname>
            <occupation>Research officer, political party</occupation>
        </user>
        
        <user id="11">
            <firstname>Briana</firstname>
            <lastname>Rios</lastname>
            <occupation>Illustrator</occupation>
        </user>
        
        <user id="12">
            <firstname>Carla</firstname>
            <lastname>Gutierrez</lastname>
            <occupation>Communications engineer</occupation>
        </user>
        
        <user id="13">
            <firstname>Maureen</firstname>
            <lastname>Lewis</lastname>
            <occupation>Armed forces logistics/support/administrative officer</occupation>
        </user>
        
        <user id="14">
            <firstname>Susan</firstname>
            <lastname>Bennett</lastname>
            <occupation>Lighting technician, broadcasting/film/video</occupation>
        </user>
        
        <user id="15">
            <firstname>Douglas</firstname>
            <lastname>Brown</lastname>
            <occupation>Technical brewer</occupation>
        </user>
        
        <user id="16">
            <firstname>James</firstname>
            <lastname>Greer</lastname>
            <occupation>Retail buyer</occupation>
        </user>
        
        <user id="17">
            <firstname>Eric</firstname>
            <lastname>Rogers</lastname>
            <occupation>Customer service manager</occupation>
        </user>
        
        <user id="18">
            <firstname>Lisa</firstname>
            <lastname>Chambers</lastname>
            <occupation>Broadcast engineer</occupation>
        </user>
        
        <user id="19">
            <firstname>Steven</firstname>
            <lastname>Herrera</lastname>
            <occupation>Building services engineer</occupation>
        </user>
        
        <user id="20">
            <firstname>Emma</firstname>
            <lastname>Lopez</lastname>
            <occupation>Gaffer</occupation>
        </user>
        
    </users>



```python
# write output to file
print(output, file=open('users.xml', 'w'))
```


```python

```
