# It is possible to forecast the stock price based on the Sentiment Analysis gathered in Twitter? (Team GoogleProject)

## Abstract

In our study we want to analyse how the \textbf{customer-company relationship impacts on the revenue} of each company as well as on the stock market. We will try to demonstrate empirically whether a \textbf{negative sentiment analysis on Twitter} for a given airline impacts negatively the stock price and vice versa.

### Some exploratory ideas on this:
* When tweets are negative, what topics do travelers tend to discuss?* When tweets are positive, what are travelers happy with?* Outside of sentiment, what other systematic variation exists in the tweets about different airlines?* What types of tweets on airlines tend to be retweeted?


## Database

\textbf{Twitter data was scraped from February of 2015} and contributors were asked to classify either positive, negative, or neutral the tweets. Then categorise the negative ratings on topics (such as "late flight" or "rude service"). Nevertheless, we also consider to develop our sentiment classifier since we think will represent a more reliable approach.

We will use this two datasets:

### Kaggle Database
* \underline{Tweet_id}: The primary key* \underline{Airline_sentiment}: Positive or negative (boolean)* \underline{Airline_sentiment_confidence}: Logistic regression (Since values form 0 to 1)* \underline{Negativereason}: Negative topic (i.e.: delay, bad flight, customer service…)* \underline{Airline}: The Airline’s name (American Airlines, United Airlines, US Airways Southwest, Delta and Virgin America)* \underline{Name}: The user’s account name (Some users tweeted more than once)* \underline{Retweet_count}: Number of the retweets* \underline{Text}: The tweet* \underline{Tweet_coord}: Coordinations of the tweet* \underline{Tweet_created}: When the tweet was created (timestamp)* \underline{Tweet_location}: Location of the tweet (i.e.: Los Angeles, San Francisco…)

### Yahoo Database
* \underline{Date}: From 01/02/2015 to 31/12/2015* \underline{Open}: Open price.* \underline{High}: Highest price during open hours.* \underline{Low}: Lowest price during open hours.* \underline{Close}: Close price.* \underline{Adj Close}: Adjusted close price.* \underline{Volume}: Daily volume.

### Databases links

* [Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
* [American Airlines Group Inc. (AAL)](https://finance.yahoo.com/quote/AAL/historyperiod1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)
* [United Airlines Holdings, Inc. (UAL)](https://finance.yahoo.com/quote/UAL/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)* [Southwest Airlines Co. (LUV)](https://finance.yahoo.com/quote/LUV/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)

## Authors
* **Pau Gallardo** - **Sara Büchner** - **Bhavya Sabesa** - **Ibrahim Ounon** [Team Google](https://github.com/SarahBuechner/DMML2019_Team_Google.git)
