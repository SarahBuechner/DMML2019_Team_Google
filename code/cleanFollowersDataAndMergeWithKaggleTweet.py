
import pandas as pd

tweets = pd.read_csv("Tweets.csv")
df = pd.read_csv("users_followers_.csv")
df['Followers'] = df['Followers'].str.replace(" Followers", "")
df['Followers'] = df['Followers'].str.replace(" Follower", "")
df['Followers'] = df['Followers'].str.replace(".", "")
df['Followers'] = pd.to_numeric(df['Followers'])

df_tweets = pd.merge(tweets,df,on='name')



df_tweets.to_csv("TweetsWithUserFollowers.csv", sep=',')

