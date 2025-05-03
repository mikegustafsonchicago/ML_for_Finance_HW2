import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

def load_data():
    """
    Load the dataset from a CSV file.
    Input: None
    Output: Macro and topics dataframes
    """
    macro = pd.read_csv('../macro.csv',parse_dates=['date'], index_col='date')
    topics = pd.read_csv('../topics.csv',parse_dates=['date'], index_col='date')
    # Align data on topics
    data = macro.join(topics, how='inner')
    # Drop rows with missing values
    data = data.dropna()
    # Define the target variable
    Y = data['mret']
    # Use only topic columns as predictors
    X = topics.loc[data.index]

    return data, X, Y

def Lasso_on_Topics():
    """
    Perform Lasso regression on the topics data.
    Search for alpha yielding exactly 5 non-zero coefficients.
    Input: None
    Output: None
    """
    # Load data
    _, X, Y = load_data()

    #Standardize predictors
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    alphas = np.logspace(-4, 4, 100)
    selected_alpha = None
    for alpha in alphas:
        lasso = Lasso(alpha=alpha, max_iter=10000)
        lasso.fit(X_scaled, Y)
        nonzero_count = np.sum(lasso.coef_ != 0)
        if nonzero_count == 5:
            selected_alpha = alpha
            break
    
    if selected_alpha is None:
        raise ValueError("No alpha found that yields exactly 5 non-zero coefficients.")
    
    print(f"Selected alpha: {selected_alpha}")

    # Fit Lasso model with the selected alpha
    lasso = Lasso(alpha=selected_alpha, max_iter=10000)
    lasso.fit(X_scaled, Y)
    mask = lasso.coef_ != 0
    selected_topics = X.columns[mask]
    print("Selected topics: ", selected_topics.tolist())

    # Run OLS on the selected topics
    X_selected = sm.add_constant(X[selected_topics])
    ols_model = sm.OLS(Y, X_selected).fit()
    print("\nOLS Summary:")
    print(ols_model.summary())
    print(f"\nR-squared: {ols_model.rsquared:.4f}")

def test_load_data():
    """
    Test the load_data function.
    Input: None
    Output: None
    """
    data, X, _ = load_data()
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
    Lasso_on_Topics()