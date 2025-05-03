import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
import statsmodels.api as sm

def load_data():
    """
    Load the dataset from a CSV file.
    Input: None
    Output: Macro and topics dataframes
    """
    macro = pd.read_csv('../macro.csv',parse_dates=['date'], index_col='date')
    topics = pd.read_csv('../topics.csv',parse_dates=['date'], index_col='date')
    # Align data on dates
    data = macro.join(topics, how='inner')
    # Drop rows with missing values
    data = data.dropna()
    # Use only topic columns as predictors
    X = topics.loc[data.index]

    return data, X

def test_load_data():
    """
    Test the load_data function.
    Input: None
    Output: None
    """
    data, X = load_data()
    assert isinstance(data, pd.DataFrame), "Data should be a DataFrame"
    assert isinstance(X, pd.DataFrame), "X should be a DataFrame"
    assert not data.empty, "Data should not be empty"
    assert not X.empty, "X should not be empty"
    print("load_data() test passed.")
    print("Data:")
    print(data.head())
    print("\nX:")
    print(X.head())


if __name__ == "__main__":
    # Run the test
    test_load_data()