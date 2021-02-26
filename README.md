### Project 3: Classification using Natural Language Processing


### Problem Statement

Build an algorithm which will accurately classify  short texts based on whether its author is a man or a woman*.
Possible real-life applications of the algorithm include:
- Data enrichment (e.g. medical survey entries with missing information)
- Prevention of social engineering (catfishing)
- Digital marketing (targeting of men and women with different content)

* Disclaimer: While gender is understood to not be a binary construct,  this project is set up as a binary classification.

### Summary

The project  consisted of five distinct steps, each of which is documented in a separate notebook (all included in the `code` subfolder):
1. Data Harvesting: code used to pull data from two chosen subreddits and export the "raw" datasets into csv files
2. Data Cleaning : code used to remove stop words, links, repeated characters, etc., from the data, leading to creation of cleaner corpora in step 3
3. Exploratory Analysis (incl. Feature Engineering): code applied to evaluate distributions of characteristics such as length of post / comment, build and analyze both corpora by looking at individual words, bigrams, trigrams, and emoji, as well as to perform sentiment analysis on both datasets
4. Classification: code written to invoke, fit, and evaluate a series of models to predict author gender based on text, sentiment of posts / comments, and use of emoji
5. Principal Component Analysis: visualizations created to compare true labels (gender of author) with labels predicted by models

It was assumed that two Subreddits would adequately reflect language and style of written communication used by women and men, respectively: AskWomen and AskMen.
Step 3 revealed that while women and men use different in words used in written communication, their style varies more when looked at through their chosen emoji. No meaningful differences were detected in verbosity of posts and comments or intensity of expressed sentiment.

The classifier (which will undergo further hyperparameter tuning before it is ready to be deployed in production) is a vote classifier composed of a Random Forest Classifier, Support Machine Vector, and an XGBoost Classifier. The model was selected based on its supreme performance (measured through accuracy) over any of the component models. (For this problem, improved accuracy is prioritized over model interpretability.)

### Data Dictionary

The data used in analysis and modeling consists of the following:

|**Feature**|**Type**|**Dataset**|**Description**|**Use**|
|:---|:---|:---|:---|
|title_selftext |string |aw_pos.csv |Content of submissions combining original columns `title` and `selftext` (after cleaning) |Primary variable in modeling |
|created_utc |datetime |aw_pos.csv |Time of submission |Exploratory analysis |
|distinguished |string |aw_pos.csv |Flag used to distinguish moderators from regular distributors |Data cleaning |
|len_chars |int |aw_pos.csv |Length of posts / comment, in # of characters |Exploratory analysis |
|len_words |int |aw_pos.csv |Length of posts / comment, in # of words |Exploratory analysis |
|avg_word_chars	|float |aw_pos.csv |Average length of words, in # of characters |Exploratory analysis |
|created_yr	|int |aw_pos.csv |Year of submission |Exploratory analysis |
|created_mth	|int |aw_pos.csv |Month of submission |Exploratory analysis |
|created_dy	|int |aw_pos.csv |Day of submission |Exploratory analysis |
|created_hr	|int |aw_pos.csv |Hour of submission |Exploratory analysis |
|emojis	|int |aw_pos.csv |Number of emoji used in a post / comment |Exploratory analysis and initial modeling |
|sia_neg |float |aw_pos.csv |Strength of negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|sia_neu |float |aw_pos.csv |Strength of neutral sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|sia_pos	|float |aw_pos.csv |Strength of positive sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_pn	|string |aw_pos.csv |Label indicating positive or negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_score	|float |aw_pos.csv |Score of positive or negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_pn_bin |int |aw_pos.csv |Binarized sentiment score (0: negative, 1: positive) |Exploratory analysis and initial modeling |
|body |string |aw_com.csv |Content of comments (after cleaning) |Primary variable in modeling |
|created_utc |datetime |aw_com.csv |Time of submission |Exploratory analysis |
|distinguished |string |aw_com.csv |Flag used to distinguish moderators from regular distributors |Data cleaning |
|len_chars |int |aw_com.csv |Length of posts / comment, in # of characters |Exploratory analysis |
|len_words |int |aw_com.csv |Length of posts / comment, in # of words |Exploratory analysis |
|avg_word_chars	|float |aw_com.csv |Average length of words, in # of characters |Exploratory analysis |
|created_yr	|int |aw_com.csv |Year of submission |Exploratory analysis |
|created_mth	|int |aw_com.csv |Month of submission |Exploratory analysis |
|created_dy	|int |aw_com.csv |Day of submission |Exploratory analysis |
|created_hr	|int |aw_com.csv |Hour of submission |Exploratory analysis |
|emojis	|int |aw_com.csv |Number of emoji used in a post / comment |Exploratory analysis and initial modeling |
|sia_neg |float |aw_com.csv |Strength of negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|sia_neu |float |aw_com.csv |Strength of neutral sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|sia_pos	|float |aw_com.csv |Strength of positive sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_pn	|string |aw_com.csv |Label indicating positive or negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_score	|float |aw_com.csv |Score of positive or negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_pn_bin |int |aw_com.csv |Binarized sentiment score (0: negative, 1: positive) |Exploratory analysis and initial modeling |
|title_selftext |string |am_pos.csv |Content of submissions combining original columns `title` and `selftext` (after cleaning) |Primary variable in modeling |
|created_utc |datetime |am_pos.csv |Time of submission |Exploratory analysis |
|distinguished |string |am_pos.csv |Flag used to distinguish moderators from regular distributors |Data cleaning |
|len_chars |int |am_pos.csv |Length of posts / comment, in # of characters |Exploratory analysis |
|len_words |int |am_pos.csv |Length of posts / comment, in # of words |Exploratory analysis |
|avg_word_chars	|float |am_pos.csv |Average length of words, in # of characters |Exploratory analysis |
|created_yr	|int |am_pos.csv |Year of submission |Exploratory analysis |
|created_mth	|int |am_pos.csv |Month of submission |Exploratory analysis |
|created_dy	|int |am_pos.csv |Day of submission |Exploratory analysis |
|created_hr	|int |am_pos.csv |Hour of submission |Exploratory analysis |
|emojis	|int |am_pos.csv |Number of emoji used in a post / comment |Exploratory analysis and initial modeling |
|sia_neg |float |am_pos.csv |Strength of negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|sia_neu |float |am_pos.csv |Strength of neutral sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|sia_pos	|float |am_pos.csv |Strength of positive sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_pn	|string |am_pos.csv |Label indicating positive or negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_score	|float |am_pos.csv |Score of positive or negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_pn_bin |int |am_pos.csv |Binarized sentiment score (0: negative, 1: positive) |Exploratory analysis and initial modeling |
|body |string |am_com.csv |Content of comments (after cleaning) |Primary variable in modeling |
|created_utc |datetime |am_com.csv |Time of submission |Exploratory analysis |
|distinguished |string |am_com.csv |Flag used to distinguish moderators from regular distributors |Data cleaning |
|len_chars |int |am_com.csv |Length of posts / comment, in # of characters |Exploratory analysis |
|len_words |int |am_com.csv |Length of posts / comment, in # of words |Exploratory analysis |
|avg_word_chars	|float |am_com.csv |Average length of words, in # of characters |Exploratory analysis |
|created_yr	|int |am_com.csv |Year of submission |Exploratory analysis |
|created_mth	|int |am_com.csv |Month of submission |Exploratory analysis |
|created_dy	|int |am_com.csv |Day of submission |Exploratory analysis |
|created_hr	|int |am_com.csv |Hour of submission |Exploratory analysis |
|emojis	|int |am_com.csv |Number of emoji used in a post / comment |Exploratory analysis and initial modeling |
|sia_neg |float |am_com.csv |Strength of negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|sia_neu |float |am_com.csv |Strength of neutral sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|sia_pos	|float |am_com.csv |Strength of positive sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_pn	|string |am_com.csv |Label indicating positive or negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_score	|float |am_com.csv |Score of positive or negative sentiment expressed in post / comment |Exploratory analysis and initial modeling |
|senti_pn_bin |int |am_com.csv |Binarized sentiment score (0: negative, 1: positive) |Exploratory analysis and initial modeling |

"aw_pos.csv" contains submissions (posts) from AskWomen subreddit. "aw_com.csv" contains comments from AskWomen subreddit.
"am_pos.csv" contains submissions (posts) from AskMen subreddit. "am_com.csv" contains comments from AskMen subreddit.

### Key Observations

1. Women and men generally write posts and comments similar lengths (see Part 3: Exploratory Analysis)
2. No significant differences were observed in the sentiment distribution and intensity - inclusion of scores in the classification model decreased model accuracy ((see Part 3: Exploratory Analysis and Part 4: Classification)
3. Men and women use emojis very differently: men use more of them and more frequently, women use them more sparingly (see Part 3: Exploratory Analysis)
4. Relatively simple models built on vectorized text achieve accuracy of ~70% on test data (Part 3)
5. The classifier chosen for further parameter tuning demonstrated ~88.2% accuracy (Part 3)

### Conclusions and Recommendations

The current "final" model offers promising results. However, before productionalizing it, the team will perform the actions outlined in Next Steps below.

---
### Next Steps

The corpora used for modeling were based on posts and comments created during just one week in December 2020. Extending the data set to include a representation of different seasons would likely refine the model's features and make the estimators more robust.
Although using emoji as features improved scores of classifiers over those using just text features (tokenized ngrams), the current "final" voting model does not account for emoji-driven features due partly to difficulties in deploying the pipeline using a custom feature extractor and partly to the computational intensity and duration of the GridSearch processes. Further calibration of hyperparameters would be attempted to account for this shortcoming.

---
