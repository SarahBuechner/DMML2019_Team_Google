# Sentiment Analysis gathered in Twitter

## Abstract
<dt align="justify">

In our study we want to show how **companies can handle complaints more efficienty** in order to avoid a bad reputation. We will provide different suggestions on how companies, and here more specifically airline companies, should address the task of treating tweets linked to their organization.

Nowadays, companies need to deal and solve issues with customers on social media. Needless to say, a non-solved negative tweet may turn viral in a couple of hours compromising the whole firm's reputation. From a **business perspective**, the company needs to **prioritize which customer needs to be replied to first**. 

We initially thought about establishing a priority based on ticket prices, however this information cannot be inferred.

Therefore, we will prioritize tweets based on the following criteria:
- **Negative sentiment** 
We consider that Tweets classified as negative should be treated before positive or neutral ones. Once we filtered out positive and neutral tweets, we will prioritize the remaining according to their level of negativity. 
- **Number of followers**
We take into account that twitter accounts with many followers are able to reach out to a larger audience and hence their tweets might have a larger impact on company's future profits than accounts with less followers. 
- **Verified accounts**
Only influential people have verified twitter accounts. Hence, any message shared by a verified account is more likely to have an larger outreach on social media than others. 
-**Business class**
Corporations tend to consider customers who bought business class tickets as a priority. Therefore, all tweets containing for instance,"business class", "first class", "priority" are classified as business class customers.  

The total number of followers and if accounts are verified or not will be acquiered through web-scraping. We created an algorithm that will get the data and merge them to our original dataset. Also, it is possible to use web-scrapping to increase the information of each passenger, such as gender, age, civil status, etc. 

Another interesting implementation from a business perspective may be data deanonymization. For instance, knowing the users account, the timestamps and the location airline companies can identify the passenger behind the account. 

We have also added a language detection and translation method. It can be useful for companies to gather tweets from any passenger in the word and reply to it in the corresponding language. 

Finally, it would have been interesting to demonstrate empirically whether a negative sentiment analysis on Twitter for a given airline affects negatively the stock price and vice versa. However, since the dataset contains tweets from a limited time period (7 days) this implementation did not seems relevant. 


</dt>


## Getting Started

First of all, you need to download all the files from the [Database](https://github.com/SarahBuechner/DMML2019_Team_Google/tree/master/Database/Database) folder `AAL.csv`, `DAL.csv`, `LUV.csv`, `UAL.csv` and `Tweets.csv`. If you prefer, you can use the URL provided in the section **Databases links**. 

```python
tweets = pd.read_csv("https://raw.githubusercontent.com/SarahBuechner/DMML2019_Team_Google/master/Database/Tweets.csv")
```
 
### Prerequisites

Before start, you must **install the software the** `Plotnine` **package** which is an implementation of a grammar of graphics in Python based on ggplot2. The grammar allows users to compose plots by explicitly mapping data to the visual objects that make up the plot. The `spacy` and the english language `-m spacy download en` packages used in the tweet *tokenization* process. Then `-U textblob` and `-m textblob.download_corpora` packages which enable to compute the *polarity* and *subjectivity* level of the tweet content. To install all packages is the following command:

```python
!pip install 'plotnine[all]'
!pip install spacy
!python -m spacy download en
!pip install -U textblob
!python -m textblob.download_corpora
!pip install vaderSentiment
!pip install yellowbrick
```

Also, it is required to import the following packages: `pandas`, `numpy`, `matplotlib.pyplot`, `seaborn`, `re`, `English`, `TextBlob` and `wordcloud`, among others. You can copy and paste the code provided below.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import itertools
import nltk
import requests

from bs4 import BeautifulSoup
from wordcloud import WordCloud,STOPWORDS
from plotnine import *
from spacy.lang.en import English
from textblob import TextBlob
from yellowbrick.classifier import PrecisionRecallCurve
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import ngrams
from nltk.stem import WordNetLemmatizer
from yellowbrick.draw import manual_legend
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
```
Once you completed that, you can run on your local machine the notebook `DM_ML.ipynb` for development and testing purposes.


## Database

**Twitter data was scraped from February of 2015** and contributors were asked to classify the tweets as either positive, negative, or neutral. Then categorize the negative ratings on topics (such as "late flight" or "rude service"). 

We will use this two datasets:

### Kaggle Database

#### Original features:
* __tweet_id__: The primary key
* __airline_sentiment__: Positive, neutral or negative.
* __airline_sentiment_confidence__: We think it is the % of surveyed who classified tweet as shwon in the Airline_sentiment column.
* __negativereason__: Negative topic (i.e.: delay, bad flight, customer service…)
* __airline__: The Airline’s name (American Airlines, United Airlines, US Airways Southwest, Delta and Virgin America)
* __name__: The user’s account name (Some users tweeted more than once)
* __retweet_count__: Number of the retweets
* __text__: The tweet
* __tweet_coord__: Coordinations of the tweet
* __tweet_created__: When the tweet was created (timestamp)
* __tweet_location__: Location of the tweet (i.e.: Los Angeles, San Francisco…)

#### Created features:
* __Verified__: Positive or negative (boolean)
* __Followers__: Number of followers.
* __tokenized_tweet__: Tokens of each tweet.
* __tokens_string__: Joint tokens as a string for each tweet.
* __polarity_Vader__: Vader text classification. Float value within the range [-1.0 to 1.0] where +1 is a very positive sentiment and -1 a very negative.
* __polarity_Textblob__: TextBlob text classification. Float value within the range [-1.0 to 1.0] where +1 is a very positive sentiment and -1 a very negative.
* __polarity_Vader_string__: Vader text classification transformed into string. 
* __polarity_Textblob_string__: TextBlob text classification transformed into string. 
* __language_tweets__: The language of the tweet.
* __translation_tweets__: The translation of the tweets into another language. 

### Yahoo Database

* __Date__: From 01/02/2015 to 31/12/2015
* __Open__: Open price.
* __High__: Highest price during open hours.
* __Low__: Lowest price during open hours.
* __Close__: Close price.
* __Adj Close__: Adjusted close price.
* __Volume__: Daily volume.


### Databases links

* [Kaggle](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
* [American Airlines Group Inc. (AAL)](https://finance.yahoo.com/quote/AAL/historyperiod1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)
* [United Airlines Holdings, Inc. (UAL)](https://finance.yahoo.com/quote/UAL/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)
* [Southwest Airlines Co. (LUV)](https://finance.yahoo.com/quote/LUV/history?period1=1422745200&period2=1451516400&interval=1d&filter=history&frequency=1d)

### Project Video
* [Youtube](https://www.youtube.com/watch?v=21sN_u5lcng)

## Authors
* **Pau Gallardo** - **Sara Büchner** - **Bhavya Sabesa** - **Ibrahim Ounon**  -  [Github Repository Team Google](https://github.com/SarahBuechner/DMML2019_Team_Google.git)
