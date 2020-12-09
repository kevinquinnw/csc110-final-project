""" Everything needed to predict the future counts"""
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List


def data_adder(data: Dict, state: str, future: int) -> None:
    """ Predict future values
    """
    # First, we need to create future values for all of our regression variables.

    for year in range(2020, future+1):
        data[state][year] = create_new_averages(data, state)


def create_new_averages(data: Dict, state: str) -> List:
    """Yeehaw"""
    st = list(data[state].values())

    temp_lst = []
    precip_lst = []
    count_lst = []
    for i in range(len(st)):
        temp_lst.append(st[i][0])
        precip_lst.append(st[i][1])
        count_lst.append(st[i][2])

    new_temp = (round(sum(temp_lst) / len(temp_lst), 1))
    new_precip = (round(sum(precip_lst) / len(precip_lst), 1))
    new_count = (round(sum(count_lst) / len(count_lst)))

    return [new_temp, new_precip, new_count]


def reset(data: Dict, state: str, future: int) -> None:
    """Reset the dictionary after plotting it"""
    for year in range(2020, future + 1):
        data[state].pop(year)


def graph_this_boring_thing(data: Dict, state: str, future: int) -> None:
    """Create a graph"""

    # Use our helper function to predict data ahead
    data_adder(data, state, future)

    # Create a pandas dataframe
    df = pd.DataFrame.from_dict(data[state], orient='index',
                                columns=['Average_Temp', 'Precipitation', 'Fire_Counts'])

    # Add a year column
    df["Year"] = df.index

    df.plot(x="Year", y="Fire_Counts", kind="line")
    plt.title('A Poisson regression model for a constant event rate in' + ' ' + state)
    plt.show()

    reset(data, state, future)
