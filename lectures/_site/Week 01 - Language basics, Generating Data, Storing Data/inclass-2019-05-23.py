import requests

def get_patient_data(patient_id):
    res = requests.get(f'http://hapi.fhir.org/baseDstu3/Patient/{patient_id}/_history/1?_pretty=true&_format=json')
    return res.json()


def get_data(id, 
    fhir_base='http://hapi.fhir.org/baseDstu3/',
    fhir_resource='Patient/'):

    res = requests.get(f'{fhir_base}{fhir_resource}{id}')
    return res.status_code, res.json()


if __name__ == "__main__":
    data = get_data(1627582)
    print(type(data), len(data))
    print(data[0], '\n')
    print(data[1])
    
    # print(type(data[0]), data[0])
    # print(type(data[1]), data[1])
    # status, data = get_data(1627582)
    # print(status)
    # print(data)
    # print('Patient Data', patient_data, '\n')
    


    # patient_data = get_data(1627582)
    # print('Patient Data', patient_data, '\n')

    # observation_data = get_data(445905, fhir_resource='Observation/')
    # print('Observation Data', observation_data, '\n')
    
