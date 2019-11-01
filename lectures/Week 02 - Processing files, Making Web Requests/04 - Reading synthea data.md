---
layout: default
title: 04 - Reading synthea data
parent: Week 02 - Processing files, Making Web Requests
grand_parent: Lectures
nav_order: 8
---

## Loading Synthea Data

Here we'll walk through the different data files from the [synthea](https://github.com/synthetichealth/synthea) data generator. Synthea can generate data in a number of formats including:
* CCDA
* CSV
* FHIR
* Text

## Reading Text Data


```python
with open('../data/text/Abraham100_Klein929_8ff56a9d-b91c-48c7-a6e9-a55344881a36.txt') as f:
    for idx, line in enumerate(f.readlines()):
        print(f'{idx}: {line}')
        if idx >= 5:
            break
```

    0: Abraham100 Klein929
    
    1: ===================
    
    2: Race:                White
    
    3: Ethnicity:           Non-Hispanic
    
    4: Gender:              M
    
    5: Age:                 61
    



```python
# find all lines 
```

## Reading CSV Data


```python
with open('../data/csv/providers.csv') as f:
    for line in f.readlines():
        print(line)
```

    Id,ORGANIZATION,NAME,GENDER,SPECIALITY,ADDRESS,CITY,STATE,ZIP,UTILIZATION
    
    5e5cf78f-134d-4f06-aee9-215efc211fbe,ef6ab57c-ed94-3dbe-9861-812d515918b3,Stanford577 Leannon79,M,GENERAL PRACTICE,88 LEWIS BAY ROAD,HYANNIS,MA,02601,116
    
    a6c2bcfc-c882-43f4-a1b8-b88ff5f2cd7f,5d4b9df1-93ae-3bc9-b680-03249990e558,Keeley419 Yundt842,F,GENERAL PRACTICE,575 BEECH STREET,HOLYOKE,MA,01040,278
    
    63b03bb2-a8a6-4a09-93dc-8d0a877ad89b,5844ad77-f653-3c2b-b7dd-e97576ab3b03,Avery919 Muller251,M,GENERAL PRACTICE,40 WRIGHT STREET,PALMER,MA,01069,287
    
    b13e5b69-0a18-47f4-959e-1e204a862ab1,f71ce1a9-cca7-3295-9a1e-c88ac3479b6f,Giovanni385 Greenfelder433,M,GENERAL PRACTICE,157 UNION STREET,MARLBOROUGH,MA,01752,329
    
    7b93076a-50de-43f1-8360-8c207bb4a2e0,c44f361c-2efb-3050-8f97-0354a12e2920,Barry322 Nicolas769,M,GENERAL PRACTICE,680 CENTER STREET,BROCKTON,MA,02302,181
    
    722adc42-3681-42e5-a0d3-931bca95a5d0,b0e04623-b02c-3f8b-92ea-943fc4db60da,Ignacio928 Towne435,M,GENERAL PRACTICE,295 VARNUM AVENUE,LOWELL,MA,01854,156
    
    4e76303c-3f26-43c2-8cc4-30f23c4f9e98,d692e283-0833-3201-8e55-4f868a9c0736,Lane844 Jacobi462,M,GENERAL PRACTICE,585 LEBANON STREET,MELROSE,MA,02176,345
    
    2b02c8fb-298f-4e25-8815-7a9f6c343406,226098a2-6a40-3588-b5bb-db56c3a30a04,Cedrick207 Runte676,M,GENERAL PRACTICE,235 NORTH PEARL STREET,BROCKTON,MA,02301,9
    
    8e049b4a-d4f6-447d-8c34-05804a9472d4,f99c74cc-7d1a-3f95-9a33-4a9357bf2f2a,Elroy493 Brakus656,M,GENERAL PRACTICE,55 LAKE AVENUE NORTH,WORCESTER,MA,01655,216
    
    62908080-e6e8-42de-a1c0-994b966b669a,6f122869-a856-3d65-8db9-099bf4f5bbb8,June482 Kassulke119,F,GENERAL PRACTICE,41 & 45 MALL ROAD,BURLINGTON,MA,01803,392
    
    91dffdf1-693f-4516-8344-796b4705f147,1eaf97fa-9de6-38de-a9c4-6efe5dc574be,Quentin28 Beahan375,M,GENERAL PRACTICE,123 SUMMER STREET,WORCESTER,MA,01608,1
    
    5b3bec55-b8f3-4959-82a3-4b420525a6d0,0d1563c1-d56c-362e-9e3d-d74463ebbe0f,Hannah56 Pfannerstill264,F,GENERAL PRACTICE,629 PLEASANT STREET,BROCKTON,MA,2301,1
    
    6a0b8ac3-412c-4188-bb42-27d537f467ae,ff9474cb-cf9c-350a-a22b-b949ee9793cf,Brendon298 Hartmann983,M,GENERAL PRACTICE,1515 ALLEN STREET,SPRINGFIELD,MA,1118,2
    
    a66fdf87-0b25-4ce7-afff-60eb9305c107,a43fb751-96fe-3496-8750-73f85651866d,Albertine688 Orn563,F,GENERAL PRACTICE,66B CONCORD STREET,WILMINGTON,MA,1887,1
    
    4cb01351-89c3-4a99-a7f7-8cc76e5fad0d,d672f853-e2a5-324e-98fa-c6d5f8dfc255,Merle11 Powlowski563,M,GENERAL PRACTICE,9 HOPE AVENUE,WALTHAM,MA,2453,2
    
    46554e2c-a660-4258-a978-a6be9cf9ccc1,a9afd4c9-8443-3b5a-a486-07c3bb109b3f,Zack583 Herzog843,M,GENERAL PRACTICE,444 MONTGOMERY STREET,CHICOPEE,MA,1020,2
    


## Reading XML Data


```python
with open('../data/ccda/Abraham100_Klein929_8ff56a9d-b91c-48c7-a6e9-a55344881a36.xml') as f:
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
with open('../data/fhir/Abraham100_Klein929_8ff56a9d-b91c-48c7-a6e9-a55344881a36.json') as f:
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
    
    5:       "fullUrl": "urn:uuid:07b3c863-ea51-45a7-b446-493b39eb72e2",
    



```python

```
