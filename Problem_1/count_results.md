
--- mret ---
Selected alpha for counts (mret): 0.009862658461312821
Selected count terms: ['1929', 'anastasio', 'define', 'doomed', 'paribas']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   mret   R-squared:                       0.174
Model:                            OLS   Adj. R-squared:                  0.166
Method:                 Least Squares   F-statistic:                     21.29
Date:                Thu, 08 May 2025   Prob (F-statistic):           6.07e-16
Time:                        17:34:37   Log-Likelihood:                 743.12
No. Observations:                 408   AIC:                            -1476.
Df Residuals:                     403   BIC:                            -1456.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0119      0.002      6.056      0.000       0.008       0.016
1929          -0.0281      0.028     -1.009      0.314      -0.083       0.027
anastasio     -0.0281      0.028     -1.009      0.314      -0.083       0.027
define        -0.1468      0.028     -5.258      0.000      -0.202      -0.092
doomed        -0.1043      0.028     -3.734      0.000      -0.159      -0.049
paribas       -0.0783      0.028     -2.802      0.005      -0.133      -0.023
==============================================================================
Omnibus:                       24.809   Durbin-Watson:                   2.059
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               35.377
Skew:                          -0.466   Prob(JB):                     2.08e-08
Kurtosis:                       4.102   Cond. No.                     1.21e+15
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 2.77e-28. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
R-squared (counts) for mret: 0.1744

--- vol ---
Selected alpha for counts (vol): 0.09770099572992257
Selected count terms: ['crisis', 'currents', 'deals', 'makers', 'tennille']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    vol   R-squared:                       0.240
Model:                            OLS   Adj. R-squared:                  0.231
Method:                 Least Squares   F-statistic:                     25.38
Date:                Thu, 08 May 2025   Prob (F-statistic):           2.91e-22
Time:                        17:36:37   Log-Likelihood:                -184.01
No. Observations:                 408   AIC:                             380.0
Df Residuals:                     402   BIC:                             404.1
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -2.1348      0.023    -93.536      0.000      -2.180      -2.090
crisis         0.1346      0.031      4.285      0.000       0.073       0.196
currents       0.3860      0.135      2.856      0.005       0.120       0.652
deals          0.0941      0.035      2.661      0.008       0.025       0.164
makers         0.0245      0.036      0.687      0.493      -0.046       0.095
tennille       0.4747      0.174      2.735      0.007       0.133       0.816
==============================================================================
Omnibus:                       45.479   Durbin-Watson:                   0.380
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               62.575
Skew:                           0.785   Prob(JB):                     2.58e-14
Kurtosis:                       4.103   Cond. No.                         18.2
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for vol: 0.2400

--- indpro ---
Selected alpha for counts (indpro): 0.0020573743134329114
Selected count terms: ['alaskans', 'bios', 'cam', 'osborn', 'palin']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 indpro   R-squared:                       0.267
Model:                            OLS   Adj. R-squared:                  0.264
Method:                 Least Squares   F-statistic:                     73.85
Date:                Thu, 08 May 2025   Prob (F-statistic):           4.52e-28
Time:                        17:37:31   Log-Likelihood:                 1565.3
No. Observations:                 408   AIC:                            -3125.
Df Residuals:                     405   BIC:                            -3112.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0019      0.000      7.438      0.000       0.001       0.002
alaskans      -0.0117      0.001     -8.909      0.000      -0.014      -0.009
bios          -0.0117      0.001     -8.909      0.000      -0.014      -0.009
cam           -0.0117      0.001     -8.909      0.000      -0.014      -0.009
osborn        -0.0252      0.003     -8.304      0.000      -0.031      -0.019
palin         -0.0117      0.001     -8.909      0.000      -0.014      -0.009
==============================================================================
Omnibus:                        8.364   Durbin-Watson:                   1.687
Prob(Omnibus):                  0.015   Jarque-Bera (JB):               12.376
Skew:                          -0.126   Prob(JB):                      0.00205
Kurtosis:                       3.815   Cond. No.                     1.57e+44
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 1.65e-86. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
R-squared (counts) for indpro: 0.2672

--- indprol1 ---
Selected alpha for counts (indprol1): 0.0015037553212997384
Selected count terms: ['aston', 'insights', 'mga', 'osborn', 'tennille']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               indprol1   R-squared:                       0.266
Model:                            OLS   Adj. R-squared:                  0.259
Method:                 Least Squares   F-statistic:                     36.59
Date:                Thu, 08 May 2025   Prob (F-statistic):           4.24e-26
Time:                        17:38:17   Log-Likelihood:                 1569.4
No. Observations:                 408   AIC:                            -3129.
Df Residuals:                     403   BIC:                            -3109.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0020      0.000      7.829      0.000       0.002       0.003
aston         -0.0057      0.003     -1.646      0.101      -0.013       0.001
insights      -0.0092      0.002     -5.415      0.000      -0.013      -0.006
mga           -0.0057      0.003     -1.646      0.101      -0.013       0.001
osborn        -0.0091      0.004     -2.323      0.021      -0.017      -0.001
tennille      -0.0079      0.002     -3.546      0.000      -0.012      -0.004
==============================================================================
Omnibus:                       18.060   Durbin-Watson:                   1.779
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               31.720
Skew:                          -0.279   Prob(JB):                     1.29e-07
Kurtosis:                       4.247   Cond. No.                     3.81e+15
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 2.81e-29. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
R-squared (counts) for indprol1: 0.2664

--- Agric_vol ---
Selected alpha for counts (Agric_vol): 0.18504070195423022
Selected count terms: ['08', 'banking', 'insight', 'jacky', 'jones']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Agric_vol   R-squared:                       0.348
Model:                            OLS   Adj. R-squared:                  0.340
Method:                 Least Squares   F-statistic:                     42.96
Date:                Thu, 08 May 2025   Prob (F-statistic):           1.92e-35
Time:                        18:24:01   Log-Likelihood:                -406.42
No. Observations:                 408   AIC:                             824.8
Df Residuals:                     402   BIC:                             848.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0730      0.040      1.827      0.068      -0.006       0.151
08             0.6554      0.146      4.489      0.000       0.368       0.943
banking       -0.3970      0.083     -4.802      0.000      -0.559      -0.234
insight        0.4186      0.094      4.444      0.000       0.233       0.604
jacky         -1.9807      0.390     -5.075      0.000      -2.748      -1.213
jones         -0.1490      0.017     -8.793      0.000      -0.182      -0.116
==============================================================================
Omnibus:                       12.144   Durbin-Watson:                   0.837
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               23.080
Skew:                          -0.095   Prob(JB):                     9.73e-06
Kurtosis:                       4.150   Cond. No.                         27.5
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Agric_vol: 0.3483

--- Food_vol ---
Selected alpha for counts (Food_vol): 0.14174741629268062
Selected count terms: ['deal', 'deals', 'media', 'pillsbury', 'track']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Food_vol   R-squared:                       0.252
Model:                            OLS   Adj. R-squared:                  0.243
Method:                 Least Squares   F-statistic:                     27.10
Date:                Thu, 08 May 2025   Prob (F-statistic):           1.22e-23
Time:                        18:26:02   Log-Likelihood:                -255.81
No. Observations:                 408   AIC:                             523.6
Df Residuals:                     402   BIC:                             547.7
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.3487      0.030     11.731      0.000       0.290       0.407
deal          -0.0448      0.023     -1.917      0.056      -0.091       0.001
deals         -0.0593      0.033     -1.804      0.072      -0.124       0.005
media         -0.1043      0.032     -3.291      0.001      -0.167      -0.042
pillsbury      1.5568      0.230      6.777      0.000       1.105       2.008
track         -0.1385      0.053     -2.610      0.009      -0.243      -0.034
==============================================================================
Omnibus:                       12.481   Durbin-Watson:                   0.641
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               14.095
Skew:                           0.340   Prob(JB):                     0.000870
Kurtosis:                       3.605   Cond. No.                         23.1
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Food_vol: 0.2521

--- Soda_vol ---
Selected alpha for counts (Soda_vol): 0.1707352647470692
Selected count terms: ['brief', 'by', 'reporter', 'staff', 'wall']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Soda_vol   R-squared:                       0.447
Model:                            OLS   Adj. R-squared:                  0.440
Method:                 Least Squares   F-statistic:                     64.87
Date:                Thu, 08 May 2025   Prob (F-statistic):           1.48e-49
Time:                        18:29:59   Log-Likelihood:                -330.03
No. Observations:                 408   AIC:                             672.1
Df Residuals:                     402   BIC:                             696.1
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.3512      0.322     -1.092      0.275      -0.983       0.281
brief          0.0695      0.012      5.667      0.000       0.045       0.094
by            -0.0055      0.013     -0.439      0.661      -0.030       0.019
reporter       0.0122      0.023      0.534      0.593      -0.033       0.057
staff          0.0106      0.026      0.413      0.680      -0.040       0.061
wall           0.0207      0.017      1.207      0.228      -0.013       0.054
==============================================================================
Omnibus:                       19.894   Durbin-Watson:                   0.613
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               23.410
Skew:                           0.464   Prob(JB):                     8.25e-06
Kurtosis:                       3.719   Cond. No.                         305.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Soda_vol: 0.4466

--- Beer_vol ---
Selected alpha for counts (Beer_vol): 0.08529644499741025
Selected count terms: ['abreast', 'merry', 'politics', 'staff', 'wall']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Beer_vol   R-squared:                       0.441
Model:                            OLS   Adj. R-squared:                  0.434
Method:                 Least Squares   F-statistic:                     63.50
Date:                Thu, 08 May 2025   Prob (F-statistic):           9.89e-49
Time:                        19:28:17   Log-Likelihood:                -166.78
No. Observations:                 408   AIC:                             345.6
Df Residuals:                     402   BIC:                             369.6
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.1670      0.031     -5.450      0.000      -0.227      -0.107
abreast       -0.1726      0.063     -2.745      0.006      -0.296      -0.049
merry          0.8170      0.186      4.391      0.000       0.451       1.183
politics      -0.0967      0.022     -4.452      0.000      -0.139      -0.054
staff          0.0146      0.011      1.292      0.197      -0.008       0.037
wall           0.0167      0.010      1.672      0.095      -0.003       0.036
==============================================================================
Omnibus:                        2.547   Durbin-Watson:                   0.792
Prob(Omnibus):                  0.280   Jarque-Bera (JB):                2.514
Skew:                           0.083   Prob(JB):                        0.284
Kurtosis:                       3.347   Cond. No.                         164.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Beer_vol: 0.4413

--- Smoke_vol ---
Selected alpha for counts (Smoke_vol): 0.1567455410205595
Selected count terms: ['andrew', 'by', 'inc', 'news', 'of']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Smoke_vol   R-squared:                       0.331
Model:                            OLS   Adj. R-squared:                  0.323
Method:                 Least Squares   F-statistic:                     39.85
Date:                Thu, 08 May 2025   Prob (F-statistic):           3.03e-33
Time:                        19:56:08   Log-Likelihood:                -324.46
No. Observations:                 408   AIC:                             660.9
Df Residuals:                     402   BIC:                             685.0
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.4321      0.224      1.933      0.054      -0.007       0.872
andrew        -0.2301      0.064     -3.584      0.000      -0.356      -0.104
by            -0.0180      0.010     -1.834      0.067      -0.037       0.001
inc            0.0517      0.020      2.534      0.012       0.012       0.092
news          -0.0334      0.009     -3.740      0.000      -0.051      -0.016
of             0.0095      0.004      2.342      0.020       0.002       0.017
==============================================================================
Omnibus:                       12.314   Durbin-Watson:                   0.594
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               12.871
Skew:                           0.435   Prob(JB):                      0.00160
Kurtosis:                       3.002   Cond. No.                         219.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Smoke_vol: 0.3314

--- Toys_vol ---
Selected alpha for counts (Toys_vol): 0.0952750047242729
Selected count terms: ['andrews', 'jones', 'kruger', 'tharp', 'the']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Toys_vol   R-squared:                       0.185
Model:                            OLS   Adj. R-squared:                  0.175
Method:                 Least Squares   F-statistic:                     18.27
Date:                Thu, 08 May 2025   Prob (F-statistic):           2.39e-16
Time:                        20:24:18   Log-Likelihood:                -207.72
No. Observations:                 408   AIC:                             427.4
Df Residuals:                     402   BIC:                             451.5
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.1956      0.051     -3.854      0.000      -0.295      -0.096
andrews        0.5625      0.193      2.919      0.004       0.184       0.941
jones         -0.0385      0.010     -3.683      0.000      -0.059      -0.018
kruger         0.5590      0.191      2.923      0.004       0.183       0.935
tharp          0.6749      0.169      4.003      0.000       0.343       1.006
the            0.0128      0.003      4.061      0.000       0.007       0.019
==============================================================================
Omnibus:                       11.557   Durbin-Watson:                   0.777
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               11.951
Skew:                           0.419   Prob(JB):                      0.00254
Kurtosis:                       3.041   Cond. No.                         179.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Toys_vol: 0.1851

--- Fun_vol ---
Selected alpha for counts (Fun_vol): 0.11456687286348714
Selected count terms: ['brief', 'news', 'politics', 'weisman', 'world']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Fun_vol   R-squared:                       0.326
Model:                            OLS   Adj. R-squared:                  0.318
Method:                 Least Squares   F-statistic:                     38.93
Date:                Thu, 08 May 2025   Prob (F-statistic):           1.38e-32
Time:                        20:52:46   Log-Likelihood:                -273.01
No. Observations:                 408   AIC:                             558.0
Df Residuals:                     402   BIC:                             582.1
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.1137      0.055     -2.064      0.040      -0.222      -0.005
brief         -0.0334      0.007     -4.469      0.000      -0.048      -0.019
news           0.0156      0.011      1.484      0.138      -0.005       0.036
politics      -0.1264      0.026     -4.938      0.000      -0.177      -0.076
weisman        0.4729      0.135      3.498      0.001       0.207       0.739
world          0.0416      0.020      2.103      0.036       0.003       0.081
==============================================================================
Omnibus:                        5.817   Durbin-Watson:                   0.682
Prob(Omnibus):                  0.055   Jarque-Bera (JB):                5.876
Skew:                           0.293   Prob(JB):                       0.0530
Kurtosis:                       2.953   Cond. No.                         38.7
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Fun_vol: 0.3263

--- Books_vol ---
Selected alpha for counts (Books_vol): 0.14174741629268062
Selected count terms: ['brief', 'by', 'finance', 'news', 'world']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Books_vol   R-squared:                       0.400
Model:                            OLS   Adj. R-squared:                  0.393
Method:                 Least Squares   F-statistic:                     53.68
Date:                Thu, 08 May 2025   Prob (F-statistic):           1.26e-42
Time:                        20:54:52   Log-Likelihood:                -202.95
No. Observations:                 408   AIC:                             417.9
Df Residuals:                     402   BIC:                             442.0
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.1734      0.185     -0.940      0.348      -0.536       0.189
brief         -0.0343      0.008     -4.274      0.000      -0.050      -0.019
by             0.0050      0.008      0.609      0.543      -0.011       0.021
finance        0.1316      0.028      4.682      0.000       0.076       0.187
news           0.0016      0.009      0.171      0.864      -0.017       0.020
world          0.0584      0.017      3.494      0.001       0.026       0.091
==============================================================================
Omnibus:                       99.571   Durbin-Watson:                   0.649
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              262.798
Skew:                           1.172   Prob(JB):                     8.59e-58
Kurtosis:                       6.156   Cond. No.                         205.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Books_vol: 0.4004

--- Hshld_vol ---
Selected alpha for counts (Hshld_vol): 0.09353431520292387
Selected count terms: ['accessible', 'arbs', 'buff', 'collects', 'guidera']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Hshld_vol   R-squared:                       0.064
Model:                            OLS   Adj. R-squared:                  0.060
Method:                 Least Squares   F-statistic:                     13.89
Date:                Thu, 08 May 2025   Prob (F-statistic):           1.46e-06
Time:                        23:54:04   Log-Likelihood:                -225.13
No. Observations:                 408   AIC:                             456.3
Df Residuals:                     405   BIC:                             468.3
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0582      0.021     -2.781      0.006      -0.099      -0.017
accessible     0.2961      0.149      1.986      0.048       0.003       0.589
arbs           0.2961      0.149      1.986      0.048       0.003       0.589
buff           0.2961      0.149      1.986      0.048       0.003       0.589
collects       0.2961      0.149      1.986      0.048       0.003       0.589
guidera        0.8672      0.422      2.054      0.041       0.037       1.697
==============================================================================
Omnibus:                       12.072   Durbin-Watson:                   0.619
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               12.295
Skew:                           0.403   Prob(JB):                      0.00214
Kurtosis:                       3.269   Cond. No.                     1.17e+34
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is  3e-66. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
R-squared (counts) for Hshld_vol: 0.0642

--- Clths_vol ---
Selected alpha for counts (Clths_vol): 0.08850074914473438
Selected count terms: ['and', 'heard', 'jones', 'news', 'of']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Clths_vol   R-squared:                       0.308
Model:                            OLS   Adj. R-squared:                  0.299
Method:                 Least Squares   F-statistic:                     35.72
Date:                Fri, 09 May 2025   Prob (F-statistic):           3.07e-30
Time:                        04:17:37   Log-Likelihood:                -240.69
No. Observations:                 408   AIC:                             493.4
Df Residuals:                     402   BIC:                             517.5
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.1084      0.089      1.221      0.223      -0.066       0.283
and            0.0175      0.008      2.176      0.030       0.002       0.033
heard          0.0621      0.025      2.491      0.013       0.013       0.111
jones         -0.0780      0.012     -6.438      0.000      -0.102      -0.054
news           0.0140      0.008      1.821      0.069      -0.001       0.029
of            -0.0105      0.003     -3.064      0.002      -0.017      -0.004
==============================================================================
Omnibus:                        5.988   Durbin-Watson:                   0.561
Prob(Omnibus):                  0.050   Jarque-Bera (JB):                3.883
Skew:                           0.034   Prob(JB):                        0.143
Kurtosis:                       2.527   Cond. No.                         73.9
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Clths_vol: 0.3076

--- Hlth_vol ---
Selected alpha for counts (Hlth_vol): 0.1176811952434999
Selected count terms: ['larkin', 'marketing', 'politics', 'salaried', 'trafalgar']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Hlth_vol   R-squared:                       0.212
Model:                            OLS   Adj. R-squared:                  0.202
Method:                 Least Squares   F-statistic:                     21.63
Date:                Fri, 09 May 2025   Prob (F-statistic):           3.44e-19
Time:                        04:35:06   Log-Likelihood:                -279.62
No. Observations:                 408   AIC:                             571.2
Df Residuals:                     402   BIC:                             595.3
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.2704      0.028     -9.671      0.000      -0.325      -0.215
larkin         1.6366      0.343      4.769      0.000       0.962       2.311
marketing     -0.1191      0.033     -3.664      0.000      -0.183      -0.055
politics      -0.0970      0.027     -3.535      0.000      -0.151      -0.043
salaried       1.0188      0.307      3.320      0.001       0.416       1.622
trafalgar      1.3411      0.375      3.573      0.000       0.603       2.079
==============================================================================
Omnibus:                       22.366   Durbin-Watson:                   0.853
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               26.060
Skew:                           0.513   Prob(JB):                     2.19e-06
Kurtosis:                       3.693   Cond. No.                         22.6
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Hlth_vol: 0.2120

--- MedEq_vol ---
Skipping MedEq_vol: No alpha found for 5 non-zero counts for MedEq_vol.

--- Drugs_vol ---
Selected alpha for counts (Drugs_vol): 0.14174741629268062
Selected count terms: ['business', 'calian', 'clinton', 'economics', 'of']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Drugs_vol   R-squared:                       0.283
Model:                            OLS   Adj. R-squared:                  0.274
Method:                 Least Squares   F-statistic:                     31.79
Date:                Fri, 09 May 2025   Prob (F-statistic):           2.76e-27
Time:                        11:05:41   Log-Likelihood:                -295.17
No. Observations:                 408   AIC:                             602.3
Df Residuals:                     402   BIC:                             626.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.2469      0.056     -4.405      0.000      -0.357      -0.137
business       0.0461      0.008      5.492      0.000       0.030       0.063
calian         0.7165      0.173      4.150      0.000       0.377       1.056
clinton        0.1988      0.051      3.897      0.000       0.099       0.299
economics     -0.1426      0.031     -4.581      0.000      -0.204      -0.081
of             0.0115      0.003      3.641      0.000       0.005       0.018
==============================================================================
Omnibus:                        6.289   Durbin-Watson:                   0.617
Prob(Omnibus):                  0.043   Jarque-Bera (JB):                6.170
Skew:                           0.257   Prob(JB):                       0.0457
Kurtosis:                       3.314   Cond. No.                         120.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Drugs_vol: 0.2833

--- Chems_vol ---
Selected alpha for counts (Chems_vol): 0.08111308307896872
Selected count terms: ['china', 'internet', 'newswires', 'unit', 'wall']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Chems_vol   R-squared:                       0.187
Model:                            OLS   Adj. R-squared:                  0.177
Method:                 Least Squares   F-statistic:                     18.46
Date:                Fri, 09 May 2025   Prob (F-statistic):           1.62e-16
Time:                        11:19:13   Log-Likelihood:                -148.75
No. Observations:                 408   AIC:                             309.5
Df Residuals:                     402   BIC:                             333.6
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0659      0.038      1.729      0.084      -0.009       0.141
china          0.0621      0.020      3.038      0.003       0.022       0.102
internet       0.1608      0.043      3.729      0.000       0.076       0.246
newswires      0.0388      0.010      3.976      0.000       0.020       0.058
unit          -0.0447      0.018     -2.462      0.014      -0.080      -0.009
wall          -0.0059      0.002     -2.374      0.018      -0.011      -0.001
==============================================================================
Omnibus:                        1.755   Durbin-Watson:                   0.673
Prob(Omnibus):                  0.416   Jarque-Bera (JB):                1.545
Skew:                          -0.086   Prob(JB):                        0.462
Kurtosis:                       3.248   Cond. No.                         30.4
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Chems_vol: 0.1868

--- Rubbr_vol ---
Selected alpha for counts (Rubbr_vol): 0.06963744730628223
Selected count terms: ['business', 'degrees', 'geoffrey', 'jerusalem', 'shipbuilding']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Rubbr_vol   R-squared:                       0.245
Model:                            OLS   Adj. R-squared:                  0.236
Method:                 Least Squares   F-statistic:                     26.09
Date:                Fri, 09 May 2025   Prob (F-statistic):           7.84e-23
Time:                        13:02:53   Log-Likelihood:                -57.558
No. Observations:                 408   AIC:                             127.1
Df Residuals:                     402   BIC:                             151.2
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
const           -0.0362      0.022     -1.675      0.095      -0.079       0.006
business        -0.0246      0.004     -5.480      0.000      -0.033      -0.016
degrees          0.4903      0.184      2.662      0.008       0.128       0.852
geoffrey         0.1951      0.049      3.993      0.000       0.099       0.291
jerusalem        0.6354      0.238      2.673      0.008       0.168       1.103
shipbuilding     0.8076      0.238      3.398      0.001       0.340       1.275
==============================================================================
Omnibus:                        2.627   Durbin-Watson:                   0.839
Prob(Omnibus):                  0.269   Jarque-Bera (JB):                2.681
Skew:                           0.170   Prob(JB):                        0.262
Kurtosis:                       2.794   Cond. No.                         96.3
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Rubbr_vol: 0.2450

--- Txtls_vol ---
Selected alpha for counts (Txtls_vol): 0.12796968682159415
Selected count terms: ['by', 'corporate', 'geoffrey', 'news', 'staff']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Txtls_vol   R-squared:                       0.476
Model:                            OLS   Adj. R-squared:                  0.470
Method:                 Least Squares   F-statistic:                     73.09
Date:                Fri, 09 May 2025   Prob (F-statistic):           2.56e-54
Time:                        14:25:03   Log-Likelihood:                -220.60
No. Observations:                 408   AIC:                             453.2
Df Residuals:                     402   BIC:                             477.3
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.2695      0.134     -2.016      0.044      -0.532      -0.007
by             0.0191      0.007      2.856      0.005       0.006       0.032
corporate      0.0976      0.017      5.799      0.000       0.064       0.131
geoffrey       0.3510      0.074      4.752      0.000       0.206       0.496
news           0.0061      0.008      0.787      0.432      -0.009       0.021
staff         -0.0260      0.004     -6.791      0.000      -0.033      -0.018
==============================================================================
Omnibus:                       11.209   Durbin-Watson:                   0.684
Prob(Omnibus):                  0.004   Jarque-Bera (JB):               11.961
Skew:                           0.339   Prob(JB):                      0.00253
Kurtosis:                       3.493   Cond. No.                         147.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Txtls_vol: 0.4762

--- BldMt_vol ---
Skipping BldMt_vol: No alpha found for 5 non-zero counts for BldMt_vol.

--- Cnstr_vol ---
Selected alpha for counts (Cnstr_vol): 0.125631660247412
Selected count terms: ['leading', 'newswires', 'policy', 'politics', 'street']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Cnstr_vol   R-squared:                       0.324
Model:                            OLS   Adj. R-squared:                  0.316
Method:                 Least Squares   F-statistic:                     38.62
Date:                Fri, 09 May 2025   Prob (F-statistic):           2.32e-32
Time:                        15:18:08   Log-Likelihood:                -156.41
No. Observations:                 408   AIC:                             324.8
Df Residuals:                     402   BIC:                             348.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0316      0.035      0.898      0.369      -0.038       0.101
leading        0.0555      0.027      2.062      0.040       0.003       0.108
newswires      0.0455      0.010      4.425      0.000       0.025       0.066
policy         0.1179      0.034      3.431      0.001       0.050       0.185
politics       0.0827      0.022      3.726      0.000       0.039       0.126
street        -0.0147      0.003     -5.789      0.000      -0.020      -0.010
==============================================================================
Omnibus:                        1.715   Durbin-Watson:                   0.596
Prob(Omnibus):                  0.424   Jarque-Bera (JB):                1.505
Skew:                          -0.083   Prob(JB):                        0.471
Kurtosis:                       3.247   Cond. No.                         26.3
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Cnstr_vol: 0.3245

--- Steel_vol ---
Selected alpha for counts (Steel_vol): 0.1006938631476027
Selected count terms: ['media', 'politics', 'staff', 'technology', 'trump']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Steel_vol   R-squared:                       0.462
Model:                            OLS   Adj. R-squared:                  0.455
Method:                 Least Squares   F-statistic:                     68.93
Date:                Fri, 09 May 2025   Prob (F-statistic):           6.11e-52
Time:                        15:54:12   Log-Likelihood:                -173.87
No. Observations:                 408   AIC:                             359.7
Df Residuals:                     402   BIC:                             383.8
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.1737      0.041      4.195      0.000       0.092       0.255
media          0.0930      0.027      3.393      0.001       0.039       0.147
politics       0.0697      0.022      3.189      0.002       0.027       0.113
staff         -0.0254      0.003     -8.357      0.000      -0.031      -0.019
technology     0.0561      0.018      3.102      0.002       0.021       0.092
trump          0.2340      0.027      8.539      0.000       0.180       0.288
==============================================================================
Omnibus:                        6.298   Durbin-Watson:                   0.614
Prob(Omnibus):                  0.043   Jarque-Bera (JB):                6.453
Skew:                           0.297   Prob(JB):                       0.0397
Kurtosis:                       2.836   Cond. No.                         25.7
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Steel_vol: 0.4616

--- FabPr_vol ---
Selected alpha for counts (FabPr_vol): 0.16566059589499135
Selected count terms: ['islamic', 'josh', 'news', 'ryan', 'wsj']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              FabPr_vol   R-squared:                       0.330
Model:                            OLS   Adj. R-squared:                  0.321
Method:                 Least Squares   F-statistic:                     39.55
Date:                Fri, 09 May 2025   Prob (F-statistic):           4.97e-33
Time:                        17:08:52   Log-Likelihood:                -378.73
No. Observations:                 408   AIC:                             769.5
Df Residuals:                     402   BIC:                             793.5
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.3689      0.041     -9.106      0.000      -0.449      -0.289
islamic        0.5608      0.125      4.504      0.000       0.316       0.806
josh           0.2652      0.127      2.089      0.037       0.016       0.515
news           0.0467      0.008      6.119      0.000       0.032       0.062
ryan           0.4968      0.108      4.594      0.000       0.284       0.709
wsj            0.1416      0.059      2.408      0.016       0.026       0.257
==============================================================================
Omnibus:                        5.600   Durbin-Watson:                   0.628
Prob(Omnibus):                  0.061   Jarque-Bera (JB):                5.696
Skew:                           0.286   Prob(JB):                       0.0580
Kurtosis:                       2.915   Cond. No.                         28.6
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for FabPr_vol: 0.3297

--- Mach_vol ---
Selected alpha for counts (Mach_vol): 0.08111308307896872
Selected count terms: ['economics', 'news', 'newswires', 'of', 'squeo']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Mach_vol   R-squared:                       0.207
Model:                            OLS   Adj. R-squared:                  0.197
Method:                 Least Squares   F-statistic:                     20.94
Date:                Fri, 09 May 2025   Prob (F-statistic):           1.31e-18
Time:                        17:13:57   Log-Likelihood:                -144.93
No. Observations:                 408   AIC:                             301.9
Df Residuals:                     402   BIC:                             325.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.2362      0.071      3.335      0.001       0.097       0.376
economics      0.0928      0.024      3.945      0.000       0.047       0.139
news           0.0091      0.006      1.642      0.101      -0.002       0.020
newswires     -0.0279      0.011     -2.556      0.011      -0.049      -0.006
of            -0.0093      0.003     -3.101      0.002      -0.015      -0.003
squeo         -0.4289      0.114     -3.778      0.000      -0.652      -0.206
==============================================================================
Omnibus:                        0.801   Durbin-Watson:                   0.633
Prob(Omnibus):                  0.670   Jarque-Bera (JB):                0.584
Skew:                          -0.027   Prob(JB):                        0.747
Kurtosis:                       3.178   Cond. No.                         113.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Mach_vol: 0.2066

--- ElcEq_vol ---
Selected alpha for counts (ElcEq_vol): 0.09770099572992257
Selected count terms: ['backup', 'business', 'inc', 'policy', 'staff']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              ElcEq_vol   R-squared:                       0.390
Model:                            OLS   Adj. R-squared:                  0.382
Method:                 Least Squares   F-statistic:                     51.31
Date:                Fri, 09 May 2025   Prob (F-statistic):           4.36e-41
Time:                        17:17:51   Log-Likelihood:                -254.90
No. Observations:                 408   AIC:                             521.8
Df Residuals:                     402   BIC:                             545.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.4937      0.041    -12.178      0.000      -0.573      -0.414
backup        -0.8429      0.207     -4.072      0.000      -1.250      -0.436
business       0.0353      0.010      3.506      0.001       0.016       0.055
inc            0.0309      0.019      1.640      0.102      -0.006       0.068
policy        -0.1460      0.041     -3.571      0.000      -0.226      -0.066
staff          0.0330      0.003      9.584      0.000       0.026       0.040
==============================================================================
Omnibus:                        2.875   Durbin-Watson:                   0.793
Prob(Omnibus):                  0.237   Jarque-Bera (JB):                2.689
Skew:                           0.195   Prob(JB):                        0.261
Kurtosis:                       3.081   Cond. No.                         102.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for ElcEq_vol: 0.3896

--- Autos_vol ---
Selected alpha for counts (Autos_vol): 0.0837380653526649
Selected count terms: ['1993', 'brief', 'concern', 'international', 'rejecting']

OLS Summary for counts:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Autos_vol   R-squared:                       0.269
Model:                            OLS   Adj. R-squared:                  0.260
Method:                 Least Squares   F-statistic:                     29.55
Date:                Fri, 09 May 2025   Prob (F-statistic):           1.46e-25
Time:                        17:37:38   Log-Likelihood:                -210.15
No. Observations:                 408   AIC:                             432.3
Df Residuals:                     402   BIC:                             456.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
=================================================================================
                    coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
const            -0.2016      0.029     -6.890      0.000      -0.259      -0.144
1993              0.6140      0.171      3.582      0.000       0.277       0.951
brief             0.0328      0.006      5.844      0.000       0.022       0.044
concern           0.1693      0.040      4.225      0.000       0.091       0.248
international     0.0631      0.022      2.825      0.005       0.019       0.107
rejecting         1.2243      0.292      4.199      0.000       0.651       1.797
==============================================================================
Omnibus:                        0.548   Durbin-Watson:                   0.770
Prob(Omnibus):                  0.761   Jarque-Bera (JB):                0.349
Skew:                          -0.014   Prob(JB):                        0.840
Kurtosis:                       3.140   Cond. No.                         79.4
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
R-squared (counts) for Autos_vol: 0.2688

--- Aero_vol ---
Skipping Aero_vol: No alpha found for 5 non-zero counts for Aero_vol.
