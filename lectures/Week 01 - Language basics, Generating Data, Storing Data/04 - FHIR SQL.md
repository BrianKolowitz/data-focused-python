---
layout: default
title: 04 - FHIR SQL
parent: Week 01 - Language basics, Generating Data, Storing Data
grand_parent: Lectures
nav_order: 8
---


```python
import json
from dateutil.parser import parse
import pprint
```


```python
f = open('fhir/Candis134_Wolff180_caac926a-429a-422d-9333-c9a3a04e68f9.json', 'r')
text = f.read()
f.close()
print(type(text))
```


```python
with open('fhir/Candis134_Wolff180_caac926a-429a-422d-9333-c9a3a04e68f9.json') as f:
    bundle = json.load(f)
print(type(bundle))
```


```python
for entry in bundle['entry']:
    resource = entry['resource']
    resource_type = resource['resourceType']
    if resource_type == 'Claim':
        id = resource['id']
        patient = resource['patient']['reference']
        status = resource['status']
        total = resource['total']['value']
        currency = resource['total']['currency']
        start = resource['billablePeriod']['start']
        end = resource['billablePeriod']['end']
        print(patient, status, total, currency, start, end)
        break
```


```python
for entry in bundle['entry']:
    resource = entry['resource']
    resource_type = resource['resourceType']
    if resource_type == 'Claim':
        id = resource['id']
        patient = resource['patient']['reference']
        status = resource['status']
        total = resource['total']['value']
        currency = resource['total']['currency']
        start = parse(resource['billablePeriod']['start'])
        end = parse(resource['billablePeriod']['end'])
        print(patient, status, total, currency, start, end)
        break
```


```python
import sqlalchemy as db
```


```python
engine = db.create_engine('sqlite:///fhir.sqlite')
connection = engine.connect()
metadata = db.MetaData()
```


```python
claims = db.Table('claims', metadata,
                  db.Column('id', db.Integer()),
                  db.Column('patient', db.String(255)),
                  db.Column('status', db.String(255)),
                  db.Column('total', db.Float()),
                  db.Column('currency', db.String(255)),
                  db.Column('start', db.DateTime()),
                  db.Column('end', db.DateTime()))

metadata.create_all(engine) #Creates the table
```


```python
print(claims.columns.keys())
```


```python
for entry in bundle['entry']:
    resource = entry['resource']
    resource_type = resource['resourceType']
    if resource_type == 'Claim':
        id = resource['id']
        patient = resource['patient']['reference']
        status = resource['status']
        total = resource['total']['value']
        currency = resource['total']['currency']
        start = parse(resource['billablePeriod']['start'])
        end = parse(resource['billablePeriod']['end'])        
        query = db.insert(claims).values(id=id, 
                                         patient=patient,
                                         status=status,
                                         total=total,
                                         currency=currency,
                                         start=start,
                                         end=end)

        result_proxy = connection.execute(query)
```


```python
stmt = db.select([claims])
results = connection.execute(stmt).fetchall()
```


```python
import pandas as pd
```


```python
df = pd.DataFrame(results)
```


```python
df.columns = results[0].keys()
```


```python
df.head()
```


```python
stmt = db.select([claims])
results = connection.execute(stmt).fetchall()
pd.DataFrame(results).head()
df.columns = results[0].keys()
df.head()
```


```python
stmt = db.select([claims]).where(claims.columns.total >= 25000.0).order_by(db.desc(claims.columns.total))
results = connection.execute(stmt).fetchall()
df = pd.DataFrame(results).head()
df.columns = results[0].keys()
df.head()
```


```python
stmt = db.select([db.func.sum(claims.columns.total).label('total claims'),
                  db.func.avg(claims.columns.total).label('average claim')])
results = connection.execute(stmt).fetchall()
df = pd.DataFrame(results).head()
df.columns = results[0].keys()
df.head()
```


```python

```
