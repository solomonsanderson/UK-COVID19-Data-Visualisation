'''
data from the response is processed to make it more  easily visualised in plotting.py
'''

import pandas as pd
from data_get import data_get


def data_processing(AREA_TYPE='nation', AREA_NAME='england'):
    response = data_get(AREA_TYPE, AREA_NAME)
    data = response.json()['data']
    data = pd.DataFrame.from_dict(data)
    data['date'] = pd.to_datetime(data['date'])
    print('***Processed***')
    print(data.columns)
    return data


def cases(data):
    pass

def deaths(data):
    pass