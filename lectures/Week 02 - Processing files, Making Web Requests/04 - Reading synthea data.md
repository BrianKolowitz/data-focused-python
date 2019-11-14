---
layout: default
title: 04 - Reading Synthea data
parent: Week 02 - Processing files, Making Web Requests
grand_parent: Lectures
nav_order: 8
---

## Reading Synthea Data

Here we'll walk through the different data files from the [synthea](https://github.com/synthetichealth/synthea) data generator. Synthea can generate data in a number of formats including:
* CCDA
* CSV
* FHIR
* Text

## Reading Text Data


```python
with open('../data/text/Abe604_Veum823_e841a5e8-9ace-437b-be32-b37d006aef87.txt') as f:
    for idx, line in enumerate(f.readlines()):
        print(f'{idx}: {line}')
        if idx >= 5:
            break
```

    0: Abe604 Veum823
    
    1: ==============
    
    2: Race:                Asian
    
    3: Ethnicity:           Non-Hispanic
    
    4: Gender:              M
    
    5: Age:                 69
    



```python
# find all lines 
```

## Reading CSV Data


```python
with open('../data/csv/providers.csv') as f:
    for idx, line in enumerate(f.readlines()):
        print(line)
        if idx >= 5:
            break
        
```

    Id,ORGANIZATION,NAME,GENDER,SPECIALITY,ADDRESS,CITY,STATE,ZIP,UTILIZATION
    
    4f073dcc-c92a-455b-8b0c-be967da311b8,ef58ea08-d883-3957-8300-150554edc8fb,Noe500 Dibbert990,M,GENERAL PRACTICE,60 HOSPITAL ROAD,LEOMINSTER,MA,01453,362
    
    7066c8e7-c63a-4de5-a6ed-2fe78ba2d484,69176529-fd1f-3b3f-abce-a0a3626769eb,Mariam937 Gleason633,F,GENERAL PRACTICE,330 MOUNT AUBURN STREET,CAMBRIDGE,MA,02138,334
    
    2d6d2a74-e052-4546-8173-ac72a39b7365,5e765f2b-e908-3888-9fc7-df2cb87beb58,Dagny669 Schoen8,F,GENERAL PRACTICE,211 PARK STREET,ATTLEBORO,MA,02703,77
    
    66ab043d-06d1-4f21-b837-2d74448feea7,f1fbcbfb-fcfa-3bd2-b7f4-df20f1b3c3a4,Tyron580 Torphy630,M,GENERAL PRACTICE,ONE GENERAL STREET,LAWRENCE,MA,01842,359
    
    4e37e414-41b9-467f-be47-4293b6dea918,e002090d-4e92-300e-b41e-7d1f21dee4c6,Loren192 Fay398,M,GENERAL PRACTICE,1493 CAMBRIDGE STREET,CAMBRIDGE,MA,02138,7
    


## Reading XML Data


```python
with open('../data/ccda/Abe604_Veum823_e841a5e8-9ace-437b-be32-b37d006aef87.xml') as f:
    for idx, line in enumerate(f.readlines()):
        print(f'{idx}: {line}')
        if idx >= 5:
            break
```

    0: <?xml version="1.0" encoding="UTF-8"?>
    
    1: <ClinicalDocument xmlns="urn:hl7-org:v3" xmlns:sdtc="urn:hl7-org:sdtc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:hl7-org:v3 http://xreg2.nist.gov:8080/hitspValidation/schema/cdar2c32/infrastructure/cda/C32_CDA.xsd">
    
    2:   <realmCode code="US"/>
    
    3:   <typeId root="2.16.840.1.113883.1.3" extension="POCD_HD000040"/>
    
    4:   <templateId root="2.16.840.1.113883.10.20.22.1.1" extension="2015-08-01"/>
    
    5:   <templateId root="2.16.840.1.113883.10.20.22.1.2" extension="2015-08-01"/>
    


## Reading JSON Data


```python
with open('../data/fhir/Abe604_Veum823_e841a5e8-9ace-437b-be32-b37d006aef87.json') as f:
    for idx, line in enumerate(f.readlines()):
        print(f'{idx}: {line}')
        if idx >= 5:
            break
```

    0: {
    
    1:   "resourceType": "Bundle",
    
    2:   "type": "transaction",
    
    3:   "entry": [
    
    4:     {
    
    5:       "fullUrl": "urn:uuid:df5f01e0-810b-4379-be90-bf53a6b3563d",
    



```python

```
