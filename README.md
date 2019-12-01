# Sentiment Analysis gathered in Twitter? (Team GoogleProject)

## Abstract

In our study we want to analyse how the **customer-company relationship impacts on the revenue** of each company as well as on the stock market. We will try to demonstrate empirically whether a **negative sentiment analysis on Twitter** for a given airline affects negatively the stock price and vice versa.

Nowadays, companies need to deal and solve issues with customers on social media. Needless to say, a non-solved negative tweet may turn viral in a couple of hours compromising the whole firm's reputation. From a **business perspective**, the company needs to **prioritize which customer needs to be replied firstly**. At first glance, one may think this priority have to be based on ticket price however this information cannot be inferred *(We will try to deanonymized it using the account_name)*.

The **first solution** purposed regarding the limitation presented in the dataset, is to **classify tweets into** two classes: **business class** *(referred as BC)* and **non-business class** *(referred as NBC)* using the tweet text content. For instance, we consider that all tweets containing "business class", "first class", "priority" are customers who bought a business class ticket. 

Once we filtered all the negative tweets from the dataset and pick those that belongint to BC group, we implement an algorithm to compute the polarity of each passanger reponse


### Some exploratory ideas on this:

1. When tweets are negative, what topics do travellers tend to discuss?
2. When tweets are positive, what are travellers happy with?
3. Outside of sentiment, what other systematic variation exists in the tweets about different airlines?
4. What types of tweets on airlines tend to be retweeted?

## Getting Started

First of all, you need to download all the files from the [Database](https://github.com/SarahBuechner/DMML2019_Team_Google/tree/master/Database/Database) folder `AAL.csv`, `DAL.csv`, `LUV.csv`, `UAL.csv` and `Tweets.csv`. If you prefer, you can use the URL provided in the section **Databases links**. 
 
### Prerequisites

Before start, you must to **install the software the** `Plotnine` **package** which is an implementation of a grammar of graphics in Python based on ggplot2. The grammar allows users to compose plots by explicitly mapping data to the visual objects that make up the plot. You can implement the following command:

```python
!pip install 'plotnine[all]'
```

Also, it is required to import the following packages: `pandas`, `numpy`, `matplotlib.pyplot` and `seaborn`. You can copy and paste the code provided below.
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```
Once you complete that, you can running on your local machine the notebook `DM_Project.ipynb` for development and testing purposes.


## Database

**Twitter data was scraped from February of 2015** and contributors were asked to classify either positive, negative, or neutral the tweets. Then categorise the negative ratings on topics (such as "late flight" or "rude service"). Nevertheless, we also consider to develop our sentiment classifier since we think will represent a more reliable approach.

We will use this two datasets:

### Kaggle Database

* __Tweet_id__: The primary key
* __Airline_sentiment__: Positive or negative (boolean)
* __Airline_sentiment_confidence__: Logistic regression (Since values form 0 to 1)
* __Negativereason__: Negative topic (i.e.: delay, bad flight, customer service…)
* __Airline__: The Airline’s name (American Airlines, United Airlines, US Airways Southwest, Delta and Virgin America)
* __Name__: The user’s account name (Some users tweeted more than once)
* __Retweet_count__: Number of the retweets
* __Text__: The tweet
* __Tweet_coord__: Coordinations of the tweet
* __Tweet_created__: When the tweet was created (timestamp)
* __Tweet_location__: Location of the tweet (i.e.: Los Angeles, San Francisco…)

### Yahoo Database

* __Date__: From 01/02/2015 to 31/12/2015
* __Open__: Open price.
* __High__: Highest price during open hours.
* __Low__: Lowest price during open hours.
* __Close__: Close price.
* __Adj Close__: Adjusted close price.
* __Volume__: Daily volume.


## Notebook 
Find below the structure of the [Notebook](https://github.com/SarahBuechner/DMML2019_Team_Google/blob/master/DM_Project.ipynb)

### 1) Exploratory Data Anlysis

#### 1.1) Sentiment Analysis by Airline:
![Distribution Sentiment by Airline](https://github.com/SarahBuechner/DMML2019_Team_Google/blob/master/Images/1.1_Sentiment_Analysis.png)\
This graph allows us to see that the most common class is negative mood = 62.69%.

#### 1.2) Negative ratings classified on topics
![Negative Ratings classification](https://github.com/SarahBuechner/DMML2019_Team_Google/blob/master/Images/1.2_Negative_Ratings_Topics.png)\
In the previous chart we saw that the most common class was the Negative mood. This graph, shows what are the most common negative topics among airlines.

### 2) Data Mining and Machine Learning
(***TO DO***)


### Databases links

* [Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
* [American Airlines Group Inc. (AAL)](https://finance.yahoo.com/quote/AAL/historyperiod1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)
* [United Airlines Holdings, Inc. (UAL)](https://finance.yahoo.com/quote/UAL/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)
* [Southwest Airlines Co. (LUV)](https://finance.yahoo.com/quote/LUV/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)

## Authors
* **Pau Gallardo** - **Sara Büchner** - **Bhavya Sabesa** - **Ibrahim Ounon**  -  [Github Repository Team Google](https://github.com/SarahBuechner/DMML2019_Team_Google.git)
