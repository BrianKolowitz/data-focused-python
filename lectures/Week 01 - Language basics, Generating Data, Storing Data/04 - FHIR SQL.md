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
f = open('../data/fhir/Abe604_Veum823_e841a5e8-9ace-437b-be32-b37d006aef87.json', 'r')
text = f.read()
f.close()
print(type(text))
```

    <class 'str'>



```python
with open('../data/fhir/Abe604_Veum823_e841a5e8-9ace-437b-be32-b37d006aef87.json') as f:
    bundle = json.load(f)
print(type(bundle))
```

    <class 'dict'>



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

    urn:uuid:df5f01e0-810b-4379-be90-bf53a6b3563d active 125.0 USD 1968-04-11T18:37:35-05:00 1968-04-11T18:52:35-05:00



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

    urn:uuid:df5f01e0-810b-4379-be90-bf53a6b3563d active 125.0 USD 1968-04-11 18:37:35-05:00 1968-04-11 18:52:35-05:00



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

    ['id', 'patient', 'status', 'total', 'currency', 'start', 'end']



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
      <th>id</th>
      <th>patient</th>
      <th>status</th>
      <th>total</th>
      <th>currency</th>
      <th>start</th>
      <th>end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b16bf2ad-9084-4764-b029-83aa5e40edaa</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>255.0</td>
      <td>USD</td>
      <td>1988-04-23 13:35:04</td>
      <td>1988-04-23 13:50:04</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b16bf2ad-9084-4764-b029-83aa5e40edaa</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>255.0</td>
      <td>USD</td>
      <td>1988-04-23 13:35:04</td>
      <td>1988-04-23 13:50:04</td>
    </tr>
    <tr>
      <th>2</th>
      <td>722b5412-303f-4c19-8065-b40c8c3cff26</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>125.0</td>
      <td>USD</td>
      <td>1988-04-23 13:35:04</td>
      <td>1988-04-23 13:50:04</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6305265e-1ffb-48af-bc29-404eafe9e426</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>125.0</td>
      <td>USD</td>
      <td>1991-08-03 13:35:04</td>
      <td>1991-08-03 13:50:04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e6f0f9cb-0655-4e3f-bbb3-b11fe034618a</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>125.0</td>
      <td>USD</td>
      <td>1997-08-09 13:35:04</td>
      <td>1997-08-09 14:50:04</td>
    </tr>
  </tbody>
</table>
</div>




```python
stmt = db.select([claims])
results = connection.execute(stmt).fetchall()
pd.DataFrame(results).head()
df.columns = results[0].keys()
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
      <th>id</th>
      <th>patient</th>
      <th>status</th>
      <th>total</th>
      <th>currency</th>
      <th>start</th>
      <th>end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b16bf2ad-9084-4764-b029-83aa5e40edaa</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>255.0</td>
      <td>USD</td>
      <td>1988-04-23 13:35:04</td>
      <td>1988-04-23 13:50:04</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b16bf2ad-9084-4764-b029-83aa5e40edaa</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>255.0</td>
      <td>USD</td>
      <td>1988-04-23 13:35:04</td>
      <td>1988-04-23 13:50:04</td>
    </tr>
    <tr>
      <th>2</th>
      <td>722b5412-303f-4c19-8065-b40c8c3cff26</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>125.0</td>
      <td>USD</td>
      <td>1988-04-23 13:35:04</td>
      <td>1988-04-23 13:50:04</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6305265e-1ffb-48af-bc29-404eafe9e426</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>125.0</td>
      <td>USD</td>
      <td>1991-08-03 13:35:04</td>
      <td>1991-08-03 13:50:04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e6f0f9cb-0655-4e3f-bbb3-b11fe034618a</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>125.0</td>
      <td>USD</td>
      <td>1997-08-09 13:35:04</td>
      <td>1997-08-09 14:50:04</td>
    </tr>
  </tbody>
</table>
</div>




```python
stmt = db.select([claims]).where(claims.columns.total >= 25000.0).order_by(db.desc(claims.columns.total))
results = connection.execute(stmt).fetchall()
df = pd.DataFrame(results).head()
df.columns = results[0].keys()
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
      <th>id</th>
      <th>patient</th>
      <th>status</th>
      <th>total</th>
      <th>currency</th>
      <th>start</th>
      <th>end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16f8da2a-322e-47ca-bc82-8b66843858f9</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>74670.12</td>
      <td>USD</td>
      <td>2015-12-26 12:35:04</td>
      <td>2015-12-26 17:50:04</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16f8da2a-322e-47ca-bc82-8b66843858f9</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>74670.12</td>
      <td>USD</td>
      <td>2015-12-26 12:35:04</td>
      <td>2015-12-26 17:50:04</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16f8da2a-322e-47ca-bc82-8b66843858f9</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>74670.12</td>
      <td>USD</td>
      <td>2015-12-26 12:35:04</td>
      <td>2015-12-26 17:50:04</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16f8da2a-322e-47ca-bc82-8b66843858f9</td>
      <td>urn:uuid:ab8f33ad-54b4-4ee0-acd7-a14918459c3d</td>
      <td>active</td>
      <td>74670.12</td>
      <td>USD</td>
      <td>2015-12-26 12:35:04</td>
      <td>2015-12-26 17:50:04</td>
    </tr>
  </tbody>
</table>
</div>




```python
stmt = db.select([db.func.sum(claims.columns.total).label('total claims'),
                  db.func.avg(claims.columns.total).label('average claim')])
results = connection.execute(stmt).fetchall()
df = pd.DataFrame(results).head()
df.columns = results[0].keys()
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
      <th>total claims</th>
      <th>average claim</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1476254.5</td>
      <td>3627.160934</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
