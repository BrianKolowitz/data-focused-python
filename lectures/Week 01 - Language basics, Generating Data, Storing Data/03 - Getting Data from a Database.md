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
engine = db.create_engine('sqlite:///census.db')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)
```


```python
# Print the column names
print(census.columns.keys())
```

    ['state', 'sex', 'age', 'pop2000', 'pop2008']



```python
# Print full table metadata
print(repr(metadata.tables['census']))
```

    Table('census', MetaData(), Column('state', VARCHAR(length=30), table=<census>), Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)


## Querying

```Table``` and ```MetaData``` have already been imported. The metadata is available as ```metadata```.


```python
import sqlalchemy as db
```


```python
engine = db.create_engine('sqlite:///census.db')
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




    [('Illinois', 'M', 0, 89600, 95012),
     ('Illinois', 'M', 1, 88445, 91829),
     ('Illinois', 'M', 2, 88729, 89547)]



### Dealing with Large ResultSet

We use ```.fetchmany()``` to load optimal no of rows and overcome memory issues in case of large datasets.


```python
ResultProxy = connection.execute(query)
# ResultSet = ResultProxy.fetchall()
num_to_fetch = 3
partial_results = ResultProxy.fetchmany(num_to_fetch)
for i in range(num_to_fetch):
    print(partial_results[i])
ResultProxy.close()
```

    ('Illinois', 'M', 0, 89600, 95012)
    ('Illinois', 'M', 1, 88445, 91829)
    ('Illinois', 'M', 2, 88729, 89547)


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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state</th>
      <th>sex</th>
      <th>age</th>
      <th>pop2000</th>
      <th>pop2008</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Illinois</td>
      <td>M</td>
      <td>0</td>
      <td>89600</td>
      <td>95012</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Illinois</td>
      <td>M</td>
      <td>1</td>
      <td>88445</td>
      <td>91829</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Illinois</td>
      <td>M</td>
      <td>2</td>
      <td>88729</td>
      <td>89547</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Illinois</td>
      <td>M</td>
      <td>3</td>
      <td>88868</td>
      <td>90037</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Illinois</td>
      <td>M</td>
      <td>4</td>
      <td>91947</td>
      <td>91111</td>
    </tr>
  </tbody>
</table>
</div>



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
sql = db.select([census]).where(census.columns.sex == 'F')
print(sql)
```

    SELECT census.state, census.sex, census.age, census.pop2000, census.pop2008 
    FROM census 
    WHERE census.sex = :sex_1


### in

**SQL**
```SQL
SELECT state, sex
FROM census
WHERE state IN (Texas, New York)
```


```python
# SQLAlchemy
sql = db.select([census.columns.state, census.columns.sex]) \
    .where(census.columns.state.in_(['Texas', 'New York']))
print(sql)
```

    SELECT census.state, census.sex 
    FROM census 
    WHERE census.state IN ([POSTCOMPILE_state_1])


### and, or, not

**SQL**
```SQL
SELECT * FROM census
WHERE state = 'California' AND NOT sex = 'M'
```


```python
# SQLAlchemy
sql = db.select([census]) \
    .where(db.and_(census.columns.state == 'California', 
                   census.columns.sex != 'M'))
print(sql)
```

    SELECT census.state, census.sex, census.age, census.pop2000, census.pop2008 
    FROM census 
    WHERE census.state = :state_1 AND census.sex != :sex_1


### order by

**SQL**
```SQL
SELECT * FROM census
ORDER BY State DESC, pop2000
```


```python
# SQLAlchemy
sql = db.select([census]).order_by(
        db.desc(census.columns.state), 
        census.columns.pop2000)
print(sql)
```

    SELECT census.state, census.sex, census.age, census.pop2000, census.pop2008 
    FROM census ORDER BY census.state DESC, census.pop2000


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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>302876613</td>
    </tr>
  </tbody>
</table>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>153959198</td>
      <td>F</td>
    </tr>
    <tr>
      <th>1</th>
      <td>148917415</td>
      <td>M</td>
    </tr>
  </tbody>
</table>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Illinois</td>
    </tr>
    <tr>
      <th>1</th>
      <td>New Jersey</td>
    </tr>
    <tr>
      <th>2</th>
      <td>District of Columbia</td>
    </tr>
    <tr>
      <th>3</th>
      <td>North Dakota</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Florida</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Maryland</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Idaho</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Massachusetts</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Oregon</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Nevada</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Michigan</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Wisconsin</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Missouri</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Washington</td>
    </tr>
    <tr>
      <th>14</th>
      <td>North Carolina</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Arizona</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Arkansas</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Colorado</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Indiana</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Pennsylvania</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Hawaii</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Kansas</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Louisiana</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Alabama</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Minnesota</td>
    </tr>
    <tr>
      <th>25</th>
      <td>South Dakota</td>
    </tr>
    <tr>
      <th>26</th>
      <td>New York</td>
    </tr>
    <tr>
      <th>27</th>
      <td>California</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Connecticut</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Ohio</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Rhode Island</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Georgia</td>
    </tr>
    <tr>
      <th>32</th>
      <td>South Carolina</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Alaska</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Delaware</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Tennessee</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Vermont</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Montana</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Kentucky</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Utah</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Nebraska</td>
    </tr>
    <tr>
      <th>41</th>
      <td>West Virginia</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Iowa</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Wyoming</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Maine</td>
    </tr>
    <tr>
      <th>45</th>
      <td>New Hampshire</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Mississippi</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Oklahoma</td>
    </tr>
    <tr>
      <th>48</th>
      <td>New Mexico</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Virginia</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Texas</td>
    </tr>
  </tbody>
</table>
</div>



### case & cast

The ```case()``` expression accepts a list of conditions to match and the column to return if the condition matches, followed by an ```else_``` if none of the conditions match.

```cast()``` function to convert an expression to a particular type


```python
engine = db.create_engine('sqlite:///census.db')
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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>143534804</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_pop = db.cast(db.func.sum(census.columns.pop2000), db.Float)
```


```python
query = db.select([female_pop/total_pop * 100])
ResultSet = connection.execute(query).fetchall()
pd.DataFrame(ResultSet)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>51.094674</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = connection.execute(query).scalar()
print(result)
```

    51.09467432293413


We use ```.scalar``` to the result when the result contains only single value

### joins

If you have two tables that already have an established relationship, you can automatically use that relationship by just adding the columns we want from each table to the select statement.

```python
select([census.columns.pop2008, state_fact.columns.abbreviation])
```


```python
engine = db.create_engine('sqlite:///census.db')
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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pop2008</th>
      <th>abbreviation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>95012</td>
      <td>IL</td>
    </tr>
    <tr>
      <th>1</th>
      <td>95012</td>
      <td>NJ</td>
    </tr>
    <tr>
      <th>2</th>
      <td>95012</td>
      <td>ND</td>
    </tr>
    <tr>
      <th>3</th>
      <td>95012</td>
      <td>OR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>95012</td>
      <td>DC</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Manual Join
query = db.select([census.columns.pop2008, state_fact.columns.abbreviation]).join(state_fact, census.columns.state == state_fact.columns.name)
print(query)
results = connection.execute(query).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(5)
```

    SELECT census.pop2008, state_fact.abbreviation 
    FROM census JOIN state_fact ON census.state = state_fact.name





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pop2008</th>
      <th>abbreviation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>95012</td>
      <td>IL</td>
    </tr>
    <tr>
      <th>1</th>
      <td>91829</td>
      <td>IL</td>
    </tr>
    <tr>
      <th>2</th>
      <td>89547</td>
      <td>IL</td>
    </tr>
    <tr>
      <th>3</th>
      <td>90037</td>
      <td>IL</td>
    </tr>
    <tr>
      <th>4</th>
      <td>91111</td>
      <td>IL</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Manual Join
query = db.select([census, state_fact])
query = query.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))
results = connection.execute(query).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state</th>
      <th>sex</th>
      <th>age</th>
      <th>pop2000</th>
      <th>pop2008</th>
      <th>id</th>
      <th>name</th>
      <th>abbreviation</th>
      <th>country</th>
      <th>type</th>
      <th>...</th>
      <th>occupied</th>
      <th>notes</th>
      <th>fips_state</th>
      <th>assoc_press</th>
      <th>standard_federal_region</th>
      <th>census_region</th>
      <th>census_region_name</th>
      <th>census_division</th>
      <th>census_division_name</th>
      <th>circuit_court</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Illinois</td>
      <td>M</td>
      <td>0</td>
      <td>89600</td>
      <td>95012</td>
      <td>13</td>
      <td>Illinois</td>
      <td>IL</td>
      <td>USA</td>
      <td>state</td>
      <td>...</td>
      <td>occupied</td>
      <td></td>
      <td>17</td>
      <td>Ill.</td>
      <td>V</td>
      <td>2</td>
      <td>Midwest</td>
      <td>3</td>
      <td>East North Central</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Illinois</td>
      <td>M</td>
      <td>1</td>
      <td>88445</td>
      <td>91829</td>
      <td>13</td>
      <td>Illinois</td>
      <td>IL</td>
      <td>USA</td>
      <td>state</td>
      <td>...</td>
      <td>occupied</td>
      <td></td>
      <td>17</td>
      <td>Ill.</td>
      <td>V</td>
      <td>2</td>
      <td>Midwest</td>
      <td>3</td>
      <td>East North Central</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Illinois</td>
      <td>M</td>
      <td>2</td>
      <td>88729</td>
      <td>89547</td>
      <td>13</td>
      <td>Illinois</td>
      <td>IL</td>
      <td>USA</td>
      <td>state</td>
      <td>...</td>
      <td>occupied</td>
      <td></td>
      <td>17</td>
      <td>Ill.</td>
      <td>V</td>
      <td>2</td>
      <td>Midwest</td>
      <td>3</td>
      <td>East North Central</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Illinois</td>
      <td>M</td>
      <td>3</td>
      <td>88868</td>
      <td>90037</td>
      <td>13</td>
      <td>Illinois</td>
      <td>IL</td>
      <td>USA</td>
      <td>state</td>
      <td>...</td>
      <td>occupied</td>
      <td></td>
      <td>17</td>
      <td>Ill.</td>
      <td>V</td>
      <td>2</td>
      <td>Midwest</td>
      <td>3</td>
      <td>East North Central</td>
      <td>7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Illinois</td>
      <td>M</td>
      <td>4</td>
      <td>91947</td>
      <td>91111</td>
      <td>13</td>
      <td>Illinois</td>
      <td>IL</td>
      <td>USA</td>
      <td>state</td>
      <td>...</td>
      <td>occupied</td>
      <td></td>
      <td>17</td>
      <td>Ill.</td>
      <td>V</td>
      <td>2</td>
      <td>Midwest</td>
      <td>3</td>
      <td>East North Central</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



## Creating and Inserting Data into Tables

By passing the database which is not present, to the engine then sqlalchemy automatically creates a new database.

### Creating Database and Table


```python
# delete the test database
import os
test_db_name = 'test.db'

if os.path.exists(test_db_name): 
    os.remove(test_db_name)
```


```python
engine = db.create_engine(f'sqlite:///{test_db_name}') #Create test.db automatically
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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>name</th>
      <th>salary</th>
      <th>active</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>naveen</td>
      <td>60000.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>ram</td>
      <td>80000.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ramesh</td>
      <td>70000.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>name</th>
      <th>salary</th>
      <th>active</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>naveen</td>
      <td>60000.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>ram</td>
      <td>80000.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ramesh</td>
      <td>70000.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>name</th>
      <th>salary</th>
      <th>active</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>naveen</td>
      <td>100000.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>ram</td>
      <td>80000.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ramesh</td>
      <td>70000.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>name</th>
      <th>salary</th>
      <th>active</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>naveen</td>
      <td>100000.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>ram</td>
      <td>80000.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ramesh</td>
      <td>70000.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>name</th>
      <th>salary</th>
      <th>active</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>naveen</td>
      <td>100000.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



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


```python

```
