# CSC110 Final Project

Predicting future wildfire counts with a poisson regression model and a negative binomial regression model. 

## Our Goal

The overall objective for this project was to predict the wildfire count for any state in the U.S. in any given year using a poisson regression model and a negative binomial regression model. 

The reason we created two models was because a Poisson distribution assumes that the mean and the variance within the distribution are the same while a negative binomial distribution adjusts the variance independently from the mean.  

## Requirements

### Testing and Code Checking
- hypothesis
- pytest
- python-ta

### Graphics and Data Visualization
- Pandas
- Patsy
- Numpy
- Statsmodels.api
- Matplotlib.pyplot
- Typing

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

## Copyright and License Information

### Source Code

The source code is Copyright (c) 2020 Mohamed Al-Fahim, Kevin Quinn, An Nguyen-Trinh, and Alexander Shchokin, and licensed under the MIT License.

### Datasets

TODO
