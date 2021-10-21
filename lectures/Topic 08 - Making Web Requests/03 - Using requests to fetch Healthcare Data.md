---
layout: default
title: 03 - Using requests to fetch Healthcare Data
parent: Topic 08 - Making Web Requests
grand_parent: Lectures
nav_order: 1
---
## Using Requests


```python
import requests
import json
```


```python
response = requests.get("http://hapi.fhir.org/baseR4/Patient/2543713")
```


```python
response.status_code
```




    200




```python
data = json.loads(response.content.decode('utf-8'))
data['name']
```




    [{'use': 'official', 'family': 'Chalmers', 'given': ['Peter', 'James']}]




```python
data['name'][0]['family']
```




    'Chalmers'




```python
data['name'][0]['given']
```




    ['Peter', 'James']




```python
data['name'][0]['given'][0]
```




    'Peter'




```python
response.text
```




    '{\n  "resourceType": "Patient",\n  "id": "2543713",\n  "meta": {\n    "versionId": "1",\n    "lastUpdated": "2021-09-06T03:21:51.345+00:00",\n    "source": "#tE3DOhkavDLHnkhZ"\n  },\n  "text": {\n    "status": "generated",\n    "div": "<div xmlns=\\"http://www.w3.org/1999/xhtml\\">Some narrative</div>"\n  },\n  "active": true,\n  "name": [ {\n    "use": "official",\n    "family": "Chalmers",\n    "given": [ "Peter", "James" ]\n  } ],\n  "gender": "male",\n  "birthDate": "1974-12-25"\n}'




```python
response.json()
```




    {'resourceType': 'Patient',
     'id': '2543713',
     'meta': {'versionId': '1',
      'lastUpdated': '2021-09-06T03:21:51.345+00:00',
      'source': '#tE3DOhkavDLHnkhZ'},
     'text': {'status': 'generated',
      'div': '<div xmlns="http://www.w3.org/1999/xhtml">Some narrative</div>'},
     'active': True,
     'name': [{'use': 'official',
       'family': 'Chalmers',
       'given': ['Peter', 'James']}],
     'gender': 'male',
     'birthDate': '1974-12-25'}




```python

```
