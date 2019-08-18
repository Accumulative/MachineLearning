# Multiple Linear Regression

# Importing the libraries
import numpy as np

from src.common import main, visualize
from sklearn.linear_model import LinearRegression
import os

from src.common.main import backward_elimination

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '50_Startups.csv')

def execute():
    [X_train, X_test, y_train, y_test], columns, _, _ = main.import_dataset(filename, 0.3, 3)

    # Fitting Simple Linear Regression to the Training set
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    predictions = regressor.predict(X_test)

    return visualize.plot(X_train, y_train, X_test, y_test, predictions, columns)

def backward_propagation(sl):
    _, columns, X, y = main.import_dataset(filename, 0.3, 3)

    return backward_elimination(X, y, columns, sl)

