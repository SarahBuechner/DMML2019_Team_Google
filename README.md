# Sentiment Analysis gathered in Twitter

## Abstract
<dt align="justify">

In our study we want to analyse how the **customer-company relationship impacts on the revenue** of each company as well as on the stock market. We will try to demonstrate empirically whether a **negative sentiment analysis on Twitter** for a given airline affects negatively the stock price and vice versa.

Nowadays, companies need to deal and solve issues with customers on social media. Needless to say, a non-solved negative tweet may turn viral in a couple of hours compromising the whole firm's reputation. From a **business perspective**, the company needs to **prioritize which customer needs to be replied firstly**. At first glance, one may think this priority have to be based on ticket price however this information cannot be inferred *(We will try to deanonymized it using the account_name)*.

The **first solution** purposed, regarding the limitations presented in the dataset, is to **classify tweets into** two classes: **business class** *(referred as BC)* and **non-business class** *(referred as NBC)* using the tweet text content. For instance, we consider that all tweets containing "business class", "first class", "priority" are customers who bought a business class ticket. 

The **second solution** to deal with that, is to figure out what is **the scope of the tweet**. For instance, if the **account is verified**, or the complaint is made by a **popular account** *(with a lot of followers)* the complaint needs to be address  with a priority. *(NOT IMPLEMENTED, since we are struggling with web-data-scraping)*

Once all the negative tweets are filtered from the dataset and pick those belonging to BC group, we proceed to implement an algorithm which sorts using the **tweet's polarity** *(range value from -1.0 to 1.0, where 0 indicates neutral, +1 indicates a very positive sentiment and -1 represents a very negative sentiment).* Using this approach, we can offer an objective solution to manage complaints on social media.

</dt>



### Some exploratory ideas on this:

1. When tweets are negative, what topics do travellers tend to discuss?
2. When tweets are positive, what are travellers happy with?
3. Outside of sentiment, what other systematic variation exists in the tweets about different airlines?
4. What types of tweets on airlines tend to be retweeted?

## Getting Started

First of all, you need to download all the files from the [Database](https://github.com/SarahBuechner/DMML2019_Team_Google/tree/master/Database/Database) folder `AAL.csv`, `DAL.csv`, `LUV.csv`, `UAL.csv` and `Tweets.csv`. If you prefer, you can use the URL provided in the section **Databases links**. 

```python
tweets = pd.read_csv("https://raw.githubusercontent.com/SarahBuechner/DMML2019_Team_Google/master/Database/Tweets.csv")
```
 
### Prerequisites

Before start, you must to **install the software the** `Plotnine` **package** which is an implementation of a grammar of graphics in Python based on ggplot2. The grammar allows users to compose plots by explicitly mapping data to the visual objects that make up the plot. The `spacy` and the english language `-m spacy download en` packages used in the tweet *tokenization* process. Then `-U textblob` and `-m textblob.download_corpora` packages which enable to compute the *polarity* and *subjectivity* level of the tweet content. To install all packages is the following command:

```python
!pip install 'plotnine[all]'
!pip install spacy
!python -m spacy download en
!pip install -U textblob
!python -m textblob.download_corpora
```

Also, it is required to import the following packages: `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, `re`, `English`, `TextBlob` and `wordcloud`. You can copy and paste the code provided below.

```python
import pandas as pd
import numpy as np
from plotnine import *
import matplotlib.pyplot as plt
import seaborn as sns
import re
from spacy.lang.en import English
from textblob import TextBlob
from wordcloud import WordCloud,STOPWORDS
```
Once you complete that, you can running on your local machine the notebook `DM_Project.ipynb` for development and testing purposes.


## Database

**Twitter data was scraped from February of 2015** and contributors were asked to classify either positive, negative, or neutral the tweets. Then categorise the negative ratings on topics (such as "late flight" or "rude service"). Nevertheless, we also consider to develop our sentiment classifier since we think will represent a more reliable approach.

We will use this two datasets:

### Kaggle Database

#### Original features:
* __Tweet_id__: The primary key
* __Airline_sentiment__: Positive, neutral or negative.
* __Airline_sentiment_confidence__: We think it is the % of surveyed who classified tweet as shwon in the Airline_sentiment column.
* __Negativereason__: Negative topic (i.e.: delay, bad flight, customer service…)
* __Airline__: The Airline’s name (American Airlines, United Airlines, US Airways Southwest, Delta and Virgin America)
* __Name__: The user’s account name (Some users tweeted more than once)
* __Retweet_count__: Number of the retweets
* __Text__: The tweet
* __Tweet_coord__: Coordinations of the tweet
* __Tweet_created__: When the tweet was created (timestamp)
* __Tweet_location__: Location of the tweet (i.e.: Los Angeles, San Francisco…)

#### Created features:
* __Tweet_polarity__: Float value within the range [-1.0 to 1.0] where +1 is a very positive sentiment and -1 a very negative sentiment.
* __Tweet_subjectivity__: Float value within the range [0.0 to 1.0] where 0.0 is very objective and 1.0 is very subjective.
* __Group_class__: Business class or non-business class.
* __Account_verified__: Positive or negative (boolean)
* __Account_popularity__: Number of followers

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

#### 1.2) Negative Reason by Airline¶
In the previous chart we saw that the most common class was the Negative mood. This graph, shows what are the most common negative topics among airlines.

```python
# TO DO: Create a Table
"""The 3 main negative topics of American are: (1) Customer Service Issue, (2) Late Flight and (3) Cancelled Flight
The 3 main negative topics of Delta are: (1) Late Flight, (2) Customer Service Issue and (3) Can't Tell
The 3 main negative topics of Southwest are: (1) Customer Service Issue, (2) Cancelled Flight and (3) Can't Tell
The 3 main negative topics of US Airways are: (1) Customer Service Issue, (2) Late Flight and (3) Can't Tell
The 3 main negative topics of United are: (1) Customer Service Issue, (2) Late Flight and (3) Can't Tell
The 3 main negative topics of Virgin America are: (1) Customer Service Issue, (2) Flight Booking Problems and (3) Can't Tell"""
```
#### 1.3) Tweet volum per day
This graph captures the volume tweet distribution grouped by week days. On Sunday it is when more tweets are released.

#### 1.4) Tweet volum per hour
This graph captures the volume tweet distribution per hour.

![Distribution tweet volume](https://github.com/SarahBuechner/DMML2019_Team_Google/blob/master/Images/1.3_Tweet_Volum_DayHour.png)\

### 2) Data Mining and Machine Learning
(***TO DO***)


### Databases links

* [Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
* [American Airlines Group Inc. (AAL)](https://finance.yahoo.com/quote/AAL/historyperiod1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)
* [United Airlines Holdings, Inc. (UAL)](https://finance.yahoo.com/quote/UAL/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)
* [Southwest Airlines Co. (LUV)](https://finance.yahoo.com/quote/LUV/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)

## Authors
* **Pau Gallardo** - **Sara Büchner** - **Bhavya Sabesa** - **Ibrahim Ounon**  -  [Github Repository Team Google](https://github.com/SarahBuechner/DMML2019_Team_Google.git)
