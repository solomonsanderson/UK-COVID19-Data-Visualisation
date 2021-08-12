'''
Gets data from the API

Web address for the API developer page: https://coronavirus.data.gov.uk/details/developers-guide#methods-get
'''

from requests import get
from json import dumps

def data_get(AREA_TYPE, AREA_NAME):

    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
    

    filters = [
        f"areaType={ AREA_TYPE }",
        f"areaName={ AREA_NAME }"
    ]

    structure = {
        "date": "date",
        "name": "areaName",
        "code": "areaCode",
        "dailyCases": "newCasesByPublishDate",
        "cumulativeCases": "cumCasesByPublishDate",
        "dailyDeaths": "newDeaths28DaysByPublishDate",
        "cumulativeDeaths": "cumDeaths28DaysByPublishDate"
    }

    params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":"))
    }


    response = get(ENDPOINT, params=params)


    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')

    else:
        return response