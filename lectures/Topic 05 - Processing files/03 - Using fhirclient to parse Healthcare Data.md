---
layout: default
title: 03 - Using fhirclient to parse Healthcare Data
parent: Topic 05 - Processing files
grand_parent: Lectures
nav_order: 5
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

For FHIR version 3

```bash
pip install fhirclient
```

or for FHIR version 4

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

patient = p.Patient.read('2543713', smart.server)
print(patient.birthDate.isostring)
print(smart.human_name(patient.name[0]))
```

    1974-12-25
    Peter James Chalmers


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

### Search Records on Server

You can also search for resources matching a particular set of criteria:


```python
smart = client.FHIRClient(settings=settings)

import fhirclient.models.patient as p

search = p.Patient.where(struct={'family': 'Cushing'})
patients = search.perform_resources(smart.server)
# print(observations)

pprint(patients[0].as_json())
```

    {'id': '2581341',
     'identifier': [{'type': {'coding': [{'code': 'MR',
                                          'system': 'http://hl7.org/fhir/v2/0203'}]},
                     'value': 'dbee78a3-a72d-41a2-b705-0023498f5228'}],
     'meta': {'lastUpdated': '2021-10-07T05:30:35.359+00:00',
              'source': '#ghjs1LZGhTvv0mp2',
              'versionId': '1'},
     'name': [{'family': 'Cushing', 'given': ['Caleb']}],
     'resourceType': 'Patient',
     'text': {'div': '<div xmlns="http://www.w3.org/1999/xhtml"><div '
                     'class="hapiHeaderText">Caleb <b>CUSHING </b></div><table '
                     'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>dbee78a3-a72d-41a2-b705-0023498f5228</td></tr></tbody></table></div>',
              'status': 'generated'}}



```python
# to get the raw Bundle instead of resources only, you can use:
bundle = search.perform(smart.server)
pprint(bundle.as_json())
```

    {'entry': [{'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/2581341',
                'resource': {'id': '2581341',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': 'dbee78a3-a72d-41a2-b705-0023498f5228'}],
                             'meta': {'lastUpdated': '2021-10-07T05:30:35.359+00:00',
                                      'source': '#ghjs1LZGhTvv0mp2',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>dbee78a3-a72d-41a2-b705-0023498f5228</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/2581393',
                'resource': {'id': '2581393',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '2575e281-136c-489b-9b4e-4baba209258e'}],
                             'meta': {'lastUpdated': '2021-10-07T05:30:55.659+00:00',
                                      'source': '#CHofcK6KSc6z9CD3',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>2575e281-136c-489b-9b4e-4baba209258e</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/2581353',
                'resource': {'id': '2581353',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '174ee1ec-c239-4b82-84a6-f0354aa6ee5f'}],
                             'meta': {'lastUpdated': '2021-10-07T05:30:39.301+00:00',
                                      'source': '#vB6DyRxG5VKe1DAW',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>174ee1ec-c239-4b82-84a6-f0354aa6ee5f</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/2581361',
                'resource': {'id': '2581361',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '7c411bcd-c418-42d5-98d1-15aac35c7be0'}],
                             'meta': {'lastUpdated': '2021-10-07T05:30:41.751+00:00',
                                      'source': '#bmgIW3uJ6beOv2VV',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>7c411bcd-c418-42d5-98d1-15aac35c7be0</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/2581369',
                'resource': {'id': '2581369',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '9972a064-bebe-424c-9093-3c9a159ef810'}],
                             'meta': {'lastUpdated': '2021-10-07T05:30:47.767+00:00',
                                      'source': '#Gv3zhMPhdfY3kmZV',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>9972a064-bebe-424c-9093-3c9a159ef810</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/2581377',
                'resource': {'id': '2581377',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': 'f5f32d1f-4cb7-46ca-aa9e-2cf0ceddcf2d'}],
                             'meta': {'lastUpdated': '2021-10-07T05:30:50.334+00:00',
                                      'source': '#H1FwlSuIbTH8HoQO',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>f5f32d1f-4cb7-46ca-aa9e-2cf0ceddcf2d</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/2581385',
                'resource': {'id': '2581385',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '6354a4f3-d14c-46fd-935b-061f12ae61cf'}],
                             'meta': {'lastUpdated': '2021-10-07T05:30:52.897+00:00',
                                      'source': '#PY6zZl3CLaJBv1iE',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>6354a4f3-d14c-46fd-935b-061f12ae61cf</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1710186',
                'resource': {'id': '1710186',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '4221bcac-4dc9-4bc4-9998-c926228c82b6'}],
                             'meta': {'lastUpdated': '2020-12-12T05:30:20.585+00:00',
                                      'source': '#MW9t13hB5Sot1wr8',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>4221bcac-4dc9-4bc4-9998-c926228c82b6</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1710194',
                'resource': {'id': '1710194',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '8c01f1ab-b1bd-49ed-8d2b-d05604d3b647'}],
                             'meta': {'lastUpdated': '2020-12-12T05:30:25.227+00:00',
                                      'source': '#oFl3LmIy0jJBy2uW',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>8c01f1ab-b1bd-49ed-8d2b-d05604d3b647</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1710202',
                'resource': {'id': '1710202',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': 'c7fdceca-5c46-43a3-8612-f05b653d8d50'}],
                             'meta': {'lastUpdated': '2020-12-12T05:30:26.105+00:00',
                                      'source': '#PObX9KJkPSlqEaqq',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>c7fdceca-5c46-43a3-8612-f05b653d8d50</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1710210',
                'resource': {'id': '1710210',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '524ba1f0-4d0b-4156-a027-090271ad0b9d'}],
                             'meta': {'lastUpdated': '2020-12-12T05:30:27.026+00:00',
                                      'source': '#QJBnM09DMDikgg58',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>524ba1f0-4d0b-4156-a027-090271ad0b9d</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1710218',
                'resource': {'id': '1710218',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '670ff5c0-1bb8-49b6-afa4-ba1ea116dfcd'}],
                             'meta': {'lastUpdated': '2020-12-12T05:30:27.852+00:00',
                                      'source': '#fr8pH05YdV3GcXaX',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>670ff5c0-1bb8-49b6-afa4-ba1ea116dfcd</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1710226',
                'resource': {'id': '1710226',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '71083472-9e8e-4850-9e71-3e0ea9eb72bf'}],
                             'meta': {'lastUpdated': '2020-12-12T05:30:28.868+00:00',
                                      'source': '#n8oLKEzzwtyWtIq0',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>71083472-9e8e-4850-9e71-3e0ea9eb72bf</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1710238',
                'resource': {'id': '1710238',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': 'b0f4dc2f-62b2-480f-a9de-9330e20bcf73'}],
                             'meta': {'lastUpdated': '2020-12-12T05:30:30.304+00:00',
                                      'source': '#qTLtPryVVRvxQWJx',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>b0f4dc2f-62b2-480f-a9de-9330e20bcf73</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1567009',
                'resource': {'id': '1567009',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '835855bd-e369-4dad-b29f-88b3eac35886'}],
                             'meta': {'lastUpdated': '2020-10-13T05:30:33.394+00:00',
                                      'source': '#v4eEjiC3mU1IFuh1',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>835855bd-e369-4dad-b29f-88b3eac35886</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1567021',
                'resource': {'id': '1567021',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': 'b769ce39-54b0-42cd-bfc1-b2bc00bc8503'}],
                             'meta': {'lastUpdated': '2020-10-13T05:30:35.498+00:00',
                                      'source': '#PPFZF3sf3RtNCdg3',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>b769ce39-54b0-42cd-bfc1-b2bc00bc8503</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1567029',
                'resource': {'id': '1567029',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '67687225-1f93-49fc-a269-f33b1dea0fc2'}],
                             'meta': {'lastUpdated': '2020-10-13T05:30:36.314+00:00',
                                      'source': '#YKCsK4p3FGH5uptc',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>67687225-1f93-49fc-a269-f33b1dea0fc2</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1567037',
                'resource': {'id': '1567037',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': 'c345df12-ff3a-431a-b149-77c4e20d1e84'}],
                             'meta': {'lastUpdated': '2020-10-13T05:30:40.008+00:00',
                                      'source': '#7xIEqCRuJyGrEyWX',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>c345df12-ff3a-431a-b149-77c4e20d1e84</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1567045',
                'resource': {'id': '1567045',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': 'e4d1beaa-5034-4f52-9489-69c7a4af355d'}],
                             'meta': {'lastUpdated': '2020-10-13T05:30:40.845+00:00',
                                      'source': '#1ig80EBKlB6QubTN',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>e4d1beaa-5034-4f52-9489-69c7a4af355d</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}},
               {'fullUrl': 'http://hapi.fhir.org/baseR4/Patient/1567053',
                'resource': {'id': '1567053',
                             'identifier': [{'type': {'coding': [{'code': 'MR',
                                                                  'system': 'http://hl7.org/fhir/v2/0203'}]},
                                             'value': '02d67065-0107-4f99-b967-ee4396a037ba'}],
                             'meta': {'lastUpdated': '2020-10-13T05:30:41.748+00:00',
                                      'source': '#Jrmnbq6HWRAMwvQ6',
                                      'versionId': '1'},
                             'name': [{'family': 'Cushing', 'given': ['Caleb']}],
                             'resourceType': 'Patient',
                             'text': {'div': '<div '
                                             'xmlns="http://www.w3.org/1999/xhtml"><div '
                                             'class="hapiHeaderText">Caleb '
                                             '<b>CUSHING </b></div><table '
                                             'class="hapiPropertyTable"><tbody><tr><td>Identifier</td><td>02d67065-0107-4f99-b967-ee4396a037ba</td></tr></tbody></table></div>',
                                      'status': 'generated'}},
                'search': {'mode': 'match'}}],
     'id': '80e8c67f-800d-4fce-8299-5b674b257a5b',
     'link': [{'relation': 'self',
               'url': 'http://hapi.fhir.org/baseR4/Patient?family=Cushing'},
              {'relation': 'next',
               'url': 'http://hapi.fhir.org/baseR4?_getpages=80e8c67f-800d-4fce-8299-5b674b257a5b&_getpagesoffset=20&_count=20&_pretty=true&_bundletype=searchset'}],
     'meta': {'lastUpdated': '2021-10-21T14:34:50.512+00:00'},
     'resourceType': 'Bundle',
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

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_93131/1295677727.py in <module>
          1 name.given = 'Peter'
    ----> 2 patient.as_json() # throws FHIRValidationError: because we incorrectly set the name to a string
    

    ~/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/fhirclient/models/fhirabstractresource.py in as_json(self)
         40 
         41     def as_json(self):
    ---> 42         js = super(FHIRAbstractResource, self).as_json()
         43         js['resourceType'] = self.resource_type
         44         return js


    ~/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/fhirclient/models/fhirabstractbase.py in as_json(self)
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



```python

```
