"""Main.py"""
from combine_datasets import *
from poisson_regression import *
from negative_binomial_regression import *

data = read_temp_csv_data('data/Annual Temperature_new.csv')
read_precip_csv_data(data, 'data/Annual Precip_new.csv')
read_csv_fire_2019(data, 'data/Historic_GeoMAC_Perimeters_2019.csv')
read_csv_fire_2000_2018(data, 'data/Historic_GeoMAC_Perimeters_Combined_2000-2018.csv')
read_csv_data_long_lang(data, 'data/US_states_long_lang.csv')


def checker(state: str, model: str) -> bool:
    """Check to see whether the state and model are in our project"""
    models = ['PR', 'NBR']
    return state in data.keys() and model in models


def data_visual(state: str, model: str) -> str:
    """Outputting the desired functions"""

    if model == 'PR':
        return poisson_graph(state)
    elif model == 'NBR':
        return negative_binomial_graph(state)
    else:
        return 'Please try again'


def adder(state: str, model: str) -> str:
    """Add the strings together"""
    return state+model    


while True:
    answer = input('Want to see more? y/n')
    if answer == 'y':
        state = input('What state do you want to take a closer look at?')
        model = input('Poisson Regression or Negative Binomial Regression? Type in PR or NBR')
        if checker(state, model):
            print(data_visual(state, model))
            continue
        else:
            print('Enter a valid state and model')
    elif answer == 'n':
        break
    else:
        print('Enter either y or n')
