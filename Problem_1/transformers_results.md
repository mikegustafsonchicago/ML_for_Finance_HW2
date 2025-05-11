--- mret ---
Selected alpha for TF-IDF (mret): 0.00916140245713852
Selected TF-IDF terms: ['1929', 'define', 'doomed', 'paribas', 'protections']

OLS Summary for TF-IDF:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   mret   R-squared:                       0.196
Model:                            OLS   Adj. R-squared:                  0.186
Method:                 Least Squares   F-statistic:                     19.55
Date:                Fri, 09 May 2025   Prob (F-statistic):           1.92e-17
Time:                        22:27:42   Log-Likelihood:                 748.43
No. Observations:                 408   AIC:                            -1485.
Df Residuals:                     402   BIC:                            -1461.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
const           0.0123      0.002      6.310      0.000       0.008       0.016
1929           -1.0711      0.846     -1.266      0.206      -2.734       0.592
define         -1.7571      0.519     -3.386      0.001      -2.777      -0.737
doomed         -1.7668      0.469     -3.769      0.000      -2.688      -0.845
paribas        -1.2793      0.454     -2.821      0.005      -2.171      -0.388
protections    -1.3905      0.440     -3.157      0.002      -2.256      -0.525
==============================================================================
Omnibus:                       25.420   Durbin-Watson:                   2.070
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               38.140
Skew:                          -0.456   Prob(JB):                     5.22e-09
Kurtosis:                       4.188   Cond. No.                         473.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (TF-IDF) for mret: 0.1956

--- vol ---
Skipping vol: No alpha found for 5 non-zero TF-IDF features for vol.

--- indpro ---
Selected alpha for TF-IDF (indpro): 0.0018761746914391195
Selected TF-IDF terms: ['alaskans', 'drafters', 'farai', 'osborn', 'palin']

OLS Summary for TF-IDF:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 indpro   R-squared:                       0.266
Model:                            OLS   Adj. R-squared:                  0.263
Method:                 Least Squares   F-statistic:                     73.57
Date:                Fri, 09 May 2025   Prob (F-statistic):           5.57e-28
Time:                        22:58:43   Log-Likelihood:                 1565.1
No. Observations:                 408   AIC:                            -3124.
Df Residuals:                     405   BIC:                            -3112.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0019      0.000      7.432      0.000       0.001       0.002
alaskans      -0.1895      0.021     -8.904      0.000      -0.231      -0.148
drafters      -0.1895      0.021     -8.904      0.000      -0.231      -0.148
farai         -0.1895      0.021     -8.904      0.000      -0.231      -0.148
osborn        -0.3830      0.046     -8.275      0.000      -0.474      -0.292
palin         -0.1895      0.021     -8.904      0.000      -0.231      -0.148
==============================================================================
Omnibus:                        8.271   Durbin-Watson:                   1.686
Prob(Omnibus):                  0.016   Jarque-Bera (JB):               12.211
Skew:                          -0.124   Prob(JB):                      0.00223
Kurtosis:                       3.811   Cond. No.                     2.01e+45
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 1.01e-88. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
R-squared (TF-IDF) for indpro: 0.2665

--- indprol1 ---
Selected alpha for TF-IDF (indprol1): 0.001589282865622978
Selected TF-IDF terms: ['insights', 'mga', 'osborn', 'schaeffler', 'tennille']

OLS Summary for TF-IDF:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               indprol1   R-squared:                       0.267
Model:                            OLS   Adj. R-squared:                  0.259
Method:                 Least Squares   F-statistic:                     36.65
Date:                Fri, 09 May 2025   Prob (F-statistic):           3.89e-26
Time:                        23:00:22   Log-Likelihood:                 1569.4
No. Observations:                 408   AIC:                            -3129.
Df Residuals:                     403   BIC:                            -3109.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0020      0.000      7.826      0.000       0.002       0.003
insights      -0.1643      0.031     -5.363      0.000      -0.225      -0.104
mga           -0.0678      0.047     -1.458      0.146      -0.159       0.024
osborn        -0.1370      0.061     -2.253      0.025      -0.256      -0.017
schaeffler    -0.0678      0.047     -1.458      0.146      -0.159       0.024
tennille      -0.1438      0.040     -3.582      0.000      -0.223      -0.065
==============================================================================
Omnibus:                       18.874   Durbin-Watson:                   1.780
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               33.269
Skew:                          -0.292   Prob(JB):                     5.97e-08
Kurtosis:                       4.271   Cond. No.                     6.50e+16
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 9.67e-32. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
R-squared (TF-IDF) for indprol1: 0.2667
