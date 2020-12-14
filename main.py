"""Main.py"""
from combine_datasets import *
from poisson_regression import *
from negative_binomial_regression import *
from map_visual import map_values

data = read_temp_csv_data('data/Annual_Temperature.csv')
read_precip_csv_data(data, 'data/Annual_Precip.csv')
read_csv_fire_2019(data, 'data/Historic_GeoMAC_Perimeters_2019.csv')
read_csv_fire_2000_2018(data, 'data/Historic_GeoMAC_Perimeters_Combined_2000-2018.csv')
long_lang_data = read_csv_data_long_lang('data/US_states_long_lang.csv')


def checker(state: str) -> bool:
    """Check to see whether the state and model are in our project"""
    return state in data.keys()


# STATE_FOCUS_MESSAGE = 'What state do you want to take a closer look at? If you do not want to, type n.'
#
#
# state = input(STATE_FOCUS_MESSAGE)
# if checker(state):
#     while checker(state):
#         model = input('Poisson Regression or Negative Binomial Regression? Type in pr or nbr.')
#         if model == 'pr':
#             poisson_graph(state)
#         elif model == 'nbr':
#             negative_binomial_graph(state)
#         else:
#             print('Invalid model. Please try again.')
#
#         state = input(STATE_FOCUS_MESSAGE)
#         continue
# else:
#     print('Thank You!')
