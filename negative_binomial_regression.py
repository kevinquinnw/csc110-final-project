"""
This file is Copyright (c) 2020 Mohamed Al-Fahim, Kevin Quinn, An Nguyen-Trinh, and Alexander Shchokin.
"""

from typing import Dict

import pandas as pd
from patsy import dmatrices
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from combine_datasets import *


def negative_binomial_graph(data: Dict, state: str) -> None:
    """A function to display a negative binomial regression model graphically"""
    
        # Preloading the data in
    data = read_temp_csv_data('data/Annual Temperature_new.csv')
    read_precip_csv_data(data, 'data/Annual Precip_new.csv')
    read_csv_fire_2019(data, 'data/Historic_GeoMAC_Perimeters_2019.csv')
    read_csv_fire_2000_2018(data, 'data/Historic_GeoMAC_Perimeters_Combined_2000-2018.csv')

    pd.options.mode.chained_assignment = None

    # First, creating a pandas dataframe for our data
    df = pd.DataFrame.from_dict(data[state], orient='index', columns=['Average_Temp', 'Precipitation', 'Fire_Counts'])

    # Creating a regression variable for the Year
    df['Year'] = df.index

    # Creates a random sample from a uniform distribution
    rand_samples = np.random.rand(len(df)) < 0.8

    # Training dataset
    df_train = df[rand_samples]

    # Testing dataset
    df_test = df[~rand_samples]

    # Regression expression in Patsy Notation
    equation = """Fire_Counts ~ Average_Temp + Precipitation + Year"""

    # Creating matrices for the training datasets w/ Patsy
    y_train, x_train = dmatrices(equation, df_train, return_type='dataframe')

    # Creating matrices for the testing datasets w/ Patsy
    y_test, x_test = dmatrices(equation, df_test, return_type='dataframe')

    # Using statsmodels GLM class to train the regression
    poisson_results = sm.GLM(y_train, x_train, family=sm.families.Poisson()).fit()

    # Adding the Lambda vector as a new column in our df
    df_train['Count_Mean'] = poisson_results.mu

    # Add a column to store values of dependent variable
    df_train['OLS_Variable'] = df_train.apply(
        lambda x: ((x['Fire_Counts'] - x['Count_Mean']) ** 2 - x['Count_Mean']) / x['Count_Mean'], axis=1)

    # Model specification for OSL Regression
    ols_equation = """OLS_Variable ~ Count_Mean - 1"""

    ols_reg_results = smf.ols(ols_equation, df_train).fit()

    nb2_training_results = sm.GLM(y_train, x_train,
                                  family=sm.families.NegativeBinomial(alpha=ols_reg_results.params[0])).fit()

    nb2_predictions = nb2_training_results.get_prediction(x_test)

    predictions_summary_frame = nb2_predictions.summary_frame()

    predicted_counts = predictions_summary_frame['mean']
    actual_counts = y_test['Fire_Counts']
    fig = plt.figure()
    fig.suptitle(f'Predicted versus actual wildfire counts in {state}')
    predicted, = plt.plot(x_test.index, predicted_counts, 'go-', label='Predicted counts')
    actual, = plt.plot(x_test.index, actual_counts, 'ro-', label='Actual counts')
    plt.legend(handles=[predicted, actual])
    plt.show()
    
    return 'A new tab has been opened with the regression you chose.'
