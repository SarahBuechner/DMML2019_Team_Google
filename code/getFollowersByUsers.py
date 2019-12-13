from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

df = pd.read_csv("Tweets.csv")

saved_column = df['name'].tolist()

users = list(dict.fromkeys(saved_column))

with open('users_followers_.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Followers", "Verified"])

    for user in users:
        url = 'https://www.twitter.com/' + user
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "lxml")

        f = soup.find('li', class_="ProfileNav-item--followers")
        try:
            title = f.find('a')['title']
            tab = []
            tab.append(user)
            tab.append(title)
            if soup.find('a', href = "/help/verified"):
                tab.append(True)
            else:
                tab.append(False)
            writer.writerow(tab)
        except:
            continue



