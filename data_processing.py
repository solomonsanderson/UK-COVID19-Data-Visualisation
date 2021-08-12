import pandas as pd
from data_get import data_get


def data_processing(AREA_TYPE, AREA_NAME):
    response = data_get(AREA_TYPE, AREA_NAME)
    data = response.json()['data']
    data = pd.DataFrame.from_dict(data)
    return data

print(data_processing('utla', 'portsmouth'))