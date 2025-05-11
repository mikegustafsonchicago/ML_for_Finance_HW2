P1:

Data:   ../macro.csv
        ../topics.csv    

(a) Lasso and OLS on Topics

Using the mret (market return) column from macro.csv, fit Lasso regression across a range of penalty parameters.

Select the penalty that yields five non-zero coefficients.

Run OLS using these five topics.

Report the R² and interpret the selected topics.

(b) Repeat for Other Outcomes

Repeat the procedure for the following variables:

vol

indpro

indprol1 (industrial production growth one period into the future)

each indvol column

Interpret the informativeness of topics for each outcome.

(c) Forecasting Industrial Production Growth

Based on what you learned in Problem Set 1, forecast industrial production growth in real time.

Provide reasoning for your modeling decisions.

(d) Document-Term Matrix from WSJ Headlines

Data: ../articles.pq (WSJ headlines)

Using CountVectorizer from sklearn, build a document-term matrix for the WSJ headlines.

(e) Repeat Analysis with Counts

Using the raw count matrix, repeat the analyses from parts (a) and (b).

Questions to answer:

How many non-zero counts are needed to recover the same R²?

What does this imply about the informativeness of counts vs. topics?

(f) Forecasting with Counts

Using the counts, build the best forecasting model for industrial production growth.

Compare your results relative to the topics approach.

(g) TF-IDF Analysis

Convert the raw counts into TF-IDF representation. And repeat the exercises from part (e) and (d). Summarize the differences between the TF-IDF and raw count approaches. Which terms are most important in either approach?