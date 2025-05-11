import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso, LassoCV
from sklearn.linear_model import LinearRegression, Ridge, RidgeCV, ElasticNet, ElasticNetCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import TimeSeriesSplit
from sklearn.ensemble import StackingRegressor
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge


def load_data(var):
    """
    Load the dataset from a CSV file.
    Input: var - target variable name
    Output: Macro and topics dataframes
    """
    macro = pd.read_csv('../macro.csv',parse_dates=['date'], index_col='date')
    topics = pd.read_csv('../topics.csv',parse_dates=['date'], index_col='date')
    # Align data on topics
    data = macro.join(topics, how='inner')
    # Drop rows with missing values
    data = data.dropna()
    # Define the target variable
    Y = data[var]
    # Use only topic columns as predictors
    X = topics.loc[data.index]

    return data, X, Y

def Lasso_on_Topics(var, space=100):
    """
    Perform Lasso regression on the topics data.
    Search for alpha yielding exactly 5 non-zero coefficients.
    Input: None
    Output: None
    """
    # Load data
    _, X, Y = load_data(var)

    #Standardize predictors
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    alphas = np.logspace(-4, 4, space)
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

def real_time_forecast_indprol1_with_sel_topics(initial_window=120, selected_topics=['Recession', 'Space program', 'Clintons', 'Southeast Asia', 'Oil market']):
    """
    Real-time forecast for industrial production growth (indprol1) using OLS on selected topics."""
    data, X, Y = load_data('indprol1')
    dates = data.index
    forecasts = []
    actuals = []
    for t in range(initial_window, len(Y)):
        # Split into training (0..t-1) and one step ahead test (t)
        print(f"\nReal-time forecast for t={t}")
        X_train = X.iloc[:t]
        Y_train = Y.iloc[:t]
        X_test = X.iloc[t:t+1]
        # Standarize on training data
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        # Fit OLS on selected topics, then forecast
        X_train_selected = sm.add_constant(X_train[selected_topics])
        model = sm.OLS(Y_train, X_train_selected).fit()
        X_test_selected = sm.add_constant(X_test[selected_topics], has_constant='add')
        # Align test columns to the model's parameters (including constant)
        X_test_selected = X_test_selected[model.params.index]
        y_pred = model.predict(X_test_selected).iloc[0]

        forecasts.append(y_pred)
        actuals.append(Y.iloc[t])
    # Evaluate out-of-sample performance
    oos_r2 = r2_score(actuals, forecasts)
    mse = mean_squared_error(actuals, forecasts)
    print(f"\nReal-time Out-of-sample R-squared: {oos_r2:.4f}")
    print(f"MSE is {mse:.4f}")

    #Plot the results
    plt.figure(figsize=(10, 5))
    plt.plot(dates[initial_window:], forecasts, label='Forecasts', color='blue')
    plt.plot(dates[initial_window:], actuals, label='Actuals', color='red')
    plt.title('Real-time Forecast of Industrial Production Growth')
    plt.xlabel('Date')
    plt.ylabel('Industrial Production Growth')
    plt.legend()
    plt.savefig('Forecast_pre_tuned_topics_OLS.png')
    print(f"Real-time forecast of industrial production growth completed.")

def real_time_forecast_indprol1(initial_window=120, alpha = 0.0005336699231206312):
    """
    Expanding window forecast for indprol1 using OLS, Lasso, Ridge, ElasticNet, Kernel Ridge, Gradient Boosting and Stacking.
    Each model is tuned by cross-validation at each step. window size is 240 months.
    X is standardized at each step
    Prints OOS R2 and MSE for each model.
    Input: None
    Output: None
    """
    data, X, Y = load_data('indprol1')
    dates = data.index
    forecasts = {
        'OLS': [],
        'Lasso': [],
        'Ridge': [],
        'ElasticNet': [],
        'KernelRidge': [],
        'GradientBoosting': [],
        'Stacking': []
    }
    actuals = []

    for t in range(initial_window, len(Y)):
        # Split into training (0..t-1) and one step ahead test (t)
        print(f"\nReal-time forecast for t={t}")
        X_train, Y_train = X.iloc[:t], Y.iloc[:t]
        X_test, Y_test = X.iloc[t:t+1], Y.iloc[t:t+1]
        # Standarize on training data
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        # Fit OLS
        ols = LinearRegression().fit(X_train_scaled, Y_train)
        # Fit Models
        lasso = LassoCV(alphas=np.logspace(-4,4,20), cv=5).fit(X_train_scaled, Y_train)
        ridge = RidgeCV(alphas=np.logspace(-4,4,20), cv=5).fit(X_train_scaled, Y_train)
        enet = ElasticNetCV(alphas=np.logspace(-4,1,20), l1_ratio=[0.1,0.5,0.9], cv=5,max_iter=10000).fit(X_train_scaled, Y_train)
        # Kernel Ridge (time alpha via CV)
        # For speed, just use default alpha=1.0
        kr = KernelRidge(kernel='rbf', alpha=1.0).fit(X_train_scaled, Y_train)
        # Gradient Boosting
        gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1).fit(X_train_scaled, Y_train)

        # Predictions
        forecasts['OLS'].append(ols.predict(X_test_scaled)[0])
        forecasts['Lasso'].append(lasso.predict(X_test_scaled)[0])
        forecasts['Ridge'].append(ridge.predict(X_test_scaled)[0])
        forecasts['ElasticNet'].append(enet.predict(X_test_scaled)[0])
        forecasts['KernelRidge'].append(kr.predict(X_test_scaled)[0])
        forecasts['GradientBoosting'].append(gbr.predict(X_test_scaled)[0])
        # Stacking
        base_models = [
            ('ols', ols),
            ('lasso', lasso),
            ('ridge', ridge),
            ('enet', enet),
            ('kr', kr),
            ('gbr', gbr)
        ]

        stacked = StackingRegressor(estimators=base_models, final_estimator=LinearRegression())
        stacked.fit(X_train_scaled, Y_train)
        forecasts['Stacking'].append(stacked.predict(X_test_scaled)[0])
        actuals.append(Y.iloc[t])

    # Compute and print OOS R2 for each model
    for model_name in forecasts.keys():
        r2 = r2_score(actuals, forecasts[model_name])
        mse = mean_squared_error(actuals, forecasts[model_name])
        print(f"\nReal-time Out-of-sample R-squared for {model_name}: {r2:.4f}")
        print(f"Real-time Out-of-sample MSE for {model_name}: {mse:.4f}")



    # # Plot the forecasts vs actuals
    # plt.figure(figsize=(10, 5))
    # plt.plot(dates[initial_window:], forecasts, label='Forecasts', color='blue')
    # plt.plot(dates[initial_window:], actuals, label='Actuals', color='red')
    # plt.title('Real-time Forecast of Industrial Production Growth')
    # plt.xlabel('Date')
    # plt.ylabel('Industrial Production Growth')
    # plt.legend()
    # plt.show()
    # print(f"Real-time forecast of industrial production growth completed.")
    # print(f"Initial window: {initial_window}")
    

    # return dates[initial_window:], forecasts, actuals

def real_time_forecast_indprol1_optimized(initial_window=120):
    data, X, Y = load_data('indprol1')
    dates = data.index
    forecasts = {
        'OLS': [],
        'Lasso': [],
        'Ridge': [],
        'ElasticNet': [],
        'KernelRidge': [],
        'GradientBoosting': [],
        'Stacking': []
    }
    actuals = []

    # Initial training for hyperparameter tuning (if needed)
    X_initial, Y_initial = X.iloc[:initial_window], Y.iloc[:initial_window]
    scaler_initial = StandardScaler()
    X_initial_scaled = scaler_initial.fit_transform(X_initial)

    # Tune Lasso once (or less frequently)
    # Use LassoCV to find the best alpha on the initial data
    initial_lasso_cv = LassoCV(alphas=np.logspace(-4,4,20), cv=5).fit(X_initial_scaled, Y_initial)
    best_lasso_alpha = initial_lasso_cv.alpha_
    print(f"Best Lasso alpha: {best_lasso_alpha}")
    # Tune Ridge and ElasticNet
    initial_ridge_cv = RidgeCV(alphas=np.logspace(-4,4,20), cv=5).fit(X_initial_scaled, Y_initial)
    initial_enet_cv = ElasticNetCV(alphas=np.logspace(-4,1,20), l1_ratio=[0.1,0.5,0.9], cv=5,max_iter=10000).fit(X_initial_scaled, Y_initial)
    initial_ridge_alpha = initial_ridge_cv.alpha_
    initial_enet_alpha = initial_enet_cv.alpha_
    initial_enet_l1_ratio = initial_enet_cv.l1_ratio_

    # Initialize models (without CV for subsequent steps)
    ols = LinearRegression()
    lasso = Lasso(alpha=best_lasso_alpha) # Use the pre-tuned alpha
    ridge = Ridge(alpha=initial_ridge_alpha) # Assuming initial tuning for ridge too
    enet = ElasticNet(alpha=initial_enet_alpha, l1_ratio=initial_enet_l1_ratio)
    kr = KernelRidge(kernel='rbf', alpha=1.0)
    gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1) # Can use warm_start here

    for t in range(initial_window, len(Y)):
        print(f"\nReal-time forecast for t={t}")
        X_train, Y_train = X.iloc[:t], Y.iloc[:t]
        X_test, Y_test = X.iloc[t:t+1], Y.iloc[t:t+1]

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Refit models (no CV)
        ols.fit(X_train_scaled, Y_train)
        lasso.fit(X_train_scaled, Y_train)
        ridge.fit(X_train_scaled, Y_train)
        enet.fit(X_train_scaled, Y_train)
        kr.fit(X_train_scaled, Y_train)
        gbr.fit(X_train_scaled, Y_train) # If using warm_start, adjust n_estimators

        # Predictions
        forecasts['OLS'].append(ols.predict(X_test_scaled)[0])
        forecasts['Lasso'].append(lasso.predict(X_test_scaled)[0])
        forecasts['Ridge'].append(ridge.predict(X_test_scaled)[0])
        forecasts['ElasticNet'].append(enet.predict(X_test_scaled)[0])
        forecasts['KernelRidge'].append(kr.predict(X_test_scaled)[0])
        forecasts['GradientBoosting'].append(gbr.predict(X_test_scaled)[0])

        # Stacking - pass already fitted models or refit if absolutely necessary
        base_models = [
            ('ols', ols),
            ('lasso', lasso),
            ('ridge', ridge),
            ('enet', enet),
            ('kr', kr),
            ('gbr', gbr)
        ]
        stacked = StackingRegressor(estimators=base_models, final_estimator=LinearRegression())
        stacked.fit(X_train_scaled, Y_train) # This will refit base models by default
        forecasts['Stacking'].append(stacked.predict(X_test_scaled)[0])
        actuals.append(Y.iloc[t])

    for model_name in forecasts.keys():
        r2 = r2_score(actuals, forecasts[model_name])
        mse = mean_squared_error(actuals, forecasts[model_name])
        print(f"\nReal-time Out-of-sample R-squared for {model_name}: {r2:.4f}")
        print(f"Real-time Out-of-sample MSE for {model_name}: {mse:.4f}")
        # Plot the forecasts vs actuals
        plt.figure(figsize=(10, 5))
        plt.plot(dates[initial_window:], forecasts[model_name], label='Forecasts', color='blue')
        plt.plot(dates[initial_window:], actuals, label='Actuals', color='red')
        plt.title(f'Real-time Forecast of Industrial Production Growth - {model_name}')
        plt.xlabel('Date')
        plt.ylabel('Industrial Production Growth')
        plt.legend()
        plt.savefig(f'Forecast_{model_name}.png')
    print(f"Real-time forecast of industrial production growth completed.")
    


def real_time_forecast_indprol1_fix_w_lassoCV(window_size=120, alpha = 0.0005336699231206312):
    """
    Forecast industrial production growth (indprol1) using a fixed rolling-window Lasso -> OLS approach.
    Input: None
    Output: None
    """
    data, X, Y = load_data('indprol1')
    dates = data.index
    forecasts, actuals = [], []
    for t in range(window_size, len(Y)):
        # Split into training (rolling window) and one step ahead test (t)
        print(f"\nReal-time forecast for t={t}")
        X_train = X.iloc[t-window_size:t]
        Y_train = Y.iloc[t-window_size:t]
        X_test = X.iloc[t:t+1]
        # Standarize on training data
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        # Fit Lasso
        lasso = LassoCV(cv=5, max_iter=10000)
        lasso.fit(X_train_scaled, Y_train)
        # Select topics with non-zero coefficients
        mask = lasso.coef_ != 0
        selected_topics = X.columns[mask]
        # print(f"Selected topics for t={t}: ", selected_topics.tolist())
        # Fit OLS on selected topics, then forecast
        X_train_selected = sm.add_constant(X_train[selected_topics])
        model = sm.OLS(Y_train, X_train_selected).fit()
        X_test_selected = sm.add_constant(X_test[selected_topics], has_constant='add')
        # Align test columns to the model's parameters (including constant)
        X_test_selected = X_test_selected[model.params.index]
        y_pred = model.predict(X_test_selected).iloc[0]

        forecasts.append(y_pred)
        actuals.append(Y.iloc[t])

    # Evaluate out-of-sample performance
    oos_r2 = r2_score(actuals, forecasts)
    mse = mean_squared_error(actuals, forecasts)
    print(f"\nReal-time Out-of-sample R-squared: {oos_r2:.4f}")
    print(f"Real-time Out-of-sample MSE: {mse:.4f}")

    # Plot the forecasts vs actuals
    plt.figure(figsize=(10, 5))
    plt.plot(dates[window_size:], forecasts, label='Forecasts', color='blue')
    plt.plot(dates[window_size:], actuals, label='Actuals', color='red')
    plt.title('Real-time Forecast of Industrial Production Growth')
    plt.xlabel('Date')
    plt.ylabel('Industrial Production Growth')
    plt.legend()
    plt.show()
    print(f"Real-time forecast of industrial production growth completed.")
    print(f"Window size: {window_size}")
    

    return dates[window_size:], forecasts, actuals

def real_time_forecast_indprol1_fix_w_lasso(window_size=120, alpha = 0.0005336699231206312):
    """
    Forecast industrial production growth (indprol1) using a fixed rolling-window Lasso -> OLS approach.
    Input: None
    Output: None
    """
    data, X, Y = load_data('indprol1')
    dates = data.index
    forecasts, actuals = [], []
    for t in range(window_size, len(Y)):
        # Split into training (rolling window) and one step ahead test (t)
        print(f"\nReal-time forecast for t={t}")
        X_train = X.iloc[t-window_size:t]
        Y_train = Y.iloc[t-window_size:t]
        X_test = X.iloc[t:t+1]
        # Standarize on training data
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        # Fit Lasso
        lasso = Lasso(alpha=alpha, max_iter=10000)
        lasso.fit(X_train_scaled, Y_train)
        # Select topics with non-zero coefficients
        mask = lasso.coef_ != 0
        selected_topics = X.columns[mask]
        # print(f"Selected topics for t={t}: ", selected_topics.tolist())
        # Fit OLS on selected topics, then forecast
        X_train_selected = sm.add_constant(X_train[selected_topics])
        model = sm.OLS(Y_train, X_train_selected).fit()
        X_test_selected = sm.add_constant(X_test[selected_topics], has_constant='add')
        # Align test columns to the model's parameters (including constant)
        X_test_selected = X_test_selected[model.params.index]
        y_pred = model.predict(X_test_selected).iloc[0]

        forecasts.append(y_pred)
        actuals.append(Y.iloc[t])

    # Evaluate out-of-sample performance
    oos_r2 = r2_score(actuals, forecasts)
    mse = mean_squared_error(actuals, forecasts)
    print(f"\nReal-time Out-of-sample R-squared: {oos_r2:.4f}")
    print(f"Real-time Out-of-sample MSE: {mse:.4f}")

    # Plot the forecasts vs actuals
    plt.figure(figsize=(10, 5))
    plt.plot(dates[window_size:], forecasts, label='Forecasts', color='blue')
    plt.plot(dates[window_size:], actuals, label='Actuals', color='red')
    plt.title('Real-time Forecast of Industrial Production Growth')
    plt.xlabel('Date')
    plt.ylabel('Industrial Production Growth')
    plt.legend()
    plt.savefig('Forecast_pre_tuned_alfa_OLS_Fix_window.png')
    print(f"Real-time forecast of industrial production growth completed.")
    print(f"Window size: {window_size}")
    

    return dates[window_size:], forecasts, actuals


def real_time_forecast_indprol1_exp_w(initial_window=120, alpha = 0.0005336699231206312):
    """
    Forecast industrial production growth (indprol1) using an expanding-window Lasso -> OLS approach.
    Input: None
    Output: None
    """
    data, X, Y = load_data('indprol1')
    dates = data.index
    forecasts, actuals = [], []
    for t in range(initial_window, len(Y)):
        # Split into training (0..t-1) and one step ahead test (t)
        X_train = X.iloc[:t]
        Y_train = Y.iloc[:t]
        X_test = X.iloc[t:t+1]
        # Standarize on training data
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        # Fit Lasso
        lasso = Lasso(alpha=alpha, max_iter=10000)
        lasso.fit(X_train_scaled, Y_train)
        # Select topics with non-zero coefficients
        mask = lasso.coef_ != 0
        selected_topics = X.columns[mask]
        # print(f"Selected topics for t={t}: ", selected_topics.tolist())
        # Fit OLS on selected topics, then forecast
        X_train_selected = sm.add_constant(X_train[selected_topics])
        model = sm.OLS(Y_train, X_train_selected).fit()
        X_test_selected = sm.add_constant(X_test[selected_topics], has_constant='add')
        # Align test columns to the model's parameters (including constant)
        X_test_selected = X_test_selected[model.params.index]
        y_pred = model.predict(X_test_selected).iloc[0]

        forecasts.append(y_pred)
        actuals.append(Y.iloc[t])

    # Evaluate out-of-sample performance
    oos_r2 = r2_score(actuals, forecasts)
    mse = mean_squared_error(actuals, forecasts)
    print(f"\nReal-time Out-of-sample R-squared: {oos_r2:.4f}")
    print(f"Real-time Out-of-sample MSE: {mse:.4f}")

    # Plot the forecasts vs actuals
    plt.figure(figsize=(10, 5))
    plt.plot(dates[initial_window:], forecasts, label='Forecasts', color='blue')
    plt.plot(dates[initial_window:], actuals, label='Actuals', color='red')
    plt.title('Real-time Forecast of Industrial Production Growth')
    plt.xlabel('Date')
    plt.ylabel('Industrial Production Growth')
    plt.legend()
    plt.savefig('Forecast_pre_tuned_alfa_OLS.png')
    print(f"Real-time forecast of industrial production growth completed.")
    print(f"Initial window: {initial_window}")

    return dates[initial_window:], forecasts, actuals

def real_time_forecast_indprol1_lassoCV(initial_window=120):
    """
    Forecast industrial production growth (indprol1) using an expanding-window Lasso -> OLS approach.
    Input: None
    Output: None
    """
    data, X, Y = load_data('indprol1')
    dates = data.index
    forecasts, actuals = [], []
    for t in range(initial_window, len(Y)):
        # Split into training (0..t-1) and one step ahead test (t)
        print(f"\nReal-time forecast for t={t}")
        X_train = X.iloc[:t]
        Y_train = Y.iloc[:t]
        X_test = X.iloc[t:t+1]
        # Standarize on training data
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        # Fit Lasso
        lasso_cv = LassoCV(cv = 5, max_iter=10000)
        lasso_cv.fit(X_train_scaled, Y_train)
        best_alpha = lasso_cv.alpha_
        # Select topics with non-zero coefficients
        mask = lasso_cv.coef_ != 0
        selected_topics = X.columns[mask]
        # print(f"Selected topics for t={t}: ", selected_topics.tolist())
        # Fit OLS on selected topics, then forecast
        X_train_selected = sm.add_constant(X_train[selected_topics])
        model = sm.OLS(Y_train, X_train_selected).fit()
        X_test_selected = sm.add_constant(X_test[selected_topics], has_constant='add')
        # Align test columns to the model's parameters (including constant)
        X_test_selected = X_test_selected[model.params.index]
        y_pred = model.predict(X_test_selected).iloc[0]

        forecasts.append(y_pred)
        actuals.append(Y.iloc[t])

    # Evaluate out-of-sample performance
    oos_r2 = r2_score(actuals, forecasts)
    mse = mean_squared_error(actuals, forecasts)
    print(f"\nReal-time Out-of-sample R-squared: {oos_r2:.4f}")
    print(f"Real-time Out-of-sample MSE: {mse:.4f}")

    # Testing AR(1) model
    naive_preds = Y.shift(1).iloc[initial_window:]
    baseline_r2 = r2_score(actuals, naive_preds)
    print(f"\nBaseline AR(1) R-squared: {baseline_r2:.4f}")

    # Plot the forecasts vs actuals
    plt.figure(figsize=(10, 5))
    plt.plot(dates[initial_window:], forecasts, label='Forecasts', color='blue')
    plt.plot(dates[initial_window:], actuals, label='Actuals', color='red')
    plt.title('Real-time Forecast of Industrial Production Growth')
    plt.xlabel('Date')
    plt.ylabel('Industrial Production Growth')
    plt.legend()
    plt.savefig('Forecast_LassoCV_OLS.png')
    print(f"Real-time forecast of industrial production growth completed.")
    print(f"Initial window: {initial_window}")
    

    return dates[initial_window:], forecasts, actuals

# here we start with part d
def Document_Term_Matrix():
    """
    Document-Term Matrix from WSJ Headlines
    Build a document-term matrix using CountVectorizer from sklearn on WSJ headlines.
    Data is loaded from ../articles.pq
    """
    print("\n=== Document-Term Matrix from WSJ Headlines ===")
    # Load the headlines data with dates in display_date column, but index date
    articles = pd.read_parquet('../articles.pq')
    articles['display_date'] = pd.to_datetime(articles['display_date'])
    articles = articles.set_index('display_date', drop=False)
    articles.index.name = 'date'
    # Vectorize headlines to create document-term matrix
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(articles['headline'])
    terms = vectorizer.get_feature_names_out()
    # Create a DataFrame for easier inspection
    dtm_df = pd.DataFrame(dtm.toarray(), index=articles.index, columns=terms)
    # Group by month and sum the counts
    dtm_df = dtm_df.resample('MS').sum()
    print(f"Document-Term Matrix Shape: {dtm_df.shape}")
    
    #save the matix to a CSV file
    dtm_df.to_csv('dtm.csv')
    print("Document-Term Matrix saved to dtm.csv")


# === Part E: Analysis with Counts ===
def load_counts(var):
    """
    Load macro data and raw counts.
    """
    # Load macro and counts data
    macro = pd.read_csv('../macro.csv', parse_dates=['date'], index_col='date')
    counts = pd.read_csv('dtm.csv', index_col='date', parse_dates=True)
    # Align and drop missing values
    data = macro.join(counts, how='inner').dropna()
    Y = data[var]
    X = counts.loc[data.index]
    return data, X, Y


def Lasso_on_Counts(var, space=100):
    """
    Perform Lasso on raw count features for variable var,
    selecting alpha that yields exactly 5 non-zero coefficients.
    Then run OLS on those selected counts.
    """
    data, X, Y = load_counts(var)
    # Standardize predictors
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # Search alphas
    alphas = np.logspace(-4, 4, space)
    selected_alpha = None
    for alpha in alphas:
        lasso = Lasso(alpha=alpha, max_iter=10000)
        lasso.fit(X_scaled, Y)
        if np.sum(lasso.coef_ != 0) == 5:
            selected_alpha = alpha
            break
    if selected_alpha is None:
        raise ValueError(f"No alpha found for 5 non-zero counts for {var}.")
    print(f"Selected alpha for counts ({var}): {selected_alpha}")
    # Fit final Lasso
    lasso = Lasso(alpha=selected_alpha, max_iter=10000)
    lasso.fit(X_scaled, Y)
    mask = lasso.coef_ != 0
    selected_terms = X.columns[mask]
    print("Selected count terms:", selected_terms.tolist())
    # OLS on selected terms
    X_sel = sm.add_constant(X[selected_terms])
    ols = sm.OLS(Y, X_sel).fit()
    print("\nOLS Summary for counts:")
    print(ols.summary())
    print(f"R-squared (counts) for {var}: {ols.rsquared:.4f}")


def part_e():
    """Part E: Repeat Analysis with Counts"""
    # Define variables as in part b
    variables = ['mret', 'vol', 'indpro', 'indprol1']
    data, _, _ = load_data(variables[0])
    indvol_vars = [col for col in data.columns if col.endswith('_vol')]
    variables.extend(indvol_vars)
    print("\n=== Part E: Lasso and OLS on Raw Counts ===")
    for var in variables:
        print(f"\n--- {var} ---")
        try:
            Lasso_on_Counts(var)
        except ValueError as e:
            # Handle cases where no alpha is found
            try:
                Lasso_on_Counts(var, space=1000)
            except ValueError as e:
                print(f"Skipping {var}: {e}")

def part_f_forecast_indprol1_lassoCV(initial_window=120,alpha=0.00150):
    """
    Forecast industrial production growth (indprol1) using an expanding-window Lasso -> OLS approach.
    Input: None
    Output: None
    """
    data, X, Y = load_counts('indprol1')
    dates = data.index
    forecasts, actuals = [], []
    for t in range(initial_window, len(Y)):
        # Split into training (0..t-1) and one step ahead test (t)
        print(f"\nReal-time forecast for t={t}")
        X_train = X.iloc[:t]
        Y_train = Y.iloc[:t]
        X_test = X.iloc[t:t+1]
        # Standarize on training data
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        # Fit Lasso
        lasso_cv = Lasso(alpha=alpha, max_iter=10000)
        lasso_cv.fit(X_train_scaled, Y_train)
        # best_alpha = lasso_cv.alpha_
        # Select topics with non-zero coefficients
        mask = lasso_cv.coef_ != 0
        selected_topics = X.columns[mask]
        # print(f"Selected topics for t={t}: ", selected_topics.tolist())
        # Fit OLS on selected topics, then forecast
        X_train_selected = sm.add_constant(X_train[selected_topics])
        model = sm.OLS(Y_train, X_train_selected).fit()
        X_test_selected = sm.add_constant(X_test[selected_topics], has_constant='add')
        # Align test columns to the model's parameters (including constant)
        X_test_selected = X_test_selected[model.params.index]
        y_pred = model.predict(X_test_selected).iloc[0]

        forecasts.append(y_pred)
        actuals.append(Y.iloc[t])

    # Evaluate out-of-sample performance
    oos_r2 = r2_score(actuals, forecasts)
    mse = mean_squared_error(actuals, forecasts)
    print(f"\nReal-time Out-of-sample R-squared: {oos_r2:.4f}")
    print(f"Real-time Out-of-sample MSE: {mse:.4f}")

    # Testing AR(1) model
    naive_preds = Y.shift(1).iloc[initial_window:]
    baseline_r2 = r2_score(actuals, naive_preds)
    print(f"\nBaseline AR(1) R-squared: {baseline_r2:.4f}")

    # Plot the forecasts vs actuals
    plt.figure(figsize=(10, 5))
    plt.plot(dates[initial_window:], forecasts, label='Forecasts', color='blue')
    plt.plot(dates[initial_window:], actuals, label='Actuals', color='red')
    plt.title('Real-time Forecast of Industrial Production Growth')
    plt.xlabel('Date')
    plt.ylabel('Industrial Production Growth')
    plt.legend()
    plt.savefig('Forecast_LassoCV_OLS_Word_Count.png')
    print(f"Real-time forecast of industrial production growth completed.")
    print(f"Initial window: {initial_window}")
    

    return dates[initial_window:], forecasts, actuals


# === Part G: TF-IDF Analysis ===
def load_tfidf(var):
    """
    Load macro data and TF-IDF-transformed counts.
    """
    macro = pd.read_csv('../macro.csv', parse_dates=['date'], index_col='date')
    counts = pd.read_csv('dtm.csv', index_col='date', parse_dates=True)
    # Transform counts to TF-IDF
    transformer = TfidfTransformer()
    X_tfidf = transformer.fit_transform(counts.values)
    terms = counts.columns
    tfidf_df = pd.DataFrame(X_tfidf.toarray(), index=counts.index, columns=terms)
    # Align with macro and drop missing
    data, _, _ = load_data(var)  # to get macro alignment logic
    data = macro.join(tfidf_df, how='inner').dropna()
    Y = data[var]
    X = tfidf_df.loc[data.index]
    return data, X, Y

def Lasso_on_Tfidf(var, space=100):
    """
    Perform Lasso on TF-IDF features for variable var,
    selecting alpha that yields exactly 5 non-zero coefficients.
    Then run OLS on those selected TF-IDF features.
    """
    data, X, Y = load_tfidf(var)
    # Standardize predictors
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # Search alphas
    alphas = np.logspace(-4, 4, space)
    selected_alpha = None
    for alpha in alphas:
        lasso = Lasso(alpha=alpha, max_iter=10000)
        lasso.fit(X_scaled, Y)
        if np.sum(lasso.coef_ != 0) == 5:
            selected_alpha = alpha
            break
    if selected_alpha is None:
        raise ValueError(f"No alpha found for 5 non-zero TF-IDF features for {var}.")
    print(f"Selected alpha for TF-IDF ({var}): {selected_alpha}")
    # Fit final Lasso
    lasso = Lasso(alpha=selected_alpha, max_iter=10000)
    lasso.fit(X_scaled, Y)
    mask = lasso.coef_ != 0
    selected_terms = X.columns[mask]
    print("Selected TF-IDF terms:", selected_terms.tolist())
    # OLS on selected features
    X_sel = sm.add_constant(X[selected_terms])
    ols = sm.OLS(Y, X_sel).fit()
    print("\nOLS Summary for TF-IDF:")
    print(ols.summary())
    print(f"R-squared (TF-IDF) for {var}: {ols.rsquared:.4f}")

def part_g():
    """
    Part G: TF-IDF Analysis
    Convert raw counts into TF-IDF and repeat the analysis from part (e).
    """
    print("\n=== Part G: TF-IDF Analysis ===")
    # Define variables similarly to part_e
    variables = ['mret', 'vol', 'indpro', 'indprol1']
    data, _, _ = load_data(variables[0])
    indvol_vars = [col for col in data.columns if col.endswith('_vol')]
    variables.extend(indvol_vars)
    for var in variables:
        print(f"\n--- {var} ---")
        try:
            Lasso_on_Tfidf(var)
        except ValueError as e:
            # Handle cases where no alpha is found
            try:
                Lasso_on_Tfidf(var, space=1000)
            except ValueError as e:
                print(f"Skipping {var}: {e}")

def test_load_data(var):
    """
    Test the load_data function.
    Input: None
    Output: None
    """
    data, X, _ = load_data(var)
    assert isinstance(data, pd.DataFrame), "Data should be a DataFrame"
    assert isinstance(X, pd.DataFrame), "X should be a DataFrame"
    assert not data.empty, "Data should not be empty"
    assert not X.empty, "X should not be empty"
    print("load_data() test passed.")
    print("Data:")
    print(data.head())
    print("\nX:")
    print(X.head())

def part_a():
    """Lasso and OLS on Topics"""
    # List of macro outcomes for regression
    var = 'mret'
    print(f"\n=== Lasso and OLS for {var} ===")
    try:
        Lasso_on_Topics(var)
    except ValueError as e:
        print(f"Skipping variable {var}: {e}")

def part_b():
    # List of macro outcomes for regression
    variables = ['mret', 'vol', 'indpro', 'indprol1']
    # Load data for the first variable to identify industry volatility columns
    data, _, _ = load_data(variables[0])
    # Find all columns ending with '_vol' as additional outcomes
    indvol_vars = [col for col in data.columns if col.endswith('_vol')]
    variables.extend(indvol_vars)

    for var in variables:
        print(f"\n=== Lasso and OLS for {var} ===")
        try:
            Lasso_on_Topics(var)
        except ValueError as e:
            try:
                Lasso_on_Topics(var, space=1000)
            except ValueError as e:
                print(f"Skipping variable {var}: {e}")

def part_c():
    """Part C: real-time forecast of industrial production growth"""
    print("\n=== Real-time forecast of industrial production growth ===")
    real_time_forecast_indprol1_with_sel_topics()

def part_d():
    Document_Term_Matrix()

if __name__ == "__main__":
    # part_d()
    # part_e()
    # counts = pd.read_csv('dtm.csv', index_col=0, parse_dates=True)
    # print(counts.head())
    # real_time_forecast_indprol1_optimized()
    # real_time_forecast_indprol1_fix_w_lasso()
    # real_time_forecast_indprol1_with_sel_topics()
    # real_time_forecast_indprol1_lassoCV()
    part_f_forecast_indprol1_lassoCV()
    # part_g()