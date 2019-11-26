# Is it possible to forecast the stock price based on the Sentiment Analysis gathered in Twitter? (Team GoogleProject)

## Abstract

In our study we want to analyse how the **customer-company relationship impacts on the revenue** of each company as well as on the stock market. We will try to demonstrate empirically whether a **negative sentiment analysis on Twitter** for a given airline impacts negatively the stock price and vice versa.

### Some exploratory ideas on this:
1. When tweets are negative, what topics do travelers tend to discuss?2. When tweets are positive, what are travelers happy with?3. Outside of sentiment, what other systematic variation exists in the tweets about different airlines?4. What types of tweets on airlines tend to be retweeted?


## Database

**Twitter data was scraped from February of 2015** and contributors were asked to classify either positive, negative, or neutral the tweets. Then categorise the negative ratings on topics (such as "late flight" or "rude service"). Nevertheless, we also consider to develop our sentiment classifier since we think will represent a more reliable approach.

We will use this two datasets:

### Kaggle Database
*_Tweet_id_: The primary key* _Airline_sentiment_: Positive or negative (boolean)* _Airline_sentiment_confidence}: Logistic regression (Since values form 0 to 1)* _Negativereason_: Negative topic (i.e.: delay, bad flight, customer service…)* _Airline_: The Airline’s name (American Airlines, United Airlines, US Airways Southwest, Delta and Virgin America)* _Name_: The user’s account name (Some users tweeted more than once)* _Retweet_count_: Number of the retweets* _Text_: The tweet* _Tweet_coord_: Coordinations of the tweet* _Tweet_created_: When the tweet was created (timestamp)* _Tweet_location_: Location of the tweet (i.e.: Los Angeles, San Francisco…)

### Yahoo Database
* _Date_: From 01/02/2015 to 31/12/2015* _Open_: Open price.* _High_: Highest price during open hours.* _Low_: Lowest price during open hours.* _Close_: Close price.* _Adj Close_: Adjusted close price.* _Volume_: Daily volume.

### Databases links

* [Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
* [American Airlines Group Inc. (AAL)](https://finance.yahoo.com/quote/AAL/historyperiod1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)
* [United Airlines Holdings, Inc. (UAL)](https://finance.yahoo.com/quote/UAL/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)* [Southwest Airlines Co. (LUV)](https://finance.yahoo.com/quote/LUV/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)

## Authors
* **Pau Gallardo** - **Sara Büchner** - **Bhavya Sabesa** - **Ibrahim Ounon**   [Github Repository Team Google](https://github.com/SarahBuechner/DMML2019_Team_Google.git)
