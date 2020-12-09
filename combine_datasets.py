"""
This file is Copyright (c) 2020 Mohamed Al-Fahim, Kevin Quinn, An Nguyen-Trinh, and Alexander Shchokin.
"""

import csv
from typing import Dict, List, Tuple

import pandas as pd

STATES_CODE_TO_NAMES = {'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AZ': 'Arizona', 'CA': 'California',
                        'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
                        'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas',
                        'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine',
                        'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MS': 'Mississippi', 'MT': 'Montana',
                        'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire',
                        'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio',
                        'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island',
                        'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah',
                        'VA': 'Virginia', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia',
                        'WY': 'Wyoming'}


def read_temp_csv_data(filepath_temp: str) -> Dict[str, Dict[int, List[float]]]:
    """Return a SIRD dictionary from the data mapped from a CSV file.

    n represents the initial population number.

    Preconditions:
        - filepath refers to a csv file in the format of
          data/modeling/ontario_covid_cases_2020_10_17.csv
          (i.e., could be that file or a different file in the same format)
        - n is the size of the population represented in the given csv file
    """
    data_so_far = {}

    with open(filepath_temp) as file_temp:
        reader_temp = csv.reader(file_temp)

        for _ in range(0, 3):
            next(reader_temp)

        states = next(reader_temp)
        for i in range(1, len(states)):
            data_so_far[states[i]] = {}

        for row in reader_temp:
            year = int(row[0])
            for i in range(1, len(row)):
                value_temp = float(row[i])
                data_so_far[states[i]][year] = [value_temp, 0, 0]

    return data_so_far


def read_precip_csv_data(data: Dict[str, Dict[int, List[float]]], filepath_precip: str) -> None:
    states_names = list(data)
    with open(filepath_precip) as file_precip:
        reader_precip = csv.reader(file_precip)

        for _ in range(0, 4):
            next(reader_precip)

        for row in reader_precip:
            year = int(row[0])
            for i in range(1, len(row)):
                value_precip = float(row[i])
                state_data = data[states_names[i-1]]
                state_data[year][1] = value_precip


def read_csv_fire_2019(data: Dict[str, Dict[int, List[float]]], filepath_fires: str) -> None:
    with open(filepath_fires) as file_fires:
        reader_fires = csv.reader(file_fires)

        next(reader_fires)
        for row in reader_fires:
            state_code = row[16]

            if state_code in STATES_CODE_TO_NAMES:
                year = int(row[7])

                state_name = STATES_CODE_TO_NAMES[state_code]

                state_info_all = data[state_name]

                state_info_year = state_info_all[year]

                state_info_year[2] += 1


def read_csv_fire_2000_2018(data: Dict[str, Dict[int, List[float]]], filepath_fires: str) -> None:
    with open(filepath_fires) as file_fires:
        reader_fires = csv.reader(file_fires)

        next(reader_fires)
        for row in reader_fires:
            state_code = row[15]

            if state_code in STATES_CODE_TO_NAMES:
                year = int(row[6])

                state_name = STATES_CODE_TO_NAMES[state_code]

                state_info_all = data[state_name]

                state_info_year = state_info_all[year]

                state_info_year[2] += 1


def read_csv_data_long_lang(filepath: str) -> Dict[str, Tuple[float, float]]:
    """
    Create and return a StateData instance for each state, excluding Hawaii, District of Columbia,
    and Puerto Rico (There's not data for Hawaii. District of Columbia and Puerto Rico are not U.S. states).

    Return a mapping from the state's postal code to the state's full name,
    so it can be used in the function reading the wildfire datasets.
    """
    # ACCUMULATOR: storing the state to its instance of StateDate
    states_location = {}

    with open(filepath) as file:
        reader = csv.reader(file)

        # Skip the header of the dataset
        next(reader)

        for row in reader:
            if row[0] in STATES_CODE_TO_NAMES:
                latitude, longitude = float(row[1]), float(row[2])

                state = STATES_CODE_TO_NAMES[row[0]]

                states_location[state] = (latitude, longitude)

    return states_location


# if __name__ == '__main__':
# Since our data isn't in a subfolder we do not need the extension
#     data = read_temp_csv_data('Annual Temperature_new.csv')
#     read_precip_csv_data(data, 'Annual Precip_new.csv')
#     read_csv_fire_2019(data, 'Historic_GeoMAC_Perimeters_2019.csv')
#     read_csv_fire_2000_2018(data, 'Historic_GeoMAC_Perimeters_Combined_2000-2018.csv')
#
#     df = pd.DataFrame.from_dict(data['Alabama'], orient='index', columns=['Average Temp', 'Precipitation', 'Fire Counts'])
#
#     print(df)
