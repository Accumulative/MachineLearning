
# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Importing the dataset
def import_dataset(file_path, split = 0.2, to_encode = None):
    dataset = pd.read_csv(file_path)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    columns = dataset.columns.values.tolist()

    if to_encode is not None:
        # Encoding categorical data
        labelencoder = LabelEncoder()
        X[:, to_encode] = labelencoder.fit_transform(X[:, to_encode])
        onehotencoder = OneHotEncoder(categorical_features=[to_encode])
        X = onehotencoder.fit_transform(X).toarray()

        # Avoiding the Dummy Variable Trap
        X = X[:, 1:]
        columns = columns[:to_encode] + columns[to_encode+1:]
        columns = ['Dummy_variable_'+str(i) for i in range(X.shape[1] - len(columns) + 1)] + columns


    # Splitting the dataset into the Training set and Test set
    # returns X_train, X_test, y_train, y_test =
    return train_test_split(X, y, test_size = split, random_state = 0), columns, X, y


import statsmodels.api as sm

def backward_elimination(x, y, columns, SL = 0.1):
    x = sm.add_constant(x)
    columns = ['const'] + columns
    result = []
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVarIndex = np.argmax(regressor_OLS.pvalues)
        if regressor_OLS.pvalues[maxVarIndex] > SL:
            x = np.delete(x, maxVarIndex, 1)
            result.append({'name': columns[maxVarIndex], 'pval': regressor_OLS.pvalues[maxVarIndex]})
            columns = np.delete(columns, maxVarIndex)

    return result