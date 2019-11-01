---
layout: default
title: 03 - Using fhirclient to parse data
parent: Week 02 - Processing files using functions, classes, and libraries
grand_parent: Lectures
nav_order: 7
---

# fhirclient 

**Note: this example uses FHIR DSTU3 whereas synthea now supports FHIR R4 so you'll need a different version of the fhirclient library to deal with each dataset**

The _fhirclient_, a flexible Python client for FHIR servers supporting the SMART on FHIR protocol.

_fhirclient_ versioning is not identical to FHIR versioning, see the full table for reference.

| Version | FHIR | |
| --- | --- | --- |
| **4.0.0** | `4.0.0` | (R4) |
| **3.0.0** | `3.0.0` | (STU-3) |
| **1.0.3** | `1.0.2` | (DSTU 2) |
| **1.0** | `1.0.1` | (DSTU 2) |

## Installation

```bash
pip install fhirclient
```

or
```bash
pip install git+https://github.com/smart-on-fhir/client-py.git
```

**NOTE: We'll use FHIR R4 here so you need to install from GitHub**

## Documentation

Technical documentation is available at [docs](https://docs.smarthealthit.org/client-py/).

## Client Use

To connect to a SMART on FHIR server (or any open FHIR server), you can use the `FHIRClient` class.
It will initialize and handle a `FHIRServer` instance, your actual handle to the FHIR server you'd like to access.

### Read Data from Server

To read a given patient from an open FHIR server, you can use:


```python
from pprint import pprint
from fhirclient import client

settings = {
'app_id': 'my_web_app',
'api_base': 'http://hapi.fhir.org/baseR4'
}

smart = client.FHIRClient(settings=settings)

import fhirclient.models.patient as p

patient = p.Patient.read('38', smart.server)
print(patient.birthDate.isostring)
print(smart.human_name(patient.name[0]))
```

    1980-01-01
    Luc Sky


If this is a protected server, you will first have to send your user to the authorize endpoint to log in.

1. Call `smart.authorize_url` to obtain the correct URL.
    2. You can use `smart.prepare()`, which will return `False` if the server is protected and you need to authorize.
    2. The `smart.ready` property has the same purpose, it will however not retrieve the server's _CapabilityStatement_ resource and hence is only useful as a quick check whether the server instance is ready.


```python
smart = client.FHIRClient(settings=settings)
smart.ready

# prints False
print(smart.prepare())

# prints True after fetching CapabilityStatement
print(smart.ready)

# prints True
print(smart.prepare())

# prints True immediately
print(smart.authorize_url)
```

    True
    True
    True
    None


You can work with the `FHIRServer` class directly, without using `FHIRClient`, but this is not recommended:


```python
import fhirclient.server

smart = fhirclient.server.FHIRServer(None, 'http://hapi.fhir.org/baseR4')

import fhirclient.models.patient as p

patient = p.Patient.read('38', smart)
patient.name[0].given
```




    ['Luc']



### Search Records on Server

You can also search for resources matching a particular set of criteria:


```python
smart = client.FHIRClient(settings=settings)

import fhirclient.models.observation as o

search = o.Observation.where(struct={'subject': 'Patient/38'})
observations = search.perform_resources(smart.server)
# print(observations)

for observation in observations:
    pprint(observation.as_json())
```

    {'code': {'coding': [{'code': 'CRE(1)',
                          'display': 'CREATININE',
                          'system': 'http://loinc.org'}]},
     'id': '52391',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:28:34.475+00:00',
              'source': '#SWMQuDDsY0r4Ndbn',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mg/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mg/l',
                                  'value': 8},
                         'low': {'code': 'mg/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mg/l',
                                 'value': 5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mg/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mg/l',
                       'value': 6}}
    {'code': {'coding': [{'code': 'K(1)',
                          'display': 'POTASSIUM',
                          'system': 'http://loinc.org'}]},
     'id': '52390',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:28:34.187+00:00',
              'source': '#ZkPXDmdj9WQhpcPC',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 5.5},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 3.5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 4.1}}
    {'code': {'coding': [{'code': 'NA(1)',
                          'display': 'SODIUM',
                          'system': 'http://loinc.org'}]},
     'id': '52389',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:28:33.889+00:00',
              'source': '#SoUHor0kX69jDHko',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 146},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 132}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 139}}
    {'code': {'coding': [{'code': 'N(1)',
                          'display': 'LEUCOCYTES',
                          'system': 'http://loinc.org'}]},
     'id': '52388',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:28:33.592+00:00',
              'source': '#fk9d4FaQW1DqbhDX',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'G/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'G/l',
                                  'value': 10},
                         'low': {'code': 'G/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'G/l',
                                 'value': 4}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'G/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'G/l',
                       'value': 5.65}}
    {'code': {'coding': [{'code': 'CRE(1)',
                          'display': 'CREATININE',
                          'system': 'http://loinc.org'}]},
     'id': '52386',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:21:42.928+00:00',
              'source': '#9id3EEsARrddLcYd',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mg/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mg/l',
                                  'value': 8},
                         'low': {'code': 'mg/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mg/l',
                                 'value': 5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mg/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mg/l',
                       'value': 6}}
    {'code': {'coding': [{'code': 'K(1)',
                          'display': 'POTASSIUM',
                          'system': 'http://loinc.org'}]},
     'id': '52385',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:21:42.620+00:00',
              'source': '#bJudecLm5RyJJFLr',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 5.5},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 3.5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 4.1}}
    {'code': {'coding': [{'code': 'NA(1)',
                          'display': 'SODIUM',
                          'system': 'http://loinc.org'}]},
     'id': '52384',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:21:42.312+00:00',
              'source': '#1MsZwjff0Cn9GO1K',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 146},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 132}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 139}}
    {'code': {'coding': [{'code': 'N(1)',
                          'display': 'LEUCOCYTES',
                          'system': 'http://loinc.org'}]},
     'id': '52383',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:21:42.017+00:00',
              'source': '#AOVr9w5iXmgJm5o2',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'G/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'G/l',
                                  'value': 10},
                         'low': {'code': 'G/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'G/l',
                                 'value': 4}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'G/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'G/l',
                       'value': 5.65}}
    {'code': {'coding': [{'code': 'CRE(1)',
                          'display': 'CREATININE',
                          'system': 'http://loinc.org'}]},
     'id': '52381',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:17:01.440+00:00',
              'source': '#9rQCaKBqqCktrFWx',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mg/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mg/l',
                                  'value': 8},
                         'low': {'code': 'mg/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mg/l',
                                 'value': 5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mg/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mg/l',
                       'value': 6}}
    {'code': {'coding': [{'code': 'K(1)',
                          'display': 'POTASSIUM',
                          'system': 'http://loinc.org'}]},
     'id': '52380',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:17:01.128+00:00',
              'source': '#cRfk4V7g0yhVZ0pe',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 5.5},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 3.5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 4.1}}
    {'code': {'coding': [{'code': 'NA(1)',
                          'display': 'SODIUM',
                          'system': 'http://loinc.org'}]},
     'id': '52379',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:17:00.815+00:00',
              'source': '#R9fOeuj088bnsod9',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 146},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 132}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 139}}
    {'code': {'coding': [{'code': 'N(1)',
                          'display': 'LEUCOCYTES',
                          'system': 'http://loinc.org'}]},
     'id': '52378',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-30T14:17:00.419+00:00',
              'source': '#UWnHDbhZAXLD0qEI',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/1141'}],
     'referenceRange': [{'high': {'code': 'G/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'G/l',
                                  'value': 10},
                         'low': {'code': 'G/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'G/l',
                                 'value': 4}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'G/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'G/l',
                       'value': 5.65}}
    {'code': {'coding': [{'code': 'K(1)',
                          'display': 'POTASSIUM',
                          'system': 'http://loinc.org'}]},
     'id': '51286',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-27T14:31:19.040+00:00',
              'source': '#N4NvLWK09cvWPw7a',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 5.5},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 3.5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 4.1}}
    {'code': {'coding': [{'code': 'NA(1)',
                          'display': 'SODIUM',
                          'system': 'http://loinc.org'}]},
     'id': '51285',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-27T14:31:18.727+00:00',
              'source': '#oCkviKNqchwDSfP5',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 146},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 132}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 139}}
    {'code': {'coding': [{'code': 'N(1)',
                          'display': 'LEUCOCYTES',
                          'system': 'http://loinc.org'}]},
     'id': '51284',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-27T14:31:18.398+00:00',
              'source': '#HNragNqo20ohjwIp',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
     'referenceRange': [{'high': {'code': 'G/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'G/l',
                                  'value': 10},
                         'low': {'code': 'G/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'G/l',
                                 'value': 4}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'G/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'G/l',
                       'value': 5.65}}
    {'code': {'coding': [{'code': 'CRE(1)',
                          'display': 'CREATININE',
                          'system': 'http://loinc.org'}]},
     'id': '51283',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-27T13:59:28.090+00:00',
              'source': '#Ga4BkHLzxi7Yykz6',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
     'referenceRange': [{'high': {'code': 'mg/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mg/l',
                                  'value': 8},
                         'low': {'code': 'mg/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mg/l',
                                 'value': 5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mg/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mg/l',
                       'value': 6}}
    {'code': {'coding': [{'code': 'K(1)',
                          'display': 'POTASSIUM',
                          'system': 'http://loinc.org'}]},
     'id': '51282',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-27T13:59:27.771+00:00',
              'source': '#qxl66ph5Ty5RJn4Q',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 5.5},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 3.5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 4.1}}
    {'code': {'coding': [{'code': 'NA(1)',
                          'display': 'SODIUM',
                          'system': 'http://loinc.org'}]},
     'id': '51281',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-27T13:59:27.463+00:00',
              'source': '#jZ9LFx51pXWzMIC9',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
     'referenceRange': [{'high': {'code': 'mEq/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mEq/l',
                                  'value': 146},
                         'low': {'code': 'mEq/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mEq/l',
                                 'value': 132}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mEq/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mEq/l',
                       'value': 139}}
    {'code': {'coding': [{'code': 'N(1)',
                          'display': 'LEUCOCYTES',
                          'system': 'http://loinc.org'}]},
     'id': '51280',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-27T13:59:27.122+00:00',
              'source': '#doSGbTbIhYfSrE4d',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
     'referenceRange': [{'high': {'code': 'G/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'G/l',
                                  'value': 10},
                         'low': {'code': 'G/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'G/l',
                                 'value': 4}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'G/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'G/l',
                       'value': 5.65}}
    {'code': {'coding': [{'code': 'CRE(1)',
                          'display': 'CREATININE',
                          'system': 'http://loinc.org'}]},
     'id': '51279',
     'interpretation': [{'coding': [{'code': 'N',
                                     'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
     'issued': '2019-10-14',
     'meta': {'lastUpdated': '2019-10-27T13:57:12.698+00:00',
              'source': '#EErteiOsAusb5QXn',
              'versionId': '1'},
     'performer': [{'display': 'LESTEST    ECLANCHER',
                    'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
     'referenceRange': [{'high': {'code': 'mg/l',
                                  'system': 'http://unitsofmeasure.org',
                                  'unit': 'mg/l',
                                  'value': 8},
                         'low': {'code': 'mg/l',
                                 'system': 'http://unitsofmeasure.org',
                                 'unit': 'mg/l',
                                 'value': 5}}],
     'resourceType': 'Observation',
     'status': 'final',
     'subject': {'display': 'Sky Luc', 'reference': 'Patient/38'},
     'valueQuantity': {'code': 'mg/l',
                       'system': 'http://unitsofmeasure.org',
                       'unit': 'mg/l',
                       'value': 6}}



```python
# to get the raw Bundle instead of resources only, you can use:
bundle = search.perform(smart.server)
pprint(bundle.as_json())
```

    {'entry': [{'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52391',
                'resource': {'code': {'coding': [{'code': 'CRE(1)',
                                                  'display': 'CREATININE',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52391',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:28:34.475+00:00',
                                      'source': '#SWMQuDDsY0r4Ndbn',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mg/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mg/l',
                                                          'value': 8},
                                                 'low': {'code': 'mg/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mg/l',
                                                         'value': 5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mg/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mg/l',
                                               'value': 6}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52390',
                'resource': {'code': {'coding': [{'code': 'K(1)',
                                                  'display': 'POTASSIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52390',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:28:34.187+00:00',
                                      'source': '#ZkPXDmdj9WQhpcPC',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 5.5},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 3.5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 4.1}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52389',
                'resource': {'code': {'coding': [{'code': 'NA(1)',
                                                  'display': 'SODIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52389',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:28:33.889+00:00',
                                      'source': '#SoUHor0kX69jDHko',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 146},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 132}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 139}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52388',
                'resource': {'code': {'coding': [{'code': 'N(1)',
                                                  'display': 'LEUCOCYTES',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52388',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:28:33.592+00:00',
                                      'source': '#fk9d4FaQW1DqbhDX',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'G/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'G/l',
                                                          'value': 10},
                                                 'low': {'code': 'G/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'G/l',
                                                         'value': 4}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'G/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'G/l',
                                               'value': 5.65}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52386',
                'resource': {'code': {'coding': [{'code': 'CRE(1)',
                                                  'display': 'CREATININE',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52386',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:21:42.928+00:00',
                                      'source': '#9id3EEsARrddLcYd',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mg/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mg/l',
                                                          'value': 8},
                                                 'low': {'code': 'mg/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mg/l',
                                                         'value': 5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mg/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mg/l',
                                               'value': 6}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52385',
                'resource': {'code': {'coding': [{'code': 'K(1)',
                                                  'display': 'POTASSIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52385',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:21:42.620+00:00',
                                      'source': '#bJudecLm5RyJJFLr',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 5.5},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 3.5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 4.1}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52384',
                'resource': {'code': {'coding': [{'code': 'NA(1)',
                                                  'display': 'SODIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52384',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:21:42.312+00:00',
                                      'source': '#1MsZwjff0Cn9GO1K',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 146},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 132}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 139}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52383',
                'resource': {'code': {'coding': [{'code': 'N(1)',
                                                  'display': 'LEUCOCYTES',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52383',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:21:42.017+00:00',
                                      'source': '#AOVr9w5iXmgJm5o2',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'G/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'G/l',
                                                          'value': 10},
                                                 'low': {'code': 'G/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'G/l',
                                                         'value': 4}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'G/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'G/l',
                                               'value': 5.65}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52381',
                'resource': {'code': {'coding': [{'code': 'CRE(1)',
                                                  'display': 'CREATININE',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52381',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:17:01.440+00:00',
                                      'source': '#9rQCaKBqqCktrFWx',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mg/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mg/l',
                                                          'value': 8},
                                                 'low': {'code': 'mg/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mg/l',
                                                         'value': 5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mg/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mg/l',
                                               'value': 6}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52380',
                'resource': {'code': {'coding': [{'code': 'K(1)',
                                                  'display': 'POTASSIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52380',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:17:01.128+00:00',
                                      'source': '#cRfk4V7g0yhVZ0pe',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 5.5},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 3.5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 4.1}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52379',
                'resource': {'code': {'coding': [{'code': 'NA(1)',
                                                  'display': 'SODIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52379',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:17:00.815+00:00',
                                      'source': '#R9fOeuj088bnsod9',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 146},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 132}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 139}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/52378',
                'resource': {'code': {'coding': [{'code': 'N(1)',
                                                  'display': 'LEUCOCYTES',
                                                  'system': 'http://loinc.org'}]},
                             'id': '52378',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-30T14:17:00.419+00:00',
                                      'source': '#UWnHDbhZAXLD0qEI',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/1141'}],
                             'referenceRange': [{'high': {'code': 'G/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'G/l',
                                                          'value': 10},
                                                 'low': {'code': 'G/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'G/l',
                                                         'value': 4}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'G/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'G/l',
                                               'value': 5.65}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/51286',
                'resource': {'code': {'coding': [{'code': 'K(1)',
                                                  'display': 'POTASSIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '51286',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-27T14:31:19.040+00:00',
                                      'source': '#N4NvLWK09cvWPw7a',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 5.5},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 3.5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 4.1}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/51285',
                'resource': {'code': {'coding': [{'code': 'NA(1)',
                                                  'display': 'SODIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '51285',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-27T14:31:18.727+00:00',
                                      'source': '#oCkviKNqchwDSfP5',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 146},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 132}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 139}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/51284',
                'resource': {'code': {'coding': [{'code': 'N(1)',
                                                  'display': 'LEUCOCYTES',
                                                  'system': 'http://loinc.org'}]},
                             'id': '51284',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-27T14:31:18.398+00:00',
                                      'source': '#HNragNqo20ohjwIp',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
                             'referenceRange': [{'high': {'code': 'G/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'G/l',
                                                          'value': 10},
                                                 'low': {'code': 'G/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'G/l',
                                                         'value': 4}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'G/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'G/l',
                                               'value': 5.65}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/51283',
                'resource': {'code': {'coding': [{'code': 'CRE(1)',
                                                  'display': 'CREATININE',
                                                  'system': 'http://loinc.org'}]},
                             'id': '51283',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-27T13:59:28.090+00:00',
                                      'source': '#Ga4BkHLzxi7Yykz6',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
                             'referenceRange': [{'high': {'code': 'mg/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mg/l',
                                                          'value': 8},
                                                 'low': {'code': 'mg/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mg/l',
                                                         'value': 5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mg/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mg/l',
                                               'value': 6}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/51282',
                'resource': {'code': {'coding': [{'code': 'K(1)',
                                                  'display': 'POTASSIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '51282',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-27T13:59:27.771+00:00',
                                      'source': '#qxl66ph5Ty5RJn4Q',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 5.5},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 3.5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 4.1}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/51281',
                'resource': {'code': {'coding': [{'code': 'NA(1)',
                                                  'display': 'SODIUM',
                                                  'system': 'http://loinc.org'}]},
                             'id': '51281',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-27T13:59:27.463+00:00',
                                      'source': '#jZ9LFx51pXWzMIC9',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
                             'referenceRange': [{'high': {'code': 'mEq/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mEq/l',
                                                          'value': 146},
                                                 'low': {'code': 'mEq/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mEq/l',
                                                         'value': 132}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mEq/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mEq/l',
                                               'value': 139}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/51280',
                'resource': {'code': {'coding': [{'code': 'N(1)',
                                                  'display': 'LEUCOCYTES',
                                                  'system': 'http://loinc.org'}]},
                             'id': '51280',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-27T13:59:27.122+00:00',
                                      'source': '#doSGbTbIhYfSrE4d',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
                             'referenceRange': [{'high': {'code': 'G/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'G/l',
                                                          'value': 10},
                                                 'low': {'code': 'G/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'G/l',
                                                         'value': 4}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'G/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'G/l',
                                               'value': 5.65}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Observation/51279',
                'resource': {'code': {'coding': [{'code': 'CRE(1)',
                                                  'display': 'CREATININE',
                                                  'system': 'http://loinc.org'}]},
                             'id': '51279',
                             'interpretation': [{'coding': [{'code': 'N',
                                                             'system': 'http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation'}]}],
                             'issued': '2019-10-14',
                             'meta': {'lastUpdated': '2019-10-27T13:57:12.698+00:00',
                                      'source': '#EErteiOsAusb5QXn',
                                      'versionId': '1'},
                             'performer': [{'display': 'LESTEST    ECLANCHER',
                                            'reference': 'Practitioner/clinFhirbqsp1zJ4G6NmckaQKAWDeLpKRF73'}],
                             'referenceRange': [{'high': {'code': 'mg/l',
                                                          'system': 'http://unitsofmeasure.org',
                                                          'unit': 'mg/l',
                                                          'value': 8},
                                                 'low': {'code': 'mg/l',
                                                         'system': 'http://unitsofmeasure.org',
                                                         'unit': 'mg/l',
                                                         'value': 5}}],
                             'resourceType': 'Observation',
                             'status': 'final',
                             'subject': {'display': 'Sky Luc',
                                         'reference': 'Patient/38'},
                             'valueQuantity': {'code': 'mg/l',
                                               'system': 'http://unitsofmeasure.org',
                                               'unit': 'mg/l',
                                               'value': 6}},
                'search': {'mode': 'match'}}],
     'id': '327cddc7-d99d-4219-b8f4-3dd782db66dd',
     'link': [{'relation': 'self',
               'url': 'http://hapi.fhir.org/baseR4/Observation?subject=Patient%2F38'},
              {'relation': 'next',
               'url': 'http://hapi.fhir.org/baseR4?_getpages=327cddc7-d99d-4219-b8f4-3dd782db66dd&_getpagesoffset=20&_count=20&_pretty=true&_bundletype=searchset'}],
     'meta': {'lastUpdated': '2019-11-01T00:01:34.662+00:00'},
     'resourceType': 'Bundle',
     'total': 204,
     'type': 'searchset'}


## Data Model Use

The client contains data model classes, built using ```fhir-parser```, that handle (de)serialization and allow to work with FHIR data in a Pythonic way.

### Initialize Data Model


```python
import fhirclient.models.patient
import fhirclient.models.humanname

data = {'id': 'patient-1'}
patient = fhirclient.models.patient.Patient(data)

print(patient.id)
```

    patient-1



```python
name = fhirclient.models.humanname.HumanName()
name.given = ['Peter']
name.family = 'Parker'

patient.name = [name]
pprint(patient.as_json())
```

    {'id': 'patient-1',
     'name': [{'family': 'Parker', 'given': ['Peter']}],
     'resourceType': 'Patient'}



```python
name.given = 'Peter'
patient.as_json() # throws FHIRValidationError: because we incorrectly set the name to a string
```


    ---------------------------------------------------------------------------

    FHIRValidationError                       Traceback (most recent call last)

    <ipython-input-19-814c163e63cc> in <module>
          1 name.given = 'Peter'
    ----> 2 patient.as_json() # throws FHIRValidationError: because we incorrectly set the name to a string
    

    ~/anaconda/envs/cmu3/lib/python3.6/site-packages/fhirclient/models/fhirabstractresource.py in as_json(self)
         40 
         41     def as_json(self):
    ---> 42         js = super(FHIRAbstractResource, self).as_json()
         43         js['resourceType'] = self.resource_type
         44         return js


    ~/anaconda/envs/cmu3/lib/python3.6/site-packages/fhirclient/models/fhirabstractbase.py in as_json(self)
        295 
        296         if len(errs) > 0:
    --> 297             raise FHIRValidationError(errs)
        298         return js
        299 


    FHIRValidationError: {root}:
      name.0:
        given:
          Expecting property "given" on <class 'fhirclient.models.humanname.HumanName'> to be list, but is <class 'str'>


### Initialize from JSON file


```python
import json
import fhirclient.models.patient

with open('patient.json', 'r') as h:
    pjs = json.load(h)
    patient = fhirclient.models.patient.Patient(pjs)
    print(patient.name[0].family)
    print(patient.name[0].given[0])
    print(patient.gender)
    print(patient.birthDate.isostring)
```

    Sky
    Luc
    male
    1980-01-01


## Using Requests only


```python
import requests
```


```python
response = requests.get("http://hapi.fhir.org/baseR4/Patient/38")
```


```python
response.status_code
```




    200




```python
data = json.loads(response.content.decode('utf-8'))
data['name']
```




    [{'family': 'Sky', 'given': ['Luc']}]




```python
data['name'][0]['family']
```




    'Sky'




```python
data['name'][0]['given']
```




    ['Luc']




```python
data['name'][0]['given'][0]
```




    'Luc'




```python
response.text
```




    '{\n  "resourceType": "Patient",\n  "id": "38",\n  "meta": {\n    "versionId": "32",\n    "lastUpdated": "2019-10-30T14:16:54.484+00:00",\n    "source": "#e0mm6ofqyX94cLL9"\n  },\n  "text": {\n    "status": "generated",\n    "div": "<div xmlns=\\"http://www.w3.org/1999/xhtml\\"> <div class=\\"hapiHeaderText\\">Hi <b>HELLO </b> </div> <table class=\\"hapiPropertyTable\\"> <tbody> <tr> <td>Identifier</td> <td>NCC-7676</td> </tr> <tr> <td>Address</td> <td> <span>Nowhere 42 </span> <br/> <span>Spöck </span> <span>Germany </span> </td> </tr> <tr> <td>Date of birth</td> <td> <span>24 October 1990</span> </td> </tr> </tbody> </table> </div>"\n  },\n  "identifier": [\n    {\n      "use": "usual",\n      "type": {\n        "coding": [\n          {\n            "system": "http://interopsante.org/fhir/valueset/fr-patient-identifier-type",\n            "version": "1.0",\n            "code": "INS-NIR",\n            "display": "NIR définitif"\n          }\n        ]\n      },\n      "system": "urn:oid:1.2.250.1.213.1.4.10",\n      "value": "1426354675483"\n    },\n    {\n      "system": "http://starfleet-hospital.ufp/NamingSystem/patient-identifier",\n      "value": "NCC-7676"\n    },\n    {\n      "system": "http://starfleet-hospital.ufp/fhir/",\n      "value": "6768"\n    }\n  ],\n  "name": [\n    {\n      "family": "Sky",\n      "given": [\n        "Luc"\n      ]\n    }\n  ],\n  "telecom": [\n    {\n      "system": "phone",\n      "value": "+49 (0)12345 - 123456"\n    }\n  ],\n  "gender": "male",\n  "birthDate": "1980-01-01",\n  "address": [\n    {\n      "line": [\n        "Nowhere 42"\n      ],\n      "city": "Spöck",\n      "postalCode": "76297",\n      "country": "Germany"\n    }\n  ],\n  "maritalStatus": {\n    "coding": [\n      {\n        "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",\n        "code": "U",\n        "display": "unmarried"\n      }\n    ]\n  }\n}'




```python
response.json()
```




    {'resourceType': 'Patient',
     'id': '38',
     'meta': {'versionId': '32',
      'lastUpdated': '2019-10-30T14:16:54.484+00:00',
      'source': '#e0mm6ofqyX94cLL9'},
     'text': {'status': 'generated',
      'div': '<div xmlns="http://www.w3.org/1999/xhtml"> <div class="hapiHeaderText">Hi <b>HELLO </b> </div> <table class="hapiPropertyTable"> <tbody> <tr> <td>Identifier</td> <td>NCC-7676</td> </tr> <tr> <td>Address</td> <td> <span>Nowhere 42 </span> <br/> <span>Spöck </span> <span>Germany </span> </td> </tr> <tr> <td>Date of birth</td> <td> <span>24 October 1990</span> </td> </tr> </tbody> </table> </div>'},
     'identifier': [{'use': 'usual',
       'type': {'coding': [{'system': 'http://interopsante.org/fhir/valueset/fr-patient-identifier-type',
          'version': '1.0',
          'code': 'INS-NIR',
          'display': 'NIR définitif'}]},
       'system': 'urn:oid:1.2.250.1.213.1.4.10',
       'value': '1426354675483'},
      {'system': 'http://starfleet-hospital.ufp/NamingSystem/patient-identifier',
       'value': 'NCC-7676'},
      {'system': 'http://starfleet-hospital.ufp/fhir/', 'value': '6768'}],
     'name': [{'family': 'Sky', 'given': ['Luc']}],
     'telecom': [{'system': 'phone', 'value': '+49 (0)12345 - 123456'}],
     'gender': 'male',
     'birthDate': '1980-01-01',
     'address': [{'line': ['Nowhere 42'],
       'city': 'Spöck',
       'postalCode': '76297',
       'country': 'Germany'}],
     'maritalStatus': {'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-MaritalStatus',
        'code': 'U',
        'display': 'unmarried'}]}}




```python

```
