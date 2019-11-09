---
layout: default
title: 03 - Getting Data from a Database
parent: Week 01 - Language basics, Generating Data, Storing Data
grand_parent: Lectures
nav_order: 7
---

# SQLAlchemy — Python Tutorial
[Source](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)

Other References
* [What are Object Relational Mappers (ORMs)](https://www.fullstackpython.com/object-relational-mappers-orms.html)
* [SQLAlchemy Basics](https://leportella.com/english/2019/01/10/sqlalchemy-basics-tutorial.html)

We often encounter data as Relational Databases. To work with them we generally would need to write raw SQL queries, pass them to the database engine and parse the returned results as a normal array of records.

SQLAlchemy provides a nice “Pythonic” way of interacting with databases. So rather than dealing with the differences between specific dialects of traditional SQL such as MySQL or PostgreSQL or Oracle, you can leverage the Pythonic framework of SQLAlchemy to streamline your workflow and more efficiently query your data.


```python
# Installing The Package
!pip install sqlalchemy
```

## Connecting to a database

To start interacting with the database we first we need to establish a connection.

```python
import sqlalchemy as db
engine = db.create_engine('dialect+driver://user:pass@host:port/db')
```

### Database connection examples

[Source](https://docs.sqlalchemy.org/en/13/core/engines.html#postgresql)

#### PostgreSQL

```python
# default
engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')

# psycopg2
engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')

# pg8000
engine = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')
```

#### MySQL

```python
# default
engine = create_engine('mysql://scott:tiger@localhost/foo')

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

# PyMySQL
engine = create_engine('mysql+pymysql://scott:tiger@localhost/foo')
```

#### Oracle

```python
engine = create_engine('oracle://scott:tiger@127.0.0.1:1521/sidname')

engine = create_engine('oracle+cx_oracle://scott:tiger@tnsname')
```

#### Microsoft SQL Server

```python
# pyodbc
engine = create_engine('mssql+pyodbc://scott:tiger@mydsn')

# pymssql
engine = create_engine('mssql+pymssql://scott:tiger@hostname:port/dbname')
```

#### SQLite

```python
# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine('sqlite:///foo.db')

# Unix/Mac - 4 initial slashes in total
engine = create_engine('sqlite:////absolute/path/to/foo.db')

# Windows
engine = create_engine('sqlite:///C:\\path\\to\\foo.db')

# Windows alternative using raw string
engine = create_engine(r'sqlite:///C:\path\to\foo.db')

# To use a SQLite :memory: database, specify an empty URL:
engine = create_engine('sqlite://')
```

## Viewing Table Details

SQLAlchemy can be used to automatically load tables from a database using something called reflection. Reflection is the process of reading the database and building the metadata based on that information.


```python
import sqlalchemy as db
```


```python
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
```


```python
# Print the column names
print(census.columns.keys())
```


```python
# Print full table metadata
print(repr(metadata.tables['census']))
```

## Querying

```Table``` and ```MetaData``` have already been imported. The metadata is available as ```metadata```.


```python
import sqlalchemy as db
```


```python
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
```


```python
#Equivalent to 'SELECT * FROM census'
query = db.select([census])
```

**ResultProxy**: The object returned by the ```.execute()``` method. It can be used in a variety of ways to get the data returned by the query.


```python
ResultProxy = connection.execute(query)
```

**ResultSet**: The actual data asked for in the query when using a fetch method such as ```.fetchall()``` on a ResultProxy.


```python
ResultSet = ResultProxy.fetchall()
```


```python
ResultSet[:3]
```

### Dealing with Large ResultSet

We use ```.fetchmany()``` to load optimal no of rows and overcome memory issues in case of large datasets.


```python
ResultProxy = connection.execute(query)
# ResultSet = ResultProxy.fetchall()
```


```python
flag = True
while flag:
    print('*** new fetch')
    partial_results = ResultProxy.fetchmany(5)
    if(partial_results == []): 
        flag = False
    for result in partial_results:
        print('\t', result)

#     print(partial_results)
ResultProxy.close()
```

### Convert to DataFrame


```python
import pandas as pd
```


```python
df = pd.DataFrame(ResultSet)
df.columns = ResultSet[0].keys()
```


```python
df.head()
```

## Filtering data

Lets see some examples of raw SQLite Queries and queries using SQLAlchemy.

### where

**SQL**
```SQL
SELECT * FROM census 
WHERE sex = F
```


```python
# SQLAlchemy
db.select([census]).where(census.columns.sex == 'F')
```

### in

**SQL**
```SQL
SELECT state, sex
FROM census
WHERE state IN (Texas, New York)
```


```python
# SQLAlchemy
db.select([census.columns.state, census.columns.sex]) \
    .where(census.columns.state.in_(['Texas', 'New York']))
```

### and, or, not

**SQL**
```SQL
SELECT * FROM census
WHERE state = 'California' AND NOT sex = 'M'
```


```python
# SQLAlchemy
db.select([census]) \
    .where(db.and_(census.columns.state == 'California', 
                   census.columns.sex != 'M'))
```

### order by

**SQL**
```SQL
SELECT * FROM census
ORDER BY State DESC, pop2000
```


```python
# SQLAlchemy
db.select([census]).order_by(
        db.desc(census.columns.state), 
        census.columns.pop2000)
```

### functions

other functions include ```avg```, ```count```, ```min```, ```max```

**SQL**
```SQL
SELECT SUM(pop2008)
FROM census
```


```python
# SQLAlchemy
query = db.select([db.func.sum(census.columns.pop2008)])
ResultSet = connection.execute(query).fetchall()
pd.DataFrame(ResultSet)
```

### group by

**SQL**
```SQL
SELECT SUM(pop2008) as pop2008, sex
FROM census
GROUP BY sex
```


```python
# SQLAlchemy
query = db.select([db.func.sum(census.columns.pop2008).label('pop2008'), 
           census.columns.sex]).group_by(census.columns.sex)
ResultSet = connection.execute(query).fetchall()
pd.DataFrame(ResultSet)
```

### distinct

**SQL**
```SQL
SELECT DISTINCT state
FROM census
```


```python
# SQLAlchemy
query = db.select([census.columns.state.distinct()])
ResultSet = connection.execute(query).fetchall()
pd.DataFrame(ResultSet)
```

### case & cast

The ```case()``` expression accepts a list of conditions to match and the column to return if the condition matches, followed by an ```else_``` if none of the conditions match.

```cast()``` function to convert an expression to a particular type


```python
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
```


```python
female_pop = db.func.sum(
    db.case([(census.columns.sex == 'F', census.columns.pop2000)],
            else_=0))
ResultSet = connection.execute(female_pop).fetchall()
pd.DataFrame(ResultSet)
```


```python
total_pop = db.cast(db.func.sum(census.columns.pop2000), db.Float)
```


```python
query = db.select([female_pop/total_pop * 100])
ResultSet = connection.execute(query).fetchall()
pd.DataFrame(ResultSet)
```


```python
result = connection.execute(query).scalar()
print(result)
```

We use ```.scalar``` to the result when the result contains only single value

### joins

If you have two tables that already have an established relationship, you can automatically use that relationship by just adding the columns we want from each table to the select statement.

```python
select([census.columns.pop2008, state_fact.columns.abbreviation])
```


```python
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()

census = db.Table('census', metadata, autoload=True, autoload_with=engine)
state_fact = db.Table('state_fact', metadata, autoload=True, autoload_with=engine)
```


```python
# Automatic Join
query = db.select([census.columns.pop2008, state_fact.columns.abbreviation])
results = connection.execute(query).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(5)
```


```python
# Manual Join
query = db.select([census, state_fact])
query = query.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))
results = connection.execute(query).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(5)
```

## Creating and Inserting Data into Tables

By passing the database which is not present, to the engine then sqlalchemy automatically creates a new database.

### Creating Database and Table


```python
# delete the test database
import os
test_db_name = 'test.sqlite'

if os.path.exists(test_db_name): 
    os.remove(test_db_name)
```


```python
engine = db.create_engine(f'sqlite:///{test_db_name}') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

emp = db.Table('emp', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )

metadata.create_all(engine) #Creates the table
```

### Inserting Data


```python
#Inserting record one by one
query = db.insert(emp).values(Id=1, name='naveen', salary=60000.00, active=True) 
ResultProxy = connection.execute(query)
```


```python
#Inserting many records at ones
query = db.insert(emp) 
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query, values_list)
```


```python
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
```

### Updating data in Databases

```python
db.update(table_name).values(attribute = new_value).where(condition)
```


```python
engine = db.create_engine(f'sqlite:///{test_db_name}')
metadata = db.MetaData()
connection = engine.connect()
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)
```


```python
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
```


```python
# Build a statement to update the salary to 100000
query = db.update(emp).values(salary = 100000)
query = query.where(emp.columns.Id == 1)
results = connection.execute(query)
```


```python
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
```

### Delete Table

```python
db.delete(table_name).where(condition)
```


```python
engine = db.create_engine(f'sqlite:///{test_db_name}')
metadata = db.MetaData()
connection = engine.connect()
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)
```


```python
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
```


```python
# Build a statement to delete where salary < 100000
query = db.delete(emp)
query = query.where(emp.columns.salary < 100000)
results = connection.execute(query)
```


```python
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
```

### Dropping a Table

```python
table_name.drop(engine) #drops a single table

metadata.drop_all(engine) #drops all the tables in the database
```


```python
engine = db.create_engine(f'sqlite:///{test_db_name}')
metadata = db.MetaData()
connection = engine.connect()
```


```python
# drop a table
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)
emp.drop(engine)
```


```python
# drop all tables
metadata.drop_all(engine)
```
