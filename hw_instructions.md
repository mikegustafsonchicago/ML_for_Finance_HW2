Problem Set 2

Business 35137Spring 2025Due: May 5th

1. Topics and Counts Forecasting

Download the following files from Canvas:

topics.csv (labeled attention to topics from structureofnews.com)

macro.csv (financial and macroeconomic outcome variables)

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

Download articles.pq (WSJ headlines) from Canvas.

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

Convert the raw counts into TF-IDF representation.

Repeat the analyses from parts (e) and (f).

Summarize:

Differences between TF-IDF and raw counts.

Identify the most important terms in either approach.

2. Topic Generation with LLMs

Using articles.pq and the generation.py script from Canvas:

(a) Prompt-Based Generation

Attempt to craft a prompt that generates the topics discovered in 1(a) and 1(b).

You may need to:

Generate article-level predictions.

Aggregate up to the monthly frequency.

Report the R² achieved.

(b) Exploring Prompt Engineering

How much does prompt engineering change results? Explore:

i. Persona approach:

Convince the LLM to behave like a "bull" or "bear".

Measure the impact on the results.

ii. Temperature control:

Adjust the temperature to control randomness.

Analyze how results change across multiple generations.

iii. Mitigating Lookahead Bias:

Test LLM behavior with articles around the Global Financial Crisis.

By instructing the LLM to ignore future information, can you mitigate lookahead bias?

(c) Forecasting with Generated Topics

Using the generation approach, attempt to forecast industrial production growth.

Document your approach and reasoning.

3. Embedding-Based Approaches

Using articles.pq and the embeddings.py script from Canvas:

(a) Embedding Regression

Form embeddings for WSJ headlines.

Repeat the analyses from parts 1(a) and 1(b) using the embeddings.

Compare performance relative to using topics.

(b) Topic Recovery

Select a few representative topics from topics.csv.

Test if you can recover these topics using the embeddings.

(c) Recovery of Generated Series

How well can you recover the generated series from part 2 using the embeddings?

(d) Forecasting with Embeddings

Using the embeddings, attempt to forecast industrial production growth.

Document your approach and reasoning.

