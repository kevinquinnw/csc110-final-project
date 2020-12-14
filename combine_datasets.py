"""
This file is Copyright (c) 2020 Mohamed Al-Fahim, Kevin Quinn, An Nguyen-Trinh, and Alexander Shchokin.
"""

import csv
from typing import Dict, List, Tuple

# The mapping of all the state codes to its full name
# (excluding the state of Hawaii and any U.S. territories)
STATES_CODE_TO_NAMES = {'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AZ': 'Arizona',
                        'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
                        'FL': 'Florida', 'GA': 'Georgia', 'IA': 'Iowa', 'ID': 'Idaho',
                        'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky',
                        'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine',
                        'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MS': 'Mississippi',
                        'MT': 'Montana', 'NC': 'North Carolina', 'ND': 'North Dakota',
                        'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
                        'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio',
                        'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
                        'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
                        'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia',
                        'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin',
                        'WV': 'West Virginia', 'WY': 'Wyoming'}


def read_temp_csv_data(filepath_temp: str) -> Dict[str, Dict[int, List[float]]]:
    """Return a mapping from the state to a mapping of the year to yearly data in the format
    [average temperature, precipitation, wildfire counts].

    Currently, the values for precipitation are wildfires counts are dummy values.

    Preconditions:
        - filepath refers to a csv file in the format of
          data/Annual_Temperature.csv
          (i.e., could be that file or a different file in the same format)
    """
    # ACCUMULATOR: The mapping from the state to its yearly data so far
    data_so_far = {}

    with open(filepath_temp) as file_temp:
        reader_temp = csv.reader(file_temp)

        # Skip the first 3 lines of the data
        for _ in range(0, 3):
            next(reader_temp)

        # Store the header containing the names of the states
        states = next(reader_temp)

        # Iterate through the header, skipping the 1st index, to map states to an empty dictionary,
        # which will map the year to the data about the average temp, precipitation, wildfire counts
        for i in range(1, len(states)):
            data_so_far[states[i]] = {}

        # Iterate through the remaining rows of the dataset
        for row in reader_temp:

            # The current year being processed
            year = int(row[0])

            # Iterate through each index of the row
            for i in range(1, len(row)):
                # The average temperature value of a state in the current year
                value_temp = float(row[i])

                # Create a mapping from the year to that year's data
                # in the format [average temp, precipitation, wildfires]
                data_so_far[states[i]][year] = [value_temp, 0, 0]  # The 0s are dummy values

    return data_so_far


def read_precip_csv_data(data: Dict[str, Dict[int, List[float]]], filepath_precip: str) -> None:
    """Read the data file storing the states' yearly precipitation values.
    Then, mutate the given dictionary of the state to its yearly data
    by replacing the precipitation's dummy value with the value from the dataset.

    Preconditions:
        - filepath refers to a csv file in the format of
          data/Annual_Precip.csv
          (i.e., could be that file or a different file in the same format)
    """
    # Extracting the key names (which are the state names) from the given mapping
    states_names = list(data)
    with open(filepath_precip) as file_precip:
        reader_precip = csv.reader(file_precip)

        # Skip the first 4 lines of the dataset
        for _ in range(0, 4):
            next(reader_precip)

        # Iterate through the remaining rows of the dataset
        for row in reader_precip:
            # The current year being processed
            year = int(row[0])

            # Iterate through each index of the row
            for i in range(1, len(row)):
                # The precipitation value of a state in the current year
                value_precip = float(row[i])

                # Extracting the state's data values from the given mapping
                # Index in the list state_names is off by 1 comparing the its index in the dataset
                state_data = data[states_names[i - 1]]

                # Replace the wildfire count's dummy value with the actual value
                state_data[year][1] = value_precip


def read_csv_fire_2019(data: Dict[str, Dict[int, List[float]]], filepath_fires: str) -> None:
    """Read the data file storing fire incidents in 2019.
    Then, mutate the given dictionary of the state to its yearly data by replacing
    the wildfire count's dummy value with the value from the dataset.

    Preconditions:
        - filepath refers to a csv file in the format of
          data/Historic_GeoMAC_Perimeters_2019.csv
          (i.e., could be that file or a different file in the same format)
    """
    with open(filepath_fires) as file_fires:
        reader_fires = csv.reader(file_fires)

        # Skip the header of the dataset
        next(reader_fires)

        for row in reader_fires:
            # Extract the location that the fire was in
            state_code = row[16]

            # Check if the location is the restricted list of states
            if state_code in STATES_CODE_TO_NAMES:
                # Extract the year
                year = int(row[7])

                # Get the state's full name
                state_name = STATES_CODE_TO_NAMES[state_code]

                # Get this state's data from the given mapping
                state_info_all = data[state_name]

                # Get this state's data in the year that the fire happened
                state_info_year = state_info_all[year]

                # Add the current state's fire count by 1
                state_info_year[2] += 1


def read_csv_fire_2000_2018(data: Dict[str, Dict[int, List[float]]], filepath_fires: str) -> None:
    """Read the data file storing fire incidents from 2000 to 2018.
    Then, mutate the given dictionary of the state to its yearly data by replacing
    the wildfire count's dummy value with the value from the dataset.

    Preconditions:
        - filepath refers to a csv file in the format of
          data/Historic_GeoMAC_Perimeters_Combined_2000-2018.csv
          (i.e., could be that file or a different file in the same format)
    """
    with open(filepath_fires) as file_fires:
        reader_fires = csv.reader(file_fires)

        # Skip the header of the dataset
        next(reader_fires)

        for row in reader_fires:
            # Extract the location that the fire was in
            state_code = row[15]

            # Check if the location is the restricted list of states
            if state_code in STATES_CODE_TO_NAMES:
                # Extract the year
                year = int(row[6])

                # Get the state's full name
                state_name = STATES_CODE_TO_NAMES[state_code]

                # Get this state's data from the given mapping
                state_info_all = data[state_name]

                # Get this state's data in the year that the fire happened
                state_info_year = state_info_all[year]

                # Add the current state's fire count by 1
                state_info_year[2] += 1


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-io': ['read_temp_csv_data',
                       'read_precip_csv_data',
                       'read_csv_fire_2019',
                       'read_csv_fire_2000_2018'],
        'extra-imports': ['python_ta.contracts', 'csv'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
