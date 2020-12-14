# CSC110 Final Project

Predicting future wildfire counts with a poisson regression model and a negative binomial regression model. 

## Our Goal

The overall objective for this project was to predict the wildfire count for any state in the U.S. in any given year using a poisson regression model and a negative binomial regression model. 

The reason we created two models was because a Poisson distribution assumes that the mean and the variance within the distribution are the same while a negative binomial distribution adjusts the variance independently from the mean.  

## Requirements

Python 3.8+

### Testing and Code Checking
- hypothesis
- pytest
- python-ta

### Graphics and Data Visualization
- Pandas
- Patsy
- Numpy
- statsmodels
- matplotlib

## Poisson Regression - how to
1. Run the poisson_regression.py file. 
2. To see the predictions for wildfire counts for any given year, type the following into the Python Console:

```python
poisson_graph('Alabama')  
```

In the above case it would output a graph for Alabama with predicted counts vs. actual counts but you can put any state in the U.S. except Hawaii, American Samoa, District of Columbia, Guam, Puerto Rico and the Virgin Islands.

## Future Prediction Poisson Regression
1. Run the future_predictor.py file.
2. To see the predictions for wildfire counts in the future assuming that there is a constant event rate, type the following into the Python Console:

```python
constant_graph('Alabama', 2040)
```

In the above case it would output a graph for Alabama for wildfire counts up to the year that was inputted (2040) but you can put any state in the U.S. except Hawaii, American Samoa, District of Columbia, Guam, Puerto Rico and the Virgin Islands, and you can input any year.

## Negative Binomial Regression 
1. Run the negative_binomial_regression.py file. 
2. To see the predictions for wildfire counts for any given year in the dataset, type the following into the Python Console: 

```python
negative_binomial_graph('Alabama')
```

In the above case it would output a graph for Alabama with actual counts vs. predicted counts but you can put any state in the U.S. except Hawaii, American Samoa, District of Columbia, Guam, Puerto Rico and the Virgin Islands.

## Interpretation of PR and NBR

### Poisson Regression

The goal of this regression was to track the trend in the wildfire counts under the assumption that the average wild fire counts is equivalent to the variance of our data. Under this assumption, a graph was displayed graphing the predicted counts versus the actual counts. 

### Negative Binomial Regression

The goal of this regression was to track the trend in the wildfire counts under the assumption that the average wild fire counts is not equivalent to the variance of our data. Under this assumption, a graph was displayed graphing the predicted counts versus the actual counts. 

### How do we analyze the data?

The regression models chosen are used for count based data and we chose these in hopes of seeing trends that are explainable and easy to utilize. From our results it may give a good idea of an overall trend for how many wildfires to expect in the future.

## Copyright and License Information

### Source Code

The source code is Copyright (c) 2020 Mohamed Al-Fahim, Kevin Quinn, An Nguyen-Trinh, and Alexander Shchokin, and licensed under the MIT License.

### Datasets

- Annual Precip.csv is based off data from https://www.ncdc.noaa.gov/cag/statewide/time-series/2/pcp/ann/11/2000-2019?base_prd=true&begbaseyear=1901&endbaseyear=2000
- Annual Temperature.csv is based off data from https://www.ncdc.noaa.gov/cag/statewide/time-series/2/tavg/12/12/2000-2019?base_prd=true&begbaseyear=1901&endbaseyear=2000
- Historic_GeoMAC_Perimeters_Combined_2000-2018.csv is based off data from https://data-nifc.opendata.arcgis.com/datasets/historic-geomac-perimeters-combined-2000-2018/data
- Historic_GeoMAC_Perimeters_2019.csv is based off data from https://data-nifc.opendata.arcgis.com/datasets/historic-geomac-perimeters-2019/data
