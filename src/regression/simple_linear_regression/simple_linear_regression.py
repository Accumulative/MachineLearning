# Simple Linear Regression

# Importing the libraries
from src.common import main, visualize
from sklearn.linear_model import LinearRegression
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Salary_Data.csv')

def execute():
    [X_train, X_test, y_train, y_test], columns, X, y = main.import_dataset(filename, 1/3)

    # Fitting Simple Linear Regression to the Training set
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    predictions = regressor.predict(X_test)

    return visualize.plot(X_train, y_train, X_test, y_test, predictions, columns)

