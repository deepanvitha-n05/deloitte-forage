import json
from datetime import datetime

with open('data-1.json','r', encoding='utf-8') as file_1:
    jsonData1 = json.load(file_1)

with open('data-2.json','r', encoding='utf-8') as file_2:
    jsonData2 = json.load(file_2)

with open('data-result.json','r', encoding='utf-8') as file_3:
    jsonExceptedResult = json.load(file_3)

def convertFromFormat1(jsonObject):
    locationParts = jsonObject['location'].split('/')

    result = {
        'deviceID': jsonObject['deviceID'],
        'deviceType': jsonObject['deviceType'],
        'timestamp': jsonObject['timestamp'],
        'location':{
            'country': locationParts[0],
            'city': locationParts[1],
            'area': locationParts[2],
            'factory': locationParts[3],
            'section': locationParts[4]
        },
        'data':{
            'status': jsonObject['operationStatus'],
            'temperature': jsonObject['temp'],
        }
    }

    return result

def iso_to_millis(iso_str):
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(dt.timestamp() * 1000)

def convertFromFormat2(jsonObject):

    result = {
        'deviceID': jsonObject['device']['id'],
        'deviceType': jsonObject['device']['type'],
        'timestamp': iso_to_millis(jsonObject['timestamp']),
        'location': {
            'country': jsonObject['country'],
            'city': jsonObject['city'],
            'area': jsonObject['area'],
            'factory': jsonObject['factory'],
            'section': jsonObject['section'],
        },
        'data':{
            'status': jsonObject['data']['status'],
            'temperature': jsonObject['data']['temperature'],
        }
    }

    return result

