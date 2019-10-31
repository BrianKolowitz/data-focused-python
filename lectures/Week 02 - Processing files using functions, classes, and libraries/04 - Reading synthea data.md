---
layout: default
title: 04 - Reading synthea data
parent: Week 02 - Processing files using functions, classes, and libraries
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
with open('../data/text/Augustine565_Conroy74_8d1c4f3b-3d44-4daf-8962-cc260bad8c87.txt') as f:
    for idx, line in enumerate(f.readlines()):
        print(f'{idx}: {line}')
#         if idx >= 5:
#             break
```

    0: Augustine565 Conroy74
    
    1: =====================
    
    2: Race:                Asian
    
    3: Ethnicity:           Non-Hispanic
    
    4: Gender:              F
    
    5: Age:                 49
    
    6: Birth Date:          1969-05-10
    
    7: Marital Status:      M
    
    8: --------------------------------------------------------------------------------
    
    9: ALLERGIES:
    
    10: No Known Allergies
    
    11: --------------------------------------------------------------------------------
    
    12: MEDICATIONS:
    
    13:   2011-05-21[STOPPED] : 3 ML liraglutide 6 MG/ML Pen Injector for Diabetes
    
    14:   2011-05-21[CURRENT] : 24 HR Metformin hydrochloride 500 MG Extended Release Oral Tablet for Diabetes
    
    15: --------------------------------------------------------------------------------
    
    16: CONDITIONS:
    
    17:   2017-05-26 - 2017-06-08 : Acute viral pharyngitis (disorder)
    
    18:   2016-08-06 -            : Hyperglycemia (disorder)
    
    19:   2016-07-27 -            : Chronic sinusitis (disorder)
    
    20:   2016-07-06 - 2016-08-17 : Acute bacterial sinusitis (disorder)
    
    21:   2013-05-25 -            : Metabolic syndrome X (disorder)
    
    22:   2013-05-25 -            : Hypertriglyceridemia (disorder)
    
    23:   2011-05-21 -            : Diabetes
    
    24:   2003-09-27 -            : Body mass index 30+ - obesity (finding)
    
    25: --------------------------------------------------------------------------------
    
    26: CARE PLANS:
    
    27:   2011-05-21[CURRENT] : Diabetes self management plan
    
    28:                          Reason: Diabetes
    
    29:                          Activity: Diabetic diet
    
    30:                          Activity: Exercise therapy
    
    31: --------------------------------------------------------------------------------
    
    32: REPORTS:
    
    33:   2017-06-03 : Lipid Panel
    
    34:            - Total Cholesterol                        245.0 mg/dL
    
    35:            - Triglycerides                            370.4 mg/dL
    
    36:            - Low Density Lipoprotein Cholesterol      139.3 mg/dL
    
    37:            - High Density Lipoprotein Cholesterol     31.6 mg/dL
    
    38:   2017-06-03 : Basic Metabolic Panel
    
    39:            - Glucose                                  135.8 mg/dL
    
    40:            - Urea Nitrogen                            9.8 mg/dL
    
    41:            - Creatinine                               1.1 mg/dL
    
    42:            - Calcium                                  9.0 mg/dL
    
    43:            - Sodium                                   137.8 mmol/L
    
    44:            - Potassium                                3.7 mmol/L
    
    45:            - Chloride                                 106.0 mmol/L
    
    46:            - Carbon Dioxide                           22.7 mmol/L
    
    47:   2016-08-06 : Lipid Panel
    
    48:            - Total Cholesterol                        245.3 mg/dL
    
    49:            - Triglycerides                            459.5 mg/dL
    
    50:            - Low Density Lipoprotein Cholesterol      121.1 mg/dL
    
    51:            - High Density Lipoprotein Cholesterol     32.3 mg/dL
    
    52:   2016-08-06 : Basic Metabolic Panel
    
    53:            - Glucose                                  133.0 mg/dL
    
    54:            - Urea Nitrogen                            19.3 mg/dL
    
    55:            - Creatinine                               1.1 mg/dL
    
    56:            - Calcium                                  9.6 mg/dL
    
    57:            - Sodium                                   142.4 mmol/L
    
    58:            - Potassium                                4.3 mmol/L
    
    59:            - Chloride                                 103.3 mmol/L
    
    60:            - Carbon Dioxide                           25.3 mmol/L
    
    61:   2015-05-30 : Complete blood count (hemogram) panel - Blood by Automated count
    
    62:            - Leukocytes [#/volume] in Blood by Automated count 5.3 10*3/uL
    
    63:            - Erythrocytes [#/volume] in Blood by Automated count 5.3 10*6/uL
    
    64:            - Hemoglobin [Mass/volume] in Blood        12.4 g/dL
    
    65:            - Hematocrit [Volume Fraction] of Blood by Automated count 35.0 %
    
    66:            - MCV [Entitic volume] by Automated count  86.9 fL
    
    67:            - MCH [Entitic mass] by Automated count    28.0 pg
    
    68:            - MCHC [Mass/volume] by Automated count    33.3 g/dL
    
    69:            - Erythrocyte distribution width [Entitic volume] by Automated count 42.9 fL
    
    70:            - Platelets [#/volume] in Blood by Automated count 330.1 10*3/uL
    
    71:            - Platelet distribution width [Entitic volume] in Blood by Automated count 255.2 fL
    
    72:            - Platelet mean volume [Entitic volume] in Blood by Automated count 11.6 fL
    
    73:   2015-05-30 : Lipid Panel
    
    74:            - Total Cholesterol                        226.7 mg/dL
    
    75:            - Triglycerides                            191.0 mg/dL
    
    76:            - Low Density Lipoprotein Cholesterol      137.2 mg/dL
    
    77:            - High Density Lipoprotein Cholesterol     51.3 mg/dL
    
    78:   2015-05-30 : Basic Metabolic Panel
    
    79:            - Glucose                                  121.6 mg/dL
    
    80:            - Urea Nitrogen                            9.9 mg/dL
    
    81:            - Creatinine                               1.4 mg/dL
    
    82:            - Calcium                                  9.7 mg/dL
    
    83:            - Sodium                                   143.7 mmol/L
    
    84:            - Potassium                                4.4 mmol/L
    
    85:            - Chloride                                 107.5 mmol/L
    
    86:            - Carbon Dioxide                           22.6 mmol/L
    
    87:   2013-05-25 : Lipid Panel
    
    88:            - Total Cholesterol                        273.8 mg/dL
    
    89:            - Triglycerides                            540.3 mg/dL
    
    90:            - Low Density Lipoprotein Cholesterol      149.5 mg/dL
    
    91:            - High Density Lipoprotein Cholesterol     16.2 mg/dL
    
    92:   2013-05-25 : Basic Metabolic Panel
    
    93:            - Glucose                                  197.9 mg/dL
    
    94:            - Urea Nitrogen                            10.8 mg/dL
    
    95:            - Creatinine                               1.0 mg/dL
    
    96:            - Calcium                                  9.3 mg/dL
    
    97:            - Sodium                                   143.6 mmol/L
    
    98:            - Potassium                                4.2 mmol/L
    
    99:            - Chloride                                 102.1 mmol/L
    
    100:            - Carbon Dioxide                           26.8 mmol/L
    
    101:   2011-05-21 : Lipid Panel
    
    102:            - Total Cholesterol                        178.3 mg/dL
    
    103:            - Triglycerides                            120.6 mg/dL
    
    104:            - Low Density Lipoprotein Cholesterol      79.1 mg/dL
    
    105:            - High Density Lipoprotein Cholesterol     75.0 mg/dL
    
    106:   2009-05-16 : Complete blood count (hemogram) panel - Blood by Automated count
    
    107:            - Leukocytes [#/volume] in Blood by Automated count 9.4 10*3/uL
    
    108:            - Erythrocytes [#/volume] in Blood by Automated count 4.2 10*6/uL
    
    109:            - Hemoglobin [Mass/volume] in Blood        13.7 g/dL
    
    110:            - Hematocrit [Volume Fraction] of Blood by Automated count 46.2 %
    
    111:            - MCV [Entitic volume] by Automated count  91.9 fL
    
    112:            - MCH [Entitic mass] by Automated count    27.3 pg
    
    113:            - MCHC [Mass/volume] by Automated count    35.9 g/dL
    
    114:            - Erythrocyte distribution width [Entitic volume] by Automated count 42.6 fL
    
    115:            - Platelets [#/volume] in Blood by Automated count 255.3 10*3/uL
    
    116:            - Platelet distribution width [Entitic volume] in Blood by Automated count 281.4 fL
    
    117:            - Platelet mean volume [Entitic volume] in Blood by Automated count 11.3 fL
    
    118: --------------------------------------------------------------------------------
    
    119: OBSERVATIONS:
    
    120:   2017-06-03 : Hemoglobin A1c/Hemoglobin.total in Blood 8.6 %
    
    121:   2017-06-03 : Tobacco smoking status NHIS              Never smoker 
    
    122:   2017-06-03 : Estimated Glomerular Filtration Rate     141.8 mL/min/{1.73_m2}
    
    123:   2017-06-03 : Microalbumin Creatinine Ratio            5.7 mg/g
    
    124:   2017-06-03 : High Density Lipoprotein Cholesterol     31.6 mg/dL
    
    125:   2017-06-03 : Low Density Lipoprotein Cholesterol      139.3 mg/dL
    
    126:   2017-06-03 : Triglycerides                            370.4 mg/dL
    
    127:   2017-06-03 : Total Cholesterol                        245.0 mg/dL
    
    128:   2017-06-03 : Carbon Dioxide                           22.7 mmol/L
    
    129:   2017-06-03 : Chloride                                 106.0 mmol/L
    
    130:   2017-06-03 : Potassium                                3.7 mmol/L
    
    131:   2017-06-03 : Sodium                                   137.8 mmol/L
    
    132:   2017-06-03 : Calcium                                  9.0 mg/dL
    
    133:   2017-06-03 : Creatinine                               1.1 mg/dL
    
    134:   2017-06-03 : Urea Nitrogen                            9.8 mg/dL
    
    135:   2017-06-03 : Glucose                                  135.8 mg/dL
    
    136:   2017-06-03 : Blood Pressure
    
    137:            - Diastolic Blood Pressure                 77.8 mmHg
    
    138:            - Systolic Blood Pressure                  113.1 mmHg
    
    139:   2017-06-03 : Body Mass Index                          40.5 kg/m2
    
    140:   2017-06-03 : Body Weight                              97.6 kg
    
    141:   2017-06-03 : Pain severity - 0-10 verbal numeric rating [Score] - Reported 3.3 {score}
    
    142:   2017-06-03 : Body Height                              155.3 cm
    
    143:   2017-05-26 : Oral temperature                         38.0 Cel
    
    144:   2016-08-06 : Hemoglobin A1c/Hemoglobin.total in Blood 8.4 %
    
    145:   2016-08-06 : Tobacco smoking status NHIS              Never smoker 
    
    146:   2016-08-06 : Estimated Glomerular Filtration Rate     142.2 mL/min/{1.73_m2}
    
    147:   2016-08-06 : Microalbumin Creatinine Ratio            15.4 mg/g
    
    148:   2016-08-06 : High Density Lipoprotein Cholesterol     32.3 mg/dL
    
    149:   2016-08-06 : Low Density Lipoprotein Cholesterol      121.1 mg/dL
    
    150:   2016-08-06 : Triglycerides                            459.5 mg/dL
    
    151:   2016-08-06 : Total Cholesterol                        245.3 mg/dL
    
    152:   2016-08-06 : Carbon Dioxide                           25.3 mmol/L
    
    153:   2016-08-06 : Chloride                                 103.3 mmol/L
    
    154:   2016-08-06 : Potassium                                4.3 mmol/L
    
    155:   2016-08-06 : Sodium                                   142.4 mmol/L
    
    156:   2016-08-06 : Calcium                                  9.6 mg/dL
    
    157:   2016-08-06 : Creatinine                               1.1 mg/dL
    
    158:   2016-08-06 : Urea Nitrogen                            19.3 mg/dL
    
    159:   2016-08-06 : Glucose                                  133.0 mg/dL
    
    160:   2016-08-06 : Blood Pressure
    
    161:            - Diastolic Blood Pressure                 77.1 mmHg
    
    162:            - Systolic Blood Pressure                  100.9 mmHg
    
    163:   2016-08-06 : Body Mass Index                          39.7 kg/m2
    
    164:   2016-08-06 : Body Weight                              95.9 kg
    
    165:   2016-08-06 : Pain severity - 0-10 verbal numeric rating [Score] - Reported 1.0 {score}
    
    166:   2016-08-06 : Body Height                              155.3 cm
    
    167:   2015-05-30 : Hemoglobin A1c/Hemoglobin.total in Blood 8.2 %
    
    168:   2015-05-30 : Tobacco smoking status NHIS              Never smoker 
    
    169:   2015-05-30 : Estimated Glomerular Filtration Rate     72.6 mL/min/{1.73_m2}
    
    170:   2015-05-30 : Platelet mean volume [Entitic volume] in Blood by Automated count 11.6 fL
    
    171:   2015-05-30 : Platelet distribution width [Entitic volume] in Blood by Automated count 255.2 fL
    
    172:   2015-05-30 : Platelets [#/volume] in Blood by Automated count 330.1 10*3/uL
    
    173:   2015-05-30 : Erythrocyte distribution width [Entitic volume] by Automated count 42.9 fL
    
    174:   2015-05-30 : MCHC [Mass/volume] by Automated count    33.3 g/dL
    
    175:   2015-05-30 : MCH [Entitic mass] by Automated count    28.0 pg
    
    176:   2015-05-30 : MCV [Entitic volume] by Automated count  86.9 fL
    
    177:   2015-05-30 : Hematocrit [Volume Fraction] of Blood by Automated count 35.0 %
    
    178:   2015-05-30 : Hemoglobin [Mass/volume] in Blood        12.4 g/dL
    
    179:   2015-05-30 : Erythrocytes [#/volume] in Blood by Automated count 5.3 10*6/uL
    
    180:   2015-05-30 : Leukocytes [#/volume] in Blood by Automated count 5.3 10*3/uL
    
    181:   2015-05-30 : Microalbumin Creatinine Ratio            9.5 mg/g
    
    182:   2015-05-30 : High Density Lipoprotein Cholesterol     51.3 mg/dL
    
    183:   2015-05-30 : Low Density Lipoprotein Cholesterol      137.2 mg/dL
    
    184:   2015-05-30 : Triglycerides                            191.0 mg/dL
    
    185:   2015-05-30 : Total Cholesterol                        226.7 mg/dL
    
    186:   2015-05-30 : Carbon Dioxide                           22.6 mmol/L
    
    187:   2015-05-30 : Chloride                                 107.5 mmol/L
    
    188:   2015-05-30 : Potassium                                4.4 mmol/L
    
    189:   2015-05-30 : Sodium                                   143.7 mmol/L
    
    190:   2015-05-30 : Calcium                                  9.7 mg/dL
    
    191:   2015-05-30 : Creatinine                               1.4 mg/dL
    
    192:   2015-05-30 : Urea Nitrogen                            9.9 mg/dL
    
    193:   2015-05-30 : Glucose                                  121.6 mg/dL
    
    194:   2015-05-30 : Blood Pressure
    
    195:            - Diastolic Blood Pressure                 72.6 mmHg
    
    196:            - Systolic Blood Pressure                  125.0 mmHg
    
    197:   2015-05-30 : Body Mass Index                          39.0 kg/m2
    
    198:   2015-05-30 : Body Weight                              94.0 kg
    
    199:   2015-05-30 : Pain severity - 0-10 verbal numeric rating [Score] - Reported 0.3 {score}
    
    200:   2015-05-30 : Body Height                              155.3 cm
    
    201:   2013-05-25 : Hemoglobin A1c/Hemoglobin.total in Blood 7.4 %
    
    202:   2013-05-25 : Tobacco smoking status NHIS              Never smoker 
    
    203:   2013-05-25 : Estimated Glomerular Filtration Rate     157.6 mL/min/{1.73_m2}
    
    204:   2013-05-25 : Microalbumin Creatinine Ratio            12.5 mg/g
    
    205:   2013-05-25 : High Density Lipoprotein Cholesterol     16.2 mg/dL
    
    206:   2013-05-25 : Low Density Lipoprotein Cholesterol      149.5 mg/dL
    
    207:   2013-05-25 : Triglycerides                            540.3 mg/dL
    
    208:   2013-05-25 : Total Cholesterol                        273.8 mg/dL
    
    209:   2013-05-25 : Carbon Dioxide                           26.8 mmol/L
    
    210:   2013-05-25 : Chloride                                 102.1 mmol/L
    
    211:   2013-05-25 : Potassium                                4.2 mmol/L
    
    212:   2013-05-25 : Sodium                                   143.6 mmol/L
    
    213:   2013-05-25 : Calcium                                  9.3 mg/dL
    
    214:   2013-05-25 : Creatinine                               1.0 mg/dL
    
    215:   2013-05-25 : Urea Nitrogen                            10.8 mg/dL
    
    216:   2013-05-25 : Glucose                                  197.9 mg/dL
    
    217:   2013-05-25 : Blood Pressure
    
    218:            - Diastolic Blood Pressure                 77.8 mmHg
    
    219:            - Systolic Blood Pressure                  119.9 mmHg
    
    220:   2013-05-25 : Body Mass Index                          37.5 kg/m2
    
    221:   2013-05-25 : Body Weight                              90.5 kg
    
    222:   2013-05-25 : Pain severity - 0-10 verbal numeric rating [Score] - Reported 2.3 {score}
    
    223:   2013-05-25 : Body Height                              155.3 cm
    
    224:   2011-05-21 : Hemoglobin A1c/Hemoglobin.total in Blood 9.1 %
    
    225:   2011-05-21 : Tobacco smoking status NHIS              Never smoker 
    
    226:   2011-05-21 : High Density Lipoprotein Cholesterol     75.0 mg/dL
    
    227:   2011-05-21 : Low Density Lipoprotein Cholesterol      79.1 mg/dL
    
    228:   2011-05-21 : Triglycerides                            120.6 mg/dL
    
    229:   2011-05-21 : Total Cholesterol                        178.3 mg/dL
    
    230:   2011-05-21 : Blood Pressure
    
    231:            - Diastolic Blood Pressure                 77.2 mmHg
    
    232:            - Systolic Blood Pressure                  112.7 mmHg
    
    233:   2011-05-21 : Body Mass Index                          36.2 kg/m2
    
    234:   2011-05-21 : Body Weight                              87.4 kg
    
    235:   2011-05-21 : Pain severity - 0-10 verbal numeric rating [Score] - Reported 2.9 {score}
    
    236:   2011-05-21 : Body Height                              155.3 cm
    
    237:   2009-05-16 : Tobacco smoking status NHIS              Never smoker 
    
    238:   2009-05-16 : Platelet mean volume [Entitic volume] in Blood by Automated count 11.3 fL
    
    239:   2009-05-16 : Platelet distribution width [Entitic volume] in Blood by Automated count 281.4 fL
    
    240:   2009-05-16 : Platelets [#/volume] in Blood by Automated count 255.3 10*3/uL
    
    241:   2009-05-16 : Erythrocyte distribution width [Entitic volume] by Automated count 42.6 fL
    
    242:   2009-05-16 : MCHC [Mass/volume] by Automated count    35.9 g/dL
    
    243:   2009-05-16 : MCH [Entitic mass] by Automated count    27.3 pg
    
    244:   2009-05-16 : MCV [Entitic volume] by Automated count  91.9 fL
    
    245:   2009-05-16 : Hematocrit [Volume Fraction] of Blood by Automated count 46.2 %
    
    246:   2009-05-16 : Hemoglobin [Mass/volume] in Blood        13.7 g/dL
    
    247:   2009-05-16 : Erythrocytes [#/volume] in Blood by Automated count 4.2 10*6/uL
    
    248:   2009-05-16 : Leukocytes [#/volume] in Blood by Automated count 9.4 10*3/uL
    
    249:   2009-05-16 : Blood Pressure
    
    250:            - Diastolic Blood Pressure                 82.9 mmHg
    
    251:            - Systolic Blood Pressure                  131.7 mmHg
    
    252:   2009-05-16 : Body Mass Index                          34.2 kg/m2
    
    253:   2009-05-16 : Body Weight                              82.6 kg
    
    254:   2009-05-16 : Pain severity - 0-10 verbal numeric rating [Score] - Reported 3.5 {score}
    
    255:   2009-05-16 : Body Height                              155.3 cm
    
    256: --------------------------------------------------------------------------------
    
    257: PROCEDURES:
    
    258:   2017-06-03 : Documentation of current medications
    
    259:   2016-08-06 : Documentation of current medications
    
    260:   2015-05-30 : Documentation of current medications
    
    261:   2013-05-25 : Documentation of current medications
    
    262: --------------------------------------------------------------------------------
    
    263: IMMUNIZATIONS:
    
    264:   2017-06-03 : Influenza, seasonal, injectable, preservative free
    
    265:   2016-08-06 : Influenza, seasonal, injectable, preservative free
    
    266:   2015-05-30 : Influenza, seasonal, injectable, preservative free
    
    267:   2013-05-25 : Influenza, seasonal, injectable, preservative free
    
    268:   2011-05-21 : Hep A, adult
    
    269:   2011-05-21 : Td (adult) preservative free
    
    270:   2011-05-21 : Influenza, seasonal, injectable, preservative free
    
    271:   2009-05-16 : Hep A, adult
    
    272:   2009-05-16 : Influenza, seasonal, injectable, preservative free
    
    273: --------------------------------------------------------------------------------
    
    274: ENCOUNTERS:
    
    275: 2017-06-03 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY
    
    276: 2017-05-26 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY : Encounter for Acute viral pharyngitis (disorder)
    
    277: 2016-08-06 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY
    
    278: 2016-07-27 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY : Encounter for Acute bacterial sinusitis (disorder)
    
    279: 2016-07-06 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY : Encounter for Acute bacterial sinusitis (disorder)
    
    280: 2015-05-30 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY
    
    281: 2013-05-25 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY
    
    282: 2011-05-21 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY
    
    283: 2009-05-16 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY
    
    284: 2003-09-27 (Dr. Del587 Williamson769) : Encounter at UPMC MERCY
    
    285: --------------------------------------------------------------------------------
    
    286: IMAGING STUDIES:
    
    287: --------------------------------------------------------------------------------
    



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
    
    30ee89ff-1932-4e7d-8358-7f84527f622e,8074c9c5-982f-3d30-8a5f-95f6ba9fde06,Del587 Williamson769,M,GENERAL PRACTICE,1400 LOCUST STREET,PITTSBURGH,PA,15219,2501,
    
    2570b996-8b89-417a-a661-a66c22e84b07,797d87ed-77fa-3b01-b971-0399bb10dc09,Bethany501 Windler79,F,GENERAL PRACTICE,3459 5TH AVENUE,PITTSBURGH,PA,15213,8,
    


## Reading XML Data


```python
with open('../data/ccda/Augustine565_Conroy74_8d1c4f3b-3d44-4daf-8962-cc260bad8c87.xml') as f:
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
with open('../data/FHIR/Augustine565_Conroy74_8d1c4f3b-3d44-4daf-8962-cc260bad8c87.json') as f:
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
    
    5:       "fullUrl": "urn:uuid:4aaeea96-ef44-4d86-a313-ed9658b91618",
    



```python

```
