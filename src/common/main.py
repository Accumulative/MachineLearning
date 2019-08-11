
# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Importing the dataset
def import_dataset(file_path, split = 0.2, to_encode = None):
    dataset = pd.read_csv(file_path)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values

    if to_encode is not None:
        # Encoding categorical data
        labelencoder = LabelEncoder()
        X[:, to_encode] = labelencoder.fit_transform(X[:, to_encode])
        onehotencoder = OneHotEncoder(categorical_features=[to_encode])
        X = onehotencoder.fit_transform(X).toarray()

        # Avoiding the Dummy Variable Trap
        X = X[:, 1:]

    # Splitting the dataset into the Training set and Test set
    # returns X_train, X_test, y_train, y_test =
    return train_test_split(X, y, test_size = split, random_state = 0)

    # Feature Scaling
    """from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)
    sc_y = StandardScaler()
    y_train = sc_y.fit_transform(y_train.reshape(-1,1))"""