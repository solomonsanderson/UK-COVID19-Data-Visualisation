'''
Checks data.csv to see if it is up to date. If data is up to date saved data is used.
Web address for the API developer page: https://coronavirus.data.gov.uk/details/developers-guide#methods-get
'''


from requests import get
from json import dumps
from datetime import datetime
from datetime import timedelta
import pandas as pd
import os.path






def data_get(AREA_TYPE='nation', AREA_NAME='england'):

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
        "cumulativeDeaths": "cumDeaths28DaysByPublishDate",
        "newVaccinesGivenByPublishDate":"newVaccinesGivenByPublishDate",
        "cumVaccinesGivenByPublishDate":"cumVaccinesGivenByPublishDate",
        "newPeopleVaccinatedFirstDoseByPublishDate":"newPeopleVaccinatedFirstDoseByPublishDate",
        "cumPeopleVaccinatedFirstDoseByPublishDate":"cumPeopleVaccinatedFirstDoseByPublishDate",
        "newPeopleVaccinatedSecondDoseByPublishDate":"newPeopleVaccinatedSecondDoseByPublishDate",
        "cumPeopleVaccinatedSecondDoseByPublishDate":"cumPeopleVaccinatedSecondDoseByPublishDate",
    }

    params = {
        "filters": str.join(";", filters),
        "structure": dumps(structure, separators=(",", ":"))
    }

    # Checking if there is saved data for the location
    print(os.path.isfile(f'data\data_{AREA_NAME}.csv'))

    now = datetime.now()
    yesterday = (now - timedelta(days=1)).date()
    saved_data = pd.read_csv(f'data\data_{AREA_NAME}.csv')
    latest_update = datetime.strptime(saved_data.iloc[0]['date'], '%Y-%m-%d').date()
    print(latest_update)
    print(yesterday)
    if os.path.isfile(f'data\data_{AREA_NAME}.csv') and (latest_update == yesterday or now.date()):
        # when there is data for location checks date
        print("***Using saved data***")
        saved_data['date'] = pd.to_datetime(saved_data['date'])

        return saved_data
                    
    else:      
        print("***Updating Data***")
        response = get(ENDPOINT, params=params)

        if response.status_code >= 400:
            print(f"***Failed to Update*** \\ Request failed: { response.text }")
            return saved_data
            
        else:
            # saving data
            new_data = response.json()['data']
            new_data = pd.DataFrame.from_dict(new_data)
            new_data['date'] = pd.to_datetime(new_data['date'])
            pd.DataFrame.to_csv(new_data, f'data\data_{AREA_NAME}.csv')
            print("***Data Updated***")

            return new_data

# print(data_get('nation', 'england'))