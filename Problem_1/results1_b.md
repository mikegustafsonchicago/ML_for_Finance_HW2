
=== Lasso and OLS for mret ===
Selected alpha: 0.0041320124001153384
Selected topics:  ['Problems', 'Federal Reserve', 'Recession', 'Bear/bull market', 'Options/VIX']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   mret   R-squared:                       0.108
Model:                            OLS   Adj. R-squared:                  0.097
Method:                 Least Squares   F-statistic:                     9.577
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.22e-08
Time:                        12:49:20   Log-Likelihood:                 713.84
No. Observations:                 402   AIC:                            -1416.
Df Residuals:                     396   BIC:                            -1392.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
const                0.1238      0.021      5.919      0.000       0.083       0.165
Problems            -9.6636      3.833     -2.521      0.012     -17.199      -2.128
Federal Reserve     -2.4771      0.901     -2.750      0.006      -4.248      -0.706
Recession           -2.6442      1.242     -2.129      0.034      -5.086      -0.203
Bear/bull market    -1.5296      1.076     -1.421      0.156      -3.646       0.587
Options/VIX         -2.3202      1.199     -1.935      0.054      -4.678       0.037
==============================================================================
Omnibus:                       11.936   Durbin-Watson:                   1.962
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               21.719
Skew:                          -0.123   Prob(JB):                     1.92e-05
Kurtosis:                       4.112   Cond. No.                     1.90e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.9e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.1079

=== Lasso and OLS for vol ===
Selected alpha: 0.08111308307896872
Selected topics:  ['Small business', 'Problems', 'Recession', 'Investment banking', 'Options/VIX']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                    vol   R-squared:                       0.629
Model:                            OLS   Adj. R-squared:                  0.625
Method:                 Least Squares   F-statistic:                     134.5
Date:                Tue, 06 May 2025   Prob (F-statistic):           4.77e-83
Time:                        12:49:34   Log-Likelihood:                -31.834
No. Observations:                 402   AIC:                             75.67
Df Residuals:                     396   BIC:                             99.65
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
======================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------
const                 -3.1888      0.167    -19.078      0.000      -3.517      -2.860
Small business      -120.0520     21.187     -5.666      0.000    -161.706     -78.398
Problems             134.8471     24.858      5.425      0.000      85.977     183.717
Recession             92.9287      8.660     10.731      0.000      75.903     109.954
Investment banking    25.9088      7.251      3.573      0.000      11.654      40.163
Options/VIX           53.9664      7.292      7.401      0.000      39.631      68.302
==============================================================================
Omnibus:                       25.775   Durbin-Watson:                   0.644
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               30.715
Skew:                           0.565   Prob(JB):                     2.14e-07
Kurtosis:                       3.746   Cond. No.                     1.94e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.94e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.6294

=== Lasso and OLS for indpro ===
Selected alpha: 0.0005659170163246243
Selected topics:  ['Recession', 'Space program', 'Clintons', 'Southeast Asia', 'Oil market']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 indpro   R-squared:                       0.219
Model:                            OLS   Adj. R-squared:                  0.209
Method:                 Least Squares   F-statistic:                     22.22
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.21e-19
Time:                        12:49:38   Log-Likelihood:                 1528.7
No. Observations:                 402   AIC:                            -3045.
Df Residuals:                     396   BIC:                            -3021.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const              0.0098      0.002      5.277      0.000       0.006       0.013
Recession         -1.0687      0.127     -8.394      0.000      -1.319      -0.818
Space program     -0.4862      0.301     -1.618      0.106      -1.077       0.105
Clintons           0.0572      0.078      0.738      0.461      -0.095       0.210
Southeast Asia     0.3595      0.149      2.414      0.016       0.067       0.652
Oil market        -0.3264      0.101     -3.244      0.001      -0.524      -0.129
==============================================================================
Omnibus:                      102.413   Durbin-Watson:                   2.031
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1045.593
Skew:                          -0.750   Prob(JB):                    8.96e-228
Kurtosis:                      10.757   Cond. No.                     1.12e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.12e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2191

=== Lasso and OLS for indprol1 ===
Selected alpha: 0.0005336699231206312
Selected topics:  ['Russia', 'Health insurance', 'Recession', 'Space program', 'Oil market']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               indprol1   R-squared:                       0.277
Model:                            OLS   Adj. R-squared:                  0.268
Method:                 Least Squares   F-statistic:                     30.30
Date:                Tue, 06 May 2025   Prob (F-statistic):           4.36e-26
Time:                        12:49:38   Log-Likelihood:                 1548.3
No. Observations:                 402   AIC:                            -3085.
Df Residuals:                     396   BIC:                            -3061.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
const                0.0117      0.002      6.937      0.000       0.008       0.015
Russia              -0.2240      0.093     -2.399      0.017      -0.408      -0.040
Health insurance     0.3862      0.105      3.664      0.000       0.179       0.593
Recession           -1.1621      0.121     -9.632      0.000      -1.399      -0.925
Space program       -0.5691      0.285     -1.997      0.047      -1.129      -0.009
Oil market          -0.3457      0.093     -3.734      0.000      -0.528      -0.164
==============================================================================
Omnibus:                      101.660   Durbin-Watson:                   2.029
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              759.553
Skew:                          -0.848   Prob(JB):                    1.16e-165
Kurtosis:                       9.517   Cond. No.                     1.11e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.11e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2767

=== Lasso and OLS for Agric_vol ===
Skipping variable Agric_vol: No alpha found that yields exactly 5 non-zero coefficients.

=== Lasso and OLS for Food_vol ===
Selected alpha: 0.11887076977119033
Selected topics:  ['Drexel', 'Investment banking', 'Southeast Asia', 'Mortgages', 'Retail']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Food_vol   R-squared:                       0.306
Model:                            OLS   Adj. R-squared:                  0.297
Method:                 Least Squares   F-statistic:                     34.90
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.46e-29
Time:                        12:54:22   Log-Likelihood:                -232.53
No. Observations:                 402   AIC:                             477.1
Df Residuals:                     396   BIC:                             501.0
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
======================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------
const                  1.0179      0.149      6.817      0.000       0.724       1.311
Drexel                22.1957      9.172      2.420      0.016       4.165      40.227
Investment banking   -38.7922     14.085     -2.754      0.006     -66.483     -11.102
Southeast Asia       -52.3065     12.918     -4.049      0.000     -77.703     -26.910
Mortgages            -34.6445      9.053     -3.827      0.000     -52.443     -16.846
Retail               -40.8820     14.983     -2.729      0.007     -70.339     -11.425
==============================================================================
Omnibus:                       57.910   Durbin-Watson:                   0.619
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              111.153
Skew:                           0.809   Prob(JB):                     7.30e-25
Kurtosis:                       5.005   Cond. No.                         757.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

R-squared: 0.3059

=== Lasso and OLS for Soda_vol ===
Selected alpha: 0.1707352647470692
Selected topics:  ['Japan', 'International exchanges', 'China', 'Trading activity', 'Lawsuits']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Soda_vol   R-squared:                       0.515
Model:                            OLS   Adj. R-squared:                  0.509
Method:                 Least Squares   F-statistic:                     84.17
Date:                Tue, 06 May 2025   Prob (F-statistic):           4.30e-60
Time:                        12:54:32   Log-Likelihood:                -292.53
No. Observations:                 402   AIC:                             597.1
Df Residuals:                     396   BIC:                             621.0
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                      -1.1020      0.208     -5.301      0.000      -1.511      -0.693
Japan                      75.7584     22.426      3.378      0.001      31.669     119.848
International exchanges    31.4227      8.345      3.766      0.000      15.017      47.828
China                     -27.3637     12.524     -2.185      0.029     -51.986      -2.742
Trading activity           35.3868     15.430      2.293      0.022       5.052      65.721
Lawsuits                   58.9995     21.090      2.798      0.005      17.538     100.461
==============================================================================
Omnibus:                       35.417   Durbin-Watson:                   0.688
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               59.875
Skew:                           0.563   Prob(JB):                     9.96e-14
Kurtosis:                       4.519   Cond. No.                         927.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

R-squared: 0.5152

=== Lasso and OLS for Beer_vol ===
Selected alpha: 0.08111308307896872
Selected topics:  ['China', 'Futures/indices', 'Private equity/hedge funds', 'Retail', 'Revenue growth']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Beer_vol   R-squared:                       0.458
Model:                            OLS   Adj. R-squared:                  0.451
Method:                 Least Squares   F-statistic:                     66.92
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.42e-50
Time:                        12:54:42   Log-Likelihood:                -158.65
No. Observations:                 402   AIC:                             329.3
Df Residuals:                     396   BIC:                             353.3
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================================
                                 coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------------
const                          0.5017      0.199      2.523      0.012       0.111       0.893
China                        -34.2285     11.903     -2.876      0.004     -57.630     -10.827
Futures/indices               98.9531     32.416      3.053      0.002      35.224     162.682
Private equity/hedge funds   -10.5682     10.733     -0.985      0.325     -31.670      10.533
Retail                       -38.8333     12.611     -3.079      0.002     -63.626     -14.040
Revenue growth               -66.1592     22.949     -2.883      0.004    -111.277     -21.041
==============================================================================
Omnibus:                       14.806   Durbin-Watson:                   0.657
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               19.983
Skew:                           0.319   Prob(JB):                     4.58e-05
Kurtosis:                       3.886   Cond. No.                     1.86e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.86e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4580

=== Lasso and OLS for Smoke_vol ===
Selected alpha: 0.20565123083486536
Selected topics:  ['News conference', 'Economic growth', 'Financial crisis', 'Tobacco', 'Exchanges/composites']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Smoke_vol   R-squared:                       0.436
Model:                            OLS   Adj. R-squared:                  0.428
Method:                 Least Squares   F-statistic:                     61.12
Date:                Tue, 06 May 2025   Prob (F-statistic):           4.07e-47
Time:                        12:54:52   Log-Likelihood:                -288.06
No. Observations:                 402   AIC:                             588.1
Df Residuals:                     396   BIC:                             612.1
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                    0.6638      0.366      1.814      0.070      -0.056       1.383
News conference        -89.7643     44.231     -2.029      0.043    -176.721      -2.808
Economic growth        -43.1167     21.871     -1.971      0.049     -86.114      -0.119
Financial crisis       -41.6120      7.586     -5.485      0.000     -56.526     -26.698
Tobacco                100.7371     21.626      4.658      0.000      58.220     143.254
Exchanges/composites    12.7051     18.543      0.685      0.494     -23.751      49.161
==============================================================================
Omnibus:                        4.610   Durbin-Watson:                   0.594
Prob(Omnibus):                  0.100   Jarque-Bera (JB):                4.659
Skew:                           0.180   Prob(JB):                       0.0973
Kurtosis:                       3.386   Cond. No.                     1.84e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.84e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4356

=== Lasso and OLS for Toys_vol ===
Selected alpha: 0.06350425168595962
Selected topics:  ['Savings & loans', 'Disease', 'Broadcasting', 'Oil market', 'Reagan']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Toys_vol   R-squared:                       0.285
Model:                            OLS   Adj. R-squared:                  0.276
Method:                 Least Squares   F-statistic:                     31.54
Date:                Tue, 06 May 2025   Prob (F-statistic):           4.92e-27
Time:                        12:57:03   Log-Likelihood:                -166.18
No. Observations:                 402   AIC:                             344.4
Df Residuals:                     396   BIC:                             368.3
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const               0.1731      0.135      1.283      0.200      -0.092       0.438
Savings & loans     9.4379      8.778      1.075      0.283      -7.819      26.695
Disease           -25.1199     11.488     -2.187      0.029     -47.705      -2.535
Broadcasting      -67.9564     14.591     -4.657      0.000     -96.642     -39.271
Oil market         19.1653      6.154      3.115      0.002       7.068      31.263
Reagan             30.7268      6.532      4.704      0.000      17.885      43.569
==============================================================================
Omnibus:                       24.437   Durbin-Watson:                   0.841
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               27.823
Skew:                           0.572   Prob(JB):                     9.08e-07
Kurtosis:                       3.592   Cond. No.                         808.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

R-squared: 0.2848

=== Lasso and OLS for Fun_vol ===
Selected alpha: 0.1707352647470692
Selected topics:  ['Competition', 'European sovereign debt', 'Financial crisis', 'Marketing', 'Exchanges/composites']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Fun_vol   R-squared:                       0.330
Model:                            OLS   Adj. R-squared:                  0.321
Method:                 Least Squares   F-statistic:                     38.98
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.57e-32
Time:                        12:57:15   Log-Likelihood:                -267.19
No. Observations:                 402   AIC:                             546.4
Df Residuals:                     396   BIC:                             570.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       0.6629      0.185      3.578      0.000       0.299       1.027
Competition              -128.3532     36.738     -3.494      0.001    -200.578     -56.128
European sovereign debt    24.1027      6.975      3.456      0.001      10.390      37.815
Financial crisis           16.3349      7.219      2.263      0.024       2.143      30.527
Marketing                 -55.5776     21.426     -2.594      0.010     -97.701     -13.455
Exchanges/composites      -21.7756     13.903     -1.566      0.118     -49.108       5.557
==============================================================================
Omnibus:                        7.007   Durbin-Watson:                   0.607
Prob(Omnibus):                  0.030   Jarque-Bera (JB):                6.646
Skew:                           0.268   Prob(JB):                       0.0360
Kurtosis:                       2.669   Cond. No.                     1.61e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.61e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3298

=== Lasso and OLS for Books_vol ===
Selected alpha: 0.1707352647470692
Selected topics:  ['Police/crime', 'Financial crisis', 'International exchanges', 'Exchanges/composites', 'European politics']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Books_vol   R-squared:                       0.439
Model:                            OLS   Adj. R-squared:                  0.432
Method:                 Least Squares   F-statistic:                     61.96
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.25e-47
Time:                        12:57:27   Log-Likelihood:                -187.12
No. Observations:                 402   AIC:                             386.2
Df Residuals:                     396   BIC:                             410.2
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                      -0.3159      0.156     -2.019      0.044      -0.624      -0.008
Police/crime               28.5266     10.388      2.746      0.006       8.103      48.950
Financial crisis           26.6580      5.537      4.814      0.000      15.772      37.544
International exchanges   -35.1653      5.576     -6.307      0.000     -46.127     -24.204
Exchanges/composites       12.5690     15.176      0.828      0.408     -17.266      42.404
European politics          24.1112     10.007      2.409      0.016       4.437      43.786
==============================================================================
Omnibus:                      129.320   Durbin-Watson:                   0.580
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              489.430
Skew:                           1.397   Prob(JB):                    5.27e-107
Kurtosis:                       7.628   Cond. No.                         855.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

R-squared: 0.4389

=== Lasso and OLS for Hshld_vol ===
Selected alpha: 0.08111308307896872
Selected topics:  ['Activists', 'Environment ', 'Control stakes', 'Recession', 'Credit cards']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Hshld_vol   R-squared:                       0.229
Model:                            OLS   Adj. R-squared:                  0.219
Method:                 Least Squares   F-statistic:                     23.51
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.05e-20
Time:                        12:57:42   Log-Likelihood:                -183.51
No. Observations:                 402   AIC:                             379.0
Df Residuals:                     396   BIC:                             403.0
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const              0.5503      0.230      2.397      0.017       0.099       1.002
Activists         46.7564     21.471      2.178      0.030       4.545      88.968
Environment      -89.3051     16.259     -5.493      0.000    -121.270     -57.340
Control stakes    99.3886     23.555      4.219      0.000      53.080     145.697
Recession        -26.1408      9.635     -2.713      0.007     -45.082      -7.199
Credit cards    -158.2560     30.491     -5.190      0.000    -218.201     -98.311
==============================================================================
Omnibus:                       23.835   Durbin-Watson:                   0.800
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               36.280
Skew:                           0.431   Prob(JB):                     1.32e-08
Kurtosis:                       4.192   Cond. No.                     1.61e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.61e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2289

=== Lasso and OLS for Clths_vol ===
Selected alpha: 0.08850074914473438
Selected topics:  ['Cable', 'C-suite', 'SEC', 'Phone companies', 'European politics']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Clths_vol   R-squared:                       0.482
Model:                            OLS   Adj. R-squared:                  0.475
Method:                 Least Squares   F-statistic:                     73.66
Date:                Tue, 06 May 2025   Prob (F-statistic):           2.06e-54
Time:                        13:00:07   Log-Likelihood:                -175.63
No. Observations:                 402   AIC:                             363.3
Df Residuals:                     396   BIC:                             387.2
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                 1.8673      0.223      8.386      0.000       1.429       2.305
Cable               -78.4303     18.682     -4.198      0.000    -115.159     -41.701
C-suite            -149.8527     28.136     -5.326      0.000    -205.168     -94.537
SEC                 -52.3396     18.317     -2.857      0.004     -88.351     -16.328
Phone companies     -65.2761      9.067     -7.199      0.000     -83.101     -47.451
European politics     7.8261      8.651      0.905      0.366      -9.182      24.834
==============================================================================
Omnibus:                        0.589   Durbin-Watson:                   0.684
Prob(Omnibus):                  0.745   Jarque-Bera (JB):                0.686
Skew:                          -0.082   Prob(JB):                        0.710
Kurtosis:                       2.882   Cond. No.                     1.59e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.59e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4819

=== Lasso and OLS for Hlth_vol ===
Selected alpha: 0.1124737178364752
Selected topics:  ['Record high', 'Mining', 'Publishing', 'Latin America', 'Product prices']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Hlth_vol   R-squared:                       0.186
Model:                            OLS   Adj. R-squared:                  0.176
Method:                 Least Squares   F-statistic:                     18.11
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.45e-16
Time:                        13:05:10   Log-Likelihood:                -282.95
No. Observations:                 402   AIC:                             577.9
Df Residuals:                     396   BIC:                             601.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const              0.9236      0.262      3.528      0.000       0.409       1.438
Record high     -125.5460     29.899     -4.199      0.000    -184.326     -66.766
Mining           -83.5173     24.749     -3.375      0.001    -132.173     -34.861
Publishing      -106.8110     26.217     -4.074      0.000    -158.352     -55.270
Latin America     80.3259     22.658      3.545      0.000      35.780     124.871
Product prices   -25.7152     36.192     -0.711      0.478     -96.867      45.437
==============================================================================
Omnibus:                       73.364   Durbin-Watson:                   0.897
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              150.066
Skew:                           0.975   Prob(JB):                     2.59e-33
Kurtosis:                       5.271   Cond. No.                     1.63e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.63e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.1861

=== Lasso and OLS for MedEq_vol ===
Selected alpha: 0.1176811952434999
Selected topics:  ['Earnings losses', 'China', 'Mid-level executives', 'Financial reports', 'Private equity/hedge funds']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              MedEq_vol   R-squared:                       0.280
Model:                            OLS   Adj. R-squared:                  0.271
Method:                 Least Squares   F-statistic:                     30.84
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.68e-26
Time:                        13:05:24   Log-Likelihood:                -180.08
No. Observations:                 402   AIC:                             372.2
Df Residuals:                     396   BIC:                             396.1
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================================
                                 coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------------
const                         -0.7380      0.200     -3.695      0.000      -1.131      -0.345
Earnings losses               27.2686     15.251      1.788      0.075      -2.715      57.252
China                         -5.9362     11.704     -0.507      0.612     -28.945      17.073
Mid-level executives          30.5264     17.515      1.743      0.082      -3.908      64.961
Financial reports            108.2138     38.470      2.813      0.005      32.582     183.845
Private equity/hedge funds   -16.5193     10.646     -1.552      0.122     -37.450       4.411
==============================================================================
Omnibus:                       17.906   Durbin-Watson:                   0.610
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               25.413
Skew:                           0.358   Prob(JB):                     3.03e-06
Kurtosis:                       4.002   Cond. No.                     2.07e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.07e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2803

=== Lasso and OLS for Drugs_vol ===
Selected alpha: 0.14831025143361043
Selected topics:  ['European sovereign debt', 'Oil drilling', 'Clintons', 'Mortgages', 'Foods/consumer goods']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Drugs_vol   R-squared:                       0.345
Model:                            OLS   Adj. R-squared:                  0.336
Method:                 Least Squares   F-statistic:                     41.66
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.96e-34
Time:                        13:06:55   Log-Likelihood:                -275.33
No. Observations:                 402   AIC:                             562.7
Df Residuals:                     396   BIC:                             586.6
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       0.2568      0.175      1.467      0.143      -0.087       0.601
European sovereign debt   -17.3233      5.750     -3.012      0.003     -28.629      -6.018
Oil drilling              -49.7396     15.800     -3.148      0.002     -80.801     -18.678
Clintons                   33.1694      7.194      4.611      0.000      19.027      47.312
Mortgages                 -63.4830      9.373     -6.773      0.000     -81.910     -45.056
Foods/consumer goods       80.0791     25.947      3.086      0.002      29.068     131.091
==============================================================================
Omnibus:                        8.344   Durbin-Watson:                   0.527
Prob(Omnibus):                  0.015   Jarque-Bera (JB):                8.235
Skew:                           0.332   Prob(JB):                       0.0163
Kurtosis:                       3.228   Cond. No.                     1.09e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.09e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3447

=== Lasso and OLS for Chems_vol ===
Selected alpha: 0.06734150657750829
Selected topics:  ['Internet', 'M&A', 'Savings & loans', 'Russia', 'Bankruptcy']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Chems_vol   R-squared:                       0.330
Model:                            OLS   Adj. R-squared:                  0.321
Method:                 Least Squares   F-statistic:                     39.00
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.52e-32
Time:                        13:07:04   Log-Likelihood:                -109.13
No. Observations:                 402   AIC:                             230.3
Df Residuals:                     396   BIC:                             254.2
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const               0.1418      0.122      1.158      0.248      -0.099       0.382
Internet           16.8876      4.957      3.407      0.001       7.142      26.633
M&A                34.1071     12.970      2.630      0.009       8.608      59.607
Savings & loans   -21.0211      7.967     -2.639      0.009     -36.684      -5.359
Russia            -24.4088      6.102     -4.000      0.000     -36.405     -12.413
Bankruptcy        -23.8064     14.084     -1.690      0.092     -51.494       3.881
==============================================================================
Omnibus:                        3.670   Durbin-Watson:                   0.718
Prob(Omnibus):                  0.160   Jarque-Bera (JB):                4.350
Skew:                          -0.031   Prob(JB):                        0.114
Kurtosis:                       3.506   Cond. No.                         975.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

R-squared: 0.3299

=== Lasso and OLS for Rubbr_vol ===
Selected alpha: 0.05281079711934331
Selected topics:  ['Fast food', 'Bankruptcy', 'Arts', 'Clintons', 'Mortgages']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Rubbr_vol   R-squared:                       0.251
Model:                            OLS   Adj. R-squared:                  0.241
Method:                 Least Squares   F-statistic:                     26.49
Date:                Tue, 06 May 2025   Prob (F-statistic):           4.17e-23
Time:                        13:08:21   Log-Likelihood:                -57.367
No. Observations:                 402   AIC:                             126.7
Df Residuals:                     396   BIC:                             150.7
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.4089      0.161      2.547      0.011       0.093       0.724
Fast food    -62.2566     20.929     -2.975      0.003    -103.403     -21.110
Bankruptcy    30.8505     10.154      3.038      0.003      10.888      50.813
Arts         -76.6615     16.875     -4.543      0.000    -109.837     -43.486
Clintons     -14.8647      3.962     -3.752      0.000     -22.654      -7.075
Mortgages     19.0095      5.710      3.329      0.001       7.783      30.236
==============================================================================
Omnibus:                       63.880   Durbin-Watson:                   0.920
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              137.148
Skew:                           0.840   Prob(JB):                     1.65e-30
Kurtosis:                       5.317   Cond. No.                     1.51e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.51e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2507

=== Lasso and OLS for Txtls_vol ===
Selected alpha: 0.20565123083486536
Selected topics:  ['Mid-size cities', 'California', 'Futures/indices', 'Acquired investment banks', 'Microchips']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Txtls_vol   R-squared:                       0.480
Model:                            OLS   Adj. R-squared:                  0.474
Method:                 Least Squares   F-statistic:                     73.24
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.51e-54
Time:                        13:08:33   Log-Likelihood:                -217.77
No. Observations:                 402   AIC:                             447.5
Df Residuals:                     396   BIC:                             471.5
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                         1.6727      0.114     14.657      0.000       1.448       1.897
Mid-size cities            -111.4269     28.421     -3.921      0.000    -167.301     -55.553
California                   -1.4719     34.374     -0.043      0.966     -69.049      66.106
Futures/indices            -112.7360     44.047     -2.559      0.011    -199.331     -26.141
Acquired investment banks   -21.6599     19.279     -1.123      0.262     -59.563      16.243
Microchips                 -120.6326     17.911     -6.735      0.000    -155.846     -85.419
==============================================================================
Omnibus:                       37.235   Durbin-Watson:                   0.640
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               52.934
Skew:                           0.656   Prob(JB):                     3.20e-12
Kurtosis:                       4.200   Cond. No.                     2.22e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.22e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4804

=== Lasso and OLS for BldMt_vol ===
Selected alpha: 0.1006938631476027
Selected topics:  ['Mobile devices', 'European sovereign debt', 'Currencies/metals', 'Oil market', 'European politics']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              BldMt_vol   R-squared:                       0.369
Model:                            OLS   Adj. R-squared:                  0.361
Method:                 Least Squares   F-statistic:                     46.39
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.08e-37
Time:                        13:10:03   Log-Likelihood:                -174.87
No. Observations:                 402   AIC:                             361.7
Df Residuals:                     396   BIC:                             385.7
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       0.2109      0.105      2.014      0.045       0.005       0.417
Mobile devices             31.3650      9.889      3.172      0.002      11.923      50.807
European sovereign debt     5.2359      5.967      0.877      0.381      -6.496      16.968
Currencies/metals         -31.6797      8.306     -3.814      0.000     -48.009     -15.351
Oil market                -47.0881      6.494     -7.251      0.000     -59.856     -34.320
European politics          25.5745      8.761      2.919      0.004       8.351      42.797
==============================================================================
Omnibus:                       15.553   Durbin-Watson:                   0.606
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               23.615
Skew:                           0.290   Prob(JB):                     7.45e-06
Kurtosis:                       4.036   Cond. No.                         650.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

R-squared: 0.3694

=== Lasso and OLS for Cnstr_vol ===
Selected alpha: 0.10447659715608042
Selected topics:  ['Executive pay', 'SEC', 'California', 'Clintons', 'Futures/indices']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Cnstr_vol   R-squared:                       0.335
Model:                            OLS   Adj. R-squared:                  0.327
Method:                 Least Squares   F-statistic:                     39.93
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.28e-33
Time:                        13:12:03   Log-Likelihood:                -152.72
No. Observations:                 402   AIC:                             317.4
Df Residuals:                     396   BIC:                             341.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const              -0.2636      0.109     -2.425      0.016      -0.477      -0.050
Executive pay      76.4874     14.110      5.421      0.000      48.748     104.227
SEC               103.4889     18.500      5.594      0.000      67.118     139.860
California        -85.8555     22.807     -3.764      0.000    -130.694     -41.017
Clintons           -8.9093      5.604     -1.590      0.113     -19.927       2.108
Futures/indices   -44.4853     28.774     -1.546      0.123    -101.055      12.084
==============================================================================
Omnibus:                        4.306   Durbin-Watson:                   0.565
Prob(Omnibus):                  0.116   Jarque-Bera (JB):                4.435
Skew:                           0.158   Prob(JB):                        0.109
Kurtosis:                       3.406   Cond. No.                     1.90e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.9e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3352

=== Lasso and OLS for Steel_vol ===
Selected alpha: 0.1176811952434999
Selected topics:  ['Problems', 'China', 'Futures/indices', 'Bush/Obama/Trump', 'Private equity/hedge funds']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Steel_vol   R-squared:                       0.503
Model:                            OLS   Adj. R-squared:                  0.497
Method:                 Least Squares   F-statistic:                     80.27
Date:                Tue, 06 May 2025   Prob (F-statistic):           5.01e-58
Time:                        13:12:17   Log-Likelihood:                -150.27
No. Observations:                 402   AIC:                             312.5
Df Residuals:                     396   BIC:                             336.5
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================================
                                 coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------------
const                          1.2262      0.226      5.416      0.000       0.781       1.671
Problems                    -239.9301     27.899     -8.600      0.000    -294.778    -185.082
China                          9.2455     11.446      0.808      0.420     -13.256      31.747
Futures/indices              -66.5322     32.783     -2.029      0.043    -130.983      -2.082
Bush/Obama/Trump              17.7465      4.524      3.923      0.000       8.853      26.640
Private equity/hedge funds    48.4865      9.883      4.906      0.000      29.057      67.916
==============================================================================
Omnibus:                        5.030   Durbin-Watson:                   0.510
Prob(Omnibus):                  0.081   Jarque-Bera (JB):                5.131
Skew:                           0.262   Prob(JB):                       0.0769
Kurtosis:                       2.820   Cond. No.                     1.94e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.94e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.5033

=== Lasso and OLS for FabPr_vol ===
Selected alpha: 0.10840143591783309
Selected topics:  ['Research', 'Environment ', 'NY politics', 'Immigration', 'Positive sentiment']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              FabPr_vol   R-squared:                       0.382
Model:                            OLS   Adj. R-squared:                  0.374
Method:                 Least Squares   F-statistic:                     48.98
Date:                Tue, 06 May 2025   Prob (F-statistic):           2.01e-39
Time:                        13:14:45   Log-Likelihood:                -357.25
No. Observations:                 402   AIC:                             726.5
Df Residuals:                     396   BIC:                             750.5
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
======================================================================================
                         coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------
const                 -0.7035      0.440     -1.599      0.111      -1.568       0.161
Research              71.3801     53.994      1.322      0.187     -34.771     177.532
Environment           75.1427     25.167      2.986      0.003      25.665     124.620
NY politics          105.0775     16.366      6.420      0.000      72.902     137.253
Immigration           57.9993     30.569      1.897      0.059      -2.098     118.097
Positive sentiment  -162.6716     55.841     -2.913      0.004    -272.454     -52.889
==============================================================================
Omnibus:                        7.308   Durbin-Watson:                   0.635
Prob(Omnibus):                  0.026   Jarque-Bera (JB):                7.145
Skew:                           0.303   Prob(JB):                       0.0281
Kurtosis:                       3.243   Cond. No.                     1.93e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.93e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3821

=== Lasso and OLS for Mach_vol ===
Skipping variable Mach_vol: No alpha found that yields exactly 5 non-zero coefficients.

=== Lasso and OLS for ElcEq_vol ===
Selected alpha: 0.1707352647470692
Selected topics:  ['Mid-size cities', 'International exchanges', 'California', 'Futures/indices', 'National security']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              ElcEq_vol   R-squared:                       0.358
Model:                            OLS   Adj. R-squared:                  0.350
Method:                 Least Squares   F-statistic:                     44.16
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.61e-36
Time:                        13:16:55   Log-Likelihood:                -261.54
No. Observations:                 402   AIC:                             535.1
Df Residuals:                     396   BIC:                             559.1
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                      -0.7528      0.187     -4.036      0.000      -1.120      -0.386
Mid-size cities            67.2659     31.566      2.131      0.034       5.207     129.324
International exchanges    25.6123      8.246      3.106      0.002       9.401      41.823
California                 89.5992     37.027      2.420      0.016      16.806     162.393
Futures/indices           -14.3625     49.768     -0.289      0.773    -112.205      83.480
National security         -34.9084     12.617     -2.767      0.006     -59.712     -10.104
==============================================================================
Omnibus:                        0.501   Durbin-Watson:                   0.610
Prob(Omnibus):                  0.778   Jarque-Bera (JB):                0.618
Skew:                           0.061   Prob(JB):                        0.734
Kurtosis:                       2.851   Cond. No.                     2.22e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.22e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3580

=== Lasso and OLS for Autos_vol ===
Selected alpha: 0.12796968682159415
Selected topics:  ['Small business', 'Treasury bonds', 'Latin America', 'Marketing', 'Automotive']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Autos_vol   R-squared:                       0.288
Model:                            OLS   Adj. R-squared:                  0.279
Method:                 Least Squares   F-statistic:                     31.97
Date:                Tue, 06 May 2025   Prob (F-statistic):           2.30e-27
Time:                        13:19:16   Log-Likelihood:                -203.64
No. Observations:                 402   AIC:                             419.3
Df Residuals:                     396   BIC:                             443.3
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const             -1.0421      0.228     -4.573      0.000      -1.490      -0.594
Small business   125.3828     34.392      3.646      0.000      57.768     192.997
Treasury bonds     6.6424      5.153      1.289      0.198      -3.488      16.773
Latin America    -68.4254     20.468     -3.343      0.001    -108.666     -28.185
Marketing         66.4955     15.123      4.397      0.000      36.764      96.227
Automotive        46.7147     12.493      3.739      0.000      22.154      71.275
==============================================================================
Omnibus:                        4.189   Durbin-Watson:                   0.693
Prob(Omnibus):                  0.123   Jarque-Bera (JB):                4.258
Skew:                           0.247   Prob(JB):                        0.119
Kurtosis:                       2.898   Cond. No.                     1.73e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.73e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2876

=== Lasso and OLS for Aero_vol ===
Skipping variable Aero_vol: No alpha found that yields exactly 5 non-zero coefficients.

=== Lasso and OLS for Ships_vol ===
Skipping variable Ships_vol: No alpha found that yields exactly 5 non-zero coefficients.

=== Lasso and OLS for Guns_vol ===
Selected alpha: 0.1707352647470692
Selected topics:  ['Research', 'Schools', 'Humor/language', 'Options/VIX', 'European politics']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Guns_vol   R-squared:                       0.302
Model:                            OLS   Adj. R-squared:                  0.294
Method:                 Least Squares   F-statistic:                     34.34
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.84e-29
Time:                        13:24:52   Log-Likelihood:                -316.45
No. Observations:                 402   AIC:                             644.9
Df Residuals:                     396   BIC:                             668.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                -0.0421      0.372     -0.113      0.910      -0.774       0.690
Research           -165.1512     42.523     -3.884      0.000    -248.750     -81.553
Schools            -109.1593     21.773     -5.013      0.000    -151.965     -66.354
Humor/language      186.4409     38.577      4.833      0.000     110.599     262.283
Options/VIX          48.5696     15.863      3.062      0.002      17.383      79.757
European politics   -15.8633     11.946     -1.328      0.185     -39.350       7.623
==============================================================================
Omnibus:                        6.628   Durbin-Watson:                   0.611
Prob(Omnibus):                  0.036   Jarque-Bera (JB):                6.771
Skew:                           0.302   Prob(JB):                       0.0339
Kurtosis:                       2.803   Cond. No.                     1.61e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.61e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3024

=== Lasso and OLS for Gold_vol ===
Selected alpha: 0.0952750047242729
Selected topics:  ['Small caps', 'Company spokesperson', 'Publishing', 'NY politics', 'Rail/trucking/shipping']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Gold_vol   R-squared:                       0.219
Model:                            OLS   Adj. R-squared:                  0.209
Method:                 Least Squares   F-statistic:                     22.18
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.30e-19
Time:                        13:27:00   Log-Likelihood:                -287.43
No. Observations:                 402   AIC:                             586.9
Df Residuals:                     396   BIC:                             610.8
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==========================================================================================
                             coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------------
const                      0.2128      0.358      0.594      0.553      -0.492       0.917
Small caps               -20.2534      6.451     -3.140      0.002     -32.936      -7.571
Company spokesperson     101.0542     53.078      1.904      0.058      -3.295     205.403
Publishing              -145.2553     29.568     -4.913      0.000    -203.386     -87.125
NY politics               -1.8140     13.757     -0.132      0.895     -28.860      25.232
Rail/trucking/shipping    71.9547     28.405      2.533      0.012      16.111     127.798
==============================================================================
Omnibus:                        6.122   Durbin-Watson:                   0.567
Prob(Omnibus):                  0.047   Jarque-Bera (JB):                6.176
Skew:                           0.303   Prob(JB):                       0.0456
Kurtosis:                       2.968   Cond. No.                     2.15e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.15e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2188

=== Lasso and OLS for Mines_vol ===
Selected alpha: 0.14174741629268062
Selected topics:  ['Mining', 'China', 'Futures/indices', 'Mortgages', 'Private equity/hedge funds']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Mines_vol   R-squared:                       0.644
Model:                            OLS   Adj. R-squared:                  0.640
Method:                 Least Squares   F-statistic:                     143.5
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.43e-86
Time:                        13:27:09   Log-Likelihood:                -175.61
No. Observations:                 402   AIC:                             363.2
Df Residuals:                     396   BIC:                             387.2
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================================
                                 coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------------
const                         -0.3643      0.229     -1.590      0.113      -0.815       0.086
Mining                       169.3904     21.883      7.741      0.000     126.368     212.413
China                         29.9318     11.842      2.528      0.012       6.650      53.213
Futures/indices             -159.1212     35.001     -4.546      0.000    -227.933     -90.309
Mortgages                     40.9757      9.972      4.109      0.000      21.371      60.580
Private equity/hedge funds    20.3996     12.438      1.640      0.102      -4.054      44.853
==============================================================================
Omnibus:                        0.291   Durbin-Watson:                   0.739
Prob(Omnibus):                  0.865   Jarque-Bera (JB):                0.416
Skew:                           0.000   Prob(JB):                        0.812
Kurtosis:                       2.842   Cond. No.                     1.95e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.95e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.6443

=== Lasso and OLS for Coal_vol ===
Selected alpha: 0.20565123083486536
Selected topics:  ['Changes', 'Treasury bonds', 'Immigration', 'China', 'Commodities']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Coal_vol   R-squared:                       0.618
Model:                            OLS   Adj. R-squared:                  0.613
Method:                 Least Squares   F-statistic:                     127.9
Date:                Tue, 06 May 2025   Prob (F-statistic):           2.35e-80
Time:                        13:27:19   Log-Likelihood:                -210.54
No. Observations:                 402   AIC:                             433.1
Df Residuals:                     396   BIC:                             457.1
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const             -0.5738      0.331     -1.735      0.083      -1.224       0.076
Changes           42.1201     54.752      0.769      0.442     -65.520     149.760
Treasury bonds   -24.6641      9.721     -2.537      0.012     -43.776      -5.552
Immigration       96.4100     18.644      5.171      0.000      59.756     133.064
China             63.3199     12.823      4.938      0.000      38.110      88.530
Commodities      -27.7184     19.670     -1.409      0.160     -66.390      10.953
==============================================================================
Omnibus:                        0.828   Durbin-Watson:                   0.429
Prob(Omnibus):                  0.661   Jarque-Bera (JB):                0.742
Skew:                           0.105   Prob(JB):                        0.690
Kurtosis:                       3.022   Cond. No.                     2.71e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.71e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.6175

=== Lasso and OLS for Oil_vol ===
Selected alpha: 0.1124737178364752
Selected topics:  ['M&A', 'Problems', 'Private/public sector', 'Financial crisis', 'Oil market']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Oil_vol   R-squared:                       0.496
Model:                            OLS   Adj. R-squared:                  0.489
Method:                 Least Squares   F-statistic:                     77.85
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.01e-56
Time:                        13:29:29   Log-Likelihood:                -175.38
No. Observations:                 402   AIC:                             362.8
Df Residuals:                     396   BIC:                             386.7
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
=========================================================================================
                            coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------------
const                     0.0867      0.256      0.339      0.735      -0.416       0.589
M&A                      81.4244     14.518      5.608      0.000      52.882     109.967
Problems               -139.2191     30.500     -4.565      0.000    -199.181     -79.257
Private/public sector   -40.3460     26.276     -1.535      0.125     -92.004      11.312
Financial crisis        -17.5680      5.331     -3.295      0.001     -28.049      -7.087
Oil market              106.6392      6.643     16.052      0.000      93.579     119.700
==============================================================================
Omnibus:                        3.876   Durbin-Watson:                   0.767
Prob(Omnibus):                  0.144   Jarque-Bera (JB):                3.928
Skew:                           0.238   Prob(JB):                        0.140
Kurtosis:                       2.910   Cond. No.                     1.67e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.67e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4957

=== Lasso and OLS for Util_vol ===
Selected alpha: 0.10256779307444219
Selected topics:  ['Music industry', 'Treasury bonds', 'Challenges', 'National security', 'Revenue growth']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               Util_vol   R-squared:                       0.456
Model:                            OLS   Adj. R-squared:                  0.449
Method:                 Least Squares   F-statistic:                     66.35
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.06e-50
Time:                        13:31:45   Log-Likelihood:                -166.46
No. Observations:                 402   AIC:                             344.9
Df Residuals:                     396   BIC:                             368.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                -0.7798      0.291     -2.679      0.008      -1.352      -0.208
Music industry       62.0013     24.894      2.491      0.013      13.060     110.942
Treasury bonds      -31.8819      7.244     -4.401      0.000     -46.124     -17.640
Challenges          103.3921     41.731      2.478      0.014      21.350     185.435
National security    32.1214      9.780      3.284      0.001      12.894      51.349
Revenue growth       22.6613     24.738      0.916      0.360     -25.973      71.296
==============================================================================
Omnibus:                       11.470   Durbin-Watson:                   0.539
Prob(Omnibus):                  0.003   Jarque-Bera (JB):               11.578
Skew:                           0.387   Prob(JB):                      0.00306
Kurtosis:                       2.696   Cond. No.                     2.28e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.28e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4559

=== Lasso and OLS for Telcm_vol ===
Selected alpha: 0.14174741629268062
Selected topics:  ['Mobile devices', 'Programs/initiatives', 'China', 'Humor/language', 'Futures/indices']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Telcm_vol   R-squared:                       0.215
Model:                            OLS   Adj. R-squared:                  0.205
Method:                 Least Squares   F-statistic:                     21.66
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.52e-19
Time:                        13:31:53   Log-Likelihood:                -333.47
No. Observations:                 402   AIC:                             678.9
Df Residuals:                     396   BIC:                             702.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                   -0.6299      0.509     -1.238      0.217      -1.630       0.371
Mobile devices         -14.9870     17.507     -0.856      0.392     -49.405      19.431
Programs/initiatives   -75.7559     66.395     -1.141      0.255    -206.287      54.776
China                  -25.2521     19.121     -1.321      0.187     -62.843      12.339
Humor/language         141.8747     41.923      3.384      0.001      59.455     224.294
Futures/indices         39.0398     53.194      0.734      0.463     -65.539     143.618
==============================================================================
Omnibus:                       45.924   Durbin-Watson:                   0.490
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               69.029
Skew:                           0.753   Prob(JB):                     1.02e-15
Kurtosis:                       4.361   Cond. No.                     2.45e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.45e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2148

=== Lasso and OLS for PerSv_vol ===
Selected alpha: 0.07225349491787214
Selected topics:  ['Environment ', 'Venture capital', 'Financial crisis', 'Foods/consumer goods', 'Trading activity']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              PerSv_vol   R-squared:                       0.259
Model:                            OLS   Adj. R-squared:                  0.250
Method:                 Least Squares   F-statistic:                     27.68
Date:                Tue, 06 May 2025   Prob (F-statistic):           4.83e-24
Time:                        13:33:03   Log-Likelihood:                -150.25
No. Observations:                 402   AIC:                             312.5
Df Residuals:                     396   BIC:                             336.5
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                    0.8142      0.154      5.301      0.000       0.512       1.116
Environment            -67.0191     15.350     -4.366      0.000     -97.196     -36.842
Venture capital        -83.3629     20.410     -4.084      0.000    -123.488     -43.237
Financial crisis        25.3322      5.217      4.856      0.000      15.076      35.589
Foods/consumer goods   -31.0021     19.480     -1.592      0.112     -69.298       7.294
Trading activity       -20.0314      7.306     -2.742      0.006     -34.394      -5.668
==============================================================================
Omnibus:                       43.314   Durbin-Watson:                   0.663
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               61.536
Skew:                           0.744   Prob(JB):                     4.34e-14
Kurtosis:                       4.209   Cond. No.                     1.25e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.25e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.2590

=== Lasso and OLS for BusSv_vol ===
Selected alpha: 0.07225349491787214
Selected topics:  ['Electronics', 'US defense', 'Health insurance', 'SEC', 'Accounting']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              BusSv_vol   R-squared:                       0.410
Model:                            OLS   Adj. R-squared:                  0.402
Method:                 Least Squares   F-statistic:                     54.97
Date:                Tue, 06 May 2025   Prob (F-statistic):           2.63e-43
Time:                        13:34:04   Log-Likelihood:                 20.625
No. Observations:                 402   AIC:                            -29.25
Df Residuals:                     396   BIC:                            -5.271
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
const               -0.1358      0.095     -1.432      0.153      -0.322       0.051
Electronics        -77.8155     10.223     -7.612      0.000     -97.913     -57.718
US defense          18.3656      4.547      4.039      0.000       9.427      27.304
Health insurance   -19.5711      5.054     -3.873      0.000     -29.507      -9.636
SEC                 42.1848     12.905      3.269      0.001      16.814      67.555
Accounting          37.8611      5.505      6.877      0.000      27.038      48.684
==============================================================================
Omnibus:                       15.664   Durbin-Watson:                   0.931
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               16.625
Skew:                           0.497   Prob(JB):                     0.000245
Kurtosis:                       3.076   Cond. No.                     1.16e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.16e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4097

=== Lasso and OLS for Hardw_vol ===
Selected alpha: 0.20565123083486536
Selected topics:  ['Phone companies', 'Tobacco', 'Oil market', 'Microchips', 'NASD']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Hardw_vol   R-squared:                       0.344
Model:                            OLS   Adj. R-squared:                  0.335
Method:                 Least Squares   F-statistic:                     41.48
Date:                Tue, 06 May 2025   Prob (F-statistic):           2.63e-34
Time:                        13:34:14   Log-Likelihood:                -371.79
No. Observations:                 402   AIC:                             755.6
Df Residuals:                     396   BIC:                             779.6
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const              -0.6713      0.154     -4.364      0.000      -0.974      -0.369
Phone companies    41.2305     17.763      2.321      0.021       6.310      76.152
Tobacco            80.3037     24.771      3.242      0.001      31.605     129.003
Oil market        -54.6811     11.063     -4.943      0.000     -76.430     -32.932
Microchips         36.0469     34.451      1.046      0.296     -31.683     103.777
NASD               51.7616     12.524      4.133      0.000      27.139      76.384
==============================================================================
Omnibus:                       37.298   Durbin-Watson:                   0.461
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               46.591
Skew:                           0.730   Prob(JB):                     7.64e-11
Kurtosis:                       3.804   Cond. No.                     1.20e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.2e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3437

=== Lasso and OLS for Softw_vol ===
Selected alpha: 0.14560059950206486
Selected topics:  ['Key role', 'Justice Department', 'China', 'Futures/indices', 'Acquired investment banks']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Softw_vol   R-squared:                       0.618
Model:                            OLS   Adj. R-squared:                  0.614
Method:                 Least Squares   F-statistic:                     128.3
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.49e-80
Time:                        13:35:34   Log-Likelihood:                -97.717
No. Observations:                 402   AIC:                             207.4
Df Residuals:                     396   BIC:                             231.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
=============================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------------
const                        -0.2175      0.261     -0.833      0.406      -0.731       0.296
Key role                   -108.7556     43.715     -2.488      0.013    -194.699     -22.813
Justice Department          -54.7319     11.126     -4.919      0.000     -76.605     -32.859
China                       -15.5941      9.874     -1.579      0.115     -35.006       3.818
Futures/indices             178.3602     33.742      5.286      0.000     112.025     244.696
Acquired investment banks    20.7860     14.181      1.466      0.143      -7.093      48.665
==============================================================================
Omnibus:                        6.021   Durbin-Watson:                   0.591
Prob(Omnibus):                  0.049   Jarque-Bera (JB):                6.085
Skew:                           0.301   Prob(JB):                       0.0477
Kurtosis:                       2.956   Cond. No.                     2.85e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.85e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.6184

=== Lasso and OLS for Chips_vol ===
Selected alpha: 0.17508270317357252
Selected topics:  ['Small caps', 'Mining', 'Phone companies', 'Bank loans', 'NASD']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Chips_vol   R-squared:                       0.441
Model:                            OLS   Adj. R-squared:                  0.434
Method:                 Least Squares   F-statistic:                     62.58
Date:                Tue, 06 May 2025   Prob (F-statistic):           5.30e-48
Time:                        13:37:00   Log-Likelihood:                -219.72
No. Observations:                 402   AIC:                             451.4
Df Residuals:                     396   BIC:                             475.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const               0.4860      0.172      2.825      0.005       0.148       0.824
Small caps          5.7172      6.391      0.895      0.372      -6.848      18.282
Mining            -96.0736     23.654     -4.062      0.000    -142.576     -49.571
Phone companies    39.6910     11.757      3.376      0.001      16.577      62.805
Bank loans        -85.7936     14.332     -5.986      0.000    -113.969     -57.618
NASD               36.5137      9.237      3.953      0.000      18.354      54.674
==============================================================================
Omnibus:                        2.378   Durbin-Watson:                   0.441
Prob(Omnibus):                  0.305   Jarque-Bera (JB):                2.124
Skew:                          -0.144   Prob(JB):                        0.346
Kurtosis:                       3.209   Cond. No.                     1.14e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.14e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4414

=== Lasso and OLS for LabEq_vol ===
Selected alpha: 0.3158635408267819
Selected topics:  ['Record high', 'Bond yields', 'Health insurance', 'SEC', 'Reagan']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              LabEq_vol   R-squared:                       0.540
Model:                            OLS   Adj. R-squared:                  0.534
Method:                 Least Squares   F-statistic:                     92.96
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.45e-64
Time:                        13:38:31   Log-Likelihood:                -353.22
No. Observations:                 402   AIC:                             718.4
Df Residuals:                     396   BIC:                             742.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
const                0.4879      0.325      1.502      0.134      -0.151       1.126
Record high       -116.9397     42.164     -2.773      0.006    -199.833     -34.046
Bond yields        -89.7098     17.639     -5.086      0.000    -124.387     -55.033
Health insurance   -70.0818     13.458     -5.207      0.000     -96.540     -43.624
SEC                148.1263     30.376      4.876      0.000      88.408     207.845
Reagan              49.8116      9.159      5.438      0.000      31.805      67.818
==============================================================================
Omnibus:                       12.504   Durbin-Watson:                   0.505
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               13.043
Skew:                           0.441   Prob(JB):                      0.00147
Kurtosis:                       3.032   Cond. No.                     1.46e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.46e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.5400

=== Lasso and OLS for Paper_vol ===
Selected alpha: 0.08111308307896872
Selected topics:  ['M&A', 'Exchanges/composites', 'Bush/Obama/Trump', 'Microchips', 'Iraq']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Paper_vol   R-squared:                       0.427
Model:                            OLS   Adj. R-squared:                  0.420
Method:                 Least Squares   F-statistic:                     59.11
Date:                Tue, 06 May 2025   Prob (F-statistic):           6.80e-46
Time:                        13:38:39   Log-Likelihood:                 65.082
No. Observations:                 402   AIC:                            -118.2
Df Residuals:                     396   BIC:                            -94.19
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                   -0.3704      0.060     -6.125      0.000      -0.489      -0.252
M&A                     28.8279      9.617      2.998      0.003       9.921      47.735
Exchanges/composites    19.6983      6.641      2.966      0.003       6.641      32.755
Bush/Obama/Trump        -9.5976      2.819     -3.405      0.001     -15.139      -4.056
Microchips              33.2062     11.419      2.908      0.004      10.757      55.656
Iraq                   -11.6066      2.048     -5.668      0.000     -15.632      -7.581
==============================================================================
Omnibus:                        2.386   Durbin-Watson:                   0.649
Prob(Omnibus):                  0.303   Jarque-Bera (JB):                2.429
Skew:                          -0.185   Prob(JB):                        0.297
Kurtosis:                       2.909   Cond. No.                     1.30e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.3e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4274

=== Lasso and OLS for Boxes_vol ===
Selected alpha: 0.09770099572992257
Selected topics:  ['Company spokesperson', 'Marketing', 'International exchanges', 'Utilities', 'Trading activity']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Boxes_vol   R-squared:                       0.322
Model:                            OLS   Adj. R-squared:                  0.314
Method:                 Least Squares   F-statistic:                     37.64
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.43e-31
Time:                        13:38:46   Log-Likelihood:                -267.58
No. Observations:                 402   AIC:                             547.2
Df Residuals:                     396   BIC:                             571.1
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       0.5381      0.277      1.946      0.052      -0.006       1.082
Company spokesperson     -163.8172     51.929     -3.155      0.002    -265.908     -61.727
Marketing                  40.3262     22.628      1.782      0.075      -4.161      84.813
International exchanges     9.2380      8.948      1.032      0.303      -8.354      26.830
Utilities                 -75.0691     15.816     -4.746      0.000    -106.164     -43.974
Trading activity           40.7987     11.636      3.506      0.001      17.922      63.676
==============================================================================
Omnibus:                       12.890   Durbin-Watson:                   0.629
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               16.597
Skew:                           0.299   Prob(JB):                     0.000249
Kurtosis:                       3.796   Cond. No.                     2.22e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.22e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3222

=== Lasso and OLS for Trans_vol ===
Selected alpha: 0.06734150657750829
Selected topics:  ['M&A', 'Control stakes', 'Iraq', 'Buffett', 'Lawsuits']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Trans_vol   R-squared:                       0.176
Model:                            OLS   Adj. R-squared:                  0.165
Method:                 Least Squares   F-statistic:                     16.90
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.81e-15
Time:                        13:38:53   Log-Likelihood:                -190.93
No. Observations:                 402   AIC:                             393.9
Df Residuals:                     396   BIC:                             417.8
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const             -0.8733      0.328     -2.663      0.008      -1.518      -0.228
M&A               27.6808     15.692      1.764      0.079      -3.170      58.532
Control stakes   109.0254     26.200      4.161      0.000      57.516     160.535
Iraq             -13.0361      3.898     -3.345      0.001     -20.699      -5.374
Buffett          183.7091     65.230      2.816      0.005      55.468     311.950
Lawsuits         -59.4517     11.550     -5.147      0.000     -82.159     -36.745
==============================================================================
Omnibus:                       30.452   Durbin-Watson:                   0.743
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               43.191
Skew:                           0.558   Prob(JB):                     4.18e-10
Kurtosis:                       4.155   Cond. No.                     3.34e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.34e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.1758

=== Lasso and OLS for Whlsl_vol ===
Selected alpha: 0.08111308307896872
Selected topics:  ['Small business', 'Japan', 'Airlines', 'Utilities', 'Options/VIX']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Whlsl_vol   R-squared:                       0.331
Model:                            OLS   Adj. R-squared:                  0.323
Method:                 Least Squares   F-statistic:                     39.26
Date:                Tue, 06 May 2025   Prob (F-statistic):           9.81e-33
Time:                        13:38:59   Log-Likelihood:                -80.197
No. Observations:                 402   AIC:                             172.4
Df Residuals:                     396   BIC:                             196.4
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==================================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------
const             -0.4352      0.143     -3.044      0.002      -0.716      -0.154
Small business   -62.7024     25.335     -2.475      0.014    -112.511     -12.894
Japan            -63.7016     10.340     -6.161      0.000     -84.030     -43.373
Airlines          36.9288      9.267      3.985      0.000      18.710      55.148
Utilities         60.5999      9.533      6.357      0.000      41.859      79.341
Options/VIX       51.7008      8.284      6.241      0.000      35.414      67.988
==============================================================================
Omnibus:                       50.145   Durbin-Watson:                   0.741
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               98.576
Skew:                           0.702   Prob(JB):                     3.93e-22
Kurtosis:                       4.978   Cond. No.                     1.74e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.74e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3314

=== Lasso and OLS for Rtail_vol ===
Selected alpha: 0.06734150657750829
Selected topics:  ['Electronics', 'Broadcasting', 'Schools', 'Germany', 'Oil market']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Rtail_vol   R-squared:                       0.190
Model:                            OLS   Adj. R-squared:                  0.179
Method:                 Least Squares   F-statistic:                     18.55
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.46e-16
Time:                        13:39:07   Log-Likelihood:                -174.98
No. Observations:                 402   AIC:                             362.0
Df Residuals:                     396   BIC:                             385.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
const           -0.4402      0.177     -2.493      0.013      -0.787      -0.093
Electronics     79.5266     18.673      4.259      0.000      42.816     116.237
Broadcasting    36.4618     16.592      2.197      0.029       3.841      69.082
Schools        -25.5312     14.929     -1.710      0.088     -54.882       3.820
Germany        -36.4689     13.817     -2.639      0.009     -63.633      -9.305
Oil market      27.5378      6.317      4.359      0.000      15.118      39.957
==============================================================================
Omnibus:                        0.375   Durbin-Watson:                   0.675
Prob(Omnibus):                  0.829   Jarque-Bera (JB):                0.437
Skew:                           0.071   Prob(JB):                        0.804
Kurtosis:                       2.924   Cond. No.                     1.14e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.14e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.1897

=== Lasso and OLS for Meals_vol ===
Selected alpha: 0.10642092440647247
Selected topics:  ['Company spokesperson', 'Pharma', 'Marketing', 'Systems', 'Reagan']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Meals_vol   R-squared:                       0.307
Model:                            OLS   Adj. R-squared:                  0.298
Method:                 Least Squares   F-statistic:                     35.10
Date:                Tue, 06 May 2025   Prob (F-statistic):           1.04e-29
Time:                        13:40:24   Log-Likelihood:                -214.12
No. Observations:                 402   AIC:                             440.2
Df Residuals:                     396   BIC:                             464.2
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
========================================================================================
                           coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------
const                    1.0199      0.362      2.816      0.005       0.308       1.732
Company spokesperson  -121.4445     48.115     -2.524      0.012    -216.037     -26.852
Pharma                  26.8174     16.686      1.607      0.109      -5.987      59.622
Marketing               79.8929     17.562      4.549      0.000      45.366     114.420
Systems               -212.2434     43.762     -4.850      0.000    -298.277    -126.209
Reagan                 -19.2613      6.440     -2.991      0.003     -31.922      -6.601
==============================================================================
Omnibus:                        8.743   Durbin-Watson:                   0.647
Prob(Omnibus):                  0.013   Jarque-Bera (JB):                9.060
Skew:                           0.297   Prob(JB):                       0.0108
Kurtosis:                       3.434   Cond. No.                     2.35e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.35e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3071

=== Lasso and OLS for Banks_vol ===
Selected alpha: 0.14174741629268062
Selected topics:  ['Financial crisis', 'SEC', 'Accounting', 'Options/VIX', 'NASD']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Banks_vol   R-squared:                       0.565
Model:                            OLS   Adj. R-squared:                  0.559
Method:                 Least Squares   F-statistic:                     102.8
Date:                Tue, 06 May 2025   Prob (F-statistic):           2.57e-69
Time:                        13:40:30   Log-Likelihood:                -220.85
No. Observations:                 402   AIC:                             453.7
Df Residuals:                     396   BIC:                             477.7
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
const                0.5944      0.125      4.751      0.000       0.348       0.840
Financial crisis    65.1358      5.361     12.150      0.000      54.596      75.675
SEC                -49.9795     24.683     -2.025      0.044     -98.506      -1.453
Accounting         -39.0985     10.388     -3.764      0.000     -59.520     -18.677
Options/VIX        -58.1992     12.696     -4.584      0.000     -83.160     -33.239
NASD               -31.5583      8.147     -3.874      0.000     -47.575     -15.541
==============================================================================
Omnibus:                        9.988   Durbin-Watson:                   0.491
Prob(Omnibus):                  0.007   Jarque-Bera (JB):               10.128
Skew:                           0.346   Prob(JB):                      0.00632
Kurtosis:                       3.356   Cond. No.                     1.22e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.22e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.5648

=== Lasso and OLS for Insur_vol ===
Selected alpha: 0.09770099572992257
Selected topics:  ['Credit ratings', 'Company spokesperson', 'Financial crisis', 'International exchanges', 'Bank loans']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Insur_vol   R-squared:                       0.336
Model:                            OLS   Adj. R-squared:                  0.328
Method:                 Least Squares   F-statistic:                     40.09
Date:                Tue, 06 May 2025   Prob (F-statistic):           2.50e-33
Time:                        13:40:39   Log-Likelihood:                -165.89
No. Observations:                 402   AIC:                             343.8
Df Residuals:                     396   BIC:                             367.8
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                      -0.9268      0.211     -4.385      0.000      -1.342      -0.511
Credit ratings             47.5366     16.790      2.831      0.005      14.527      80.546
Company spokesperson      109.7515     39.920      2.749      0.006      31.269     188.234
Financial crisis           21.7628      4.937      4.408      0.000      12.056      31.470
International exchanges   -21.7756      4.731     -4.603      0.000     -31.076     -12.475
Bank loans                 32.9125     13.077      2.517      0.012       7.203      58.622
==============================================================================
Omnibus:                       26.684   Durbin-Watson:                   0.552
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               43.781
Skew:                           0.449   Prob(JB):                     3.11e-10
Kurtosis:                       4.345   Cond. No.                     2.20e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.2e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3361

=== Lasso and OLS for RlEst_vol ===
Selected alpha: 0.09770099572992257
Selected topics:  ['Publishing', 'Automotive', 'International exchanges', 'Mortgages', 'National security']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              RlEst_vol   R-squared:                       0.399
Model:                            OLS   Adj. R-squared:                  0.391
Method:                 Least Squares   F-statistic:                     52.50
Date:                Tue, 06 May 2025   Prob (F-statistic):           9.96e-42
Time:                        13:40:49   Log-Likelihood:                -180.92
No. Observations:                 402   AIC:                             373.8
Df Residuals:                     396   BIC:                             397.8
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                      -1.3531      0.180     -7.526      0.000      -1.707      -1.000
Publishing                 38.0157     21.974      1.730      0.084      -5.185      81.216
Automotive                 71.8910     11.672      6.159      0.000      48.945      94.837
International exchanges    31.6433      4.997      6.332      0.000      21.819      41.468
Mortgages                  64.2237      7.983      8.045      0.000      48.529      79.918
National security         -14.9892      9.927     -1.510      0.132     -34.506       4.527
==============================================================================
Omnibus:                       17.871   Durbin-Watson:                   0.594
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               18.988
Skew:                           0.512   Prob(JB):                     7.53e-05
Kurtosis:                       3.291   Cond. No.                     1.17e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.17e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.3987

=== Lasso and OLS for Fin_vol ===
Selected alpha: 0.14174741629268062
Selected topics:  ['Canada/South Africa', 'Mortgages', 'Subsidiaries', 'Taxes', 'Private equity/hedge funds']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                Fin_vol   R-squared:                       0.420
Model:                            OLS   Adj. R-squared:                  0.412
Method:                 Least Squares   F-statistic:                     57.28
Date:                Tue, 06 May 2025   Prob (F-statistic):           9.28e-45
Time:                        13:40:57   Log-Likelihood:                -171.94
No. Observations:                 402   AIC:                             355.9
Df Residuals:                     396   BIC:                             379.9
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================================
                                 coef    std err          t      P>|t|      [0.025      0.975]
----------------------------------------------------------------------------------------------
const                          0.6703      0.177      3.779      0.000       0.322       1.019
Canada/South Africa          -54.5231     23.103     -2.360      0.019     -99.942      -9.104
Mortgages                     46.5666      9.040      5.151      0.000      28.793      64.340
Subsidiaries                 -91.8257     30.846     -2.977      0.003    -152.467     -31.184
Taxes                        -33.8101      7.197     -4.698      0.000     -47.959     -19.662
Private equity/hedge funds     8.1699     10.925      0.748      0.455     -13.308      29.648
==============================================================================
Omnibus:                        5.164   Durbin-Watson:                   0.534
Prob(Omnibus):                  0.076   Jarque-Bera (JB):                4.933
Skew:                           0.259   Prob(JB):                       0.0849
Kurtosis:                       3.159   Cond. No.                     1.78e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.78e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.4197

=== Lasso and OLS for Other_vol ===
Selected alpha: 0.125631660247412
Selected topics:  ['Treasury bonds', 'Japan', 'International exchanges', 'Futures/indices', 'Elections']

OLS Summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              Other_vol   R-squared:                       0.608
Model:                            OLS   Adj. R-squared:                  0.603
Method:                 Least Squares   F-statistic:                     122.6
Date:                Tue, 06 May 2025   Prob (F-statistic):           3.67e-78
Time:                        13:42:11   Log-Likelihood:                -151.32
No. Observations:                 402   AIC:                             314.6
Df Residuals:                     396   BIC:                             338.6
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                      -1.1978      0.105    -11.376      0.000      -1.405      -0.991
Treasury bonds             12.0763      6.098      1.980      0.048       0.087      24.065
Japan                      69.9089     15.787      4.428      0.000      38.873     100.945
International exchanges     8.4913      6.399      1.327      0.185      -4.088      21.071
Futures/indices           196.9518     34.357      5.732      0.000     129.406     264.498
Elections                 -11.1974      2.069     -5.413      0.000     -15.264      -7.131
==============================================================================
Omnibus:                       21.890   Durbin-Watson:                   0.748
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               30.689
Skew:                           0.430   Prob(JB):                     2.17e-07
Kurtosis:                       4.045   Cond. No.                     1.96e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.96e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

R-squared: 0.6076