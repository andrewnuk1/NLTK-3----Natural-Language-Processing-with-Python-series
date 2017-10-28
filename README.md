# Twitter Sentiment Analysis

A fork from Sentdex, added in some missing code for one of the pickles
- Main change was to add code to save the featuresets pickle in pickler.py
- Also, using the Stanford Training and Test Data for the positive / negative tweets
- Other very minor changes



**pickler.py** is the first program to run, it trains the classifiers.
- "short_reviews/positive_cleaned_tweets.txt" are 90,000 positive tweets from the Stanford set
- "short_reviews/negative_cleaned_tweets.txt" are 90,000 negative tweets from the stanford set
- uses 20,000 shuffled tweets from the stanford data set as testing data



**sentiment_mod.py** is a module that is called in the next program



**test_sentiment.py** is the sentiment analysis program to run.
- "justeat2017070120170930nodates.txt" in this case was the tweets to/from @justeatuk in 2017 to end september
- 'outputresultjusteat2017070120170930try2.xls' is the excel workbook the results are saved to in cols of 50,000 rows
