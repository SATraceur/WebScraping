# Ideas for the stream listener class taken from
# http://adilmoujahid.com/posts/2014/07/twitter-analytics/

import json
import time
import numpy as np
import pandas as pd
import tweepy
import matplotlib.pyplot as plt
from tweepy.streaming import StreamListener
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

consumer_key = 'gtzmmN0c9cx55jBcnoINwr430'
consumer_secret = 'Owk4y8u4CRuUmfSbOphu9oEvPDfKDEwTsaJBHV86mIxPv0pTo1'
access_token = '4864444555-kgN1CaSS24xWFkYGPPEc8XZkpYrg9G6FwrMrwcZ'
access_token_secret = 'ogcTIkhkLuIaOrR3Z2sLuOypCxwKSkq7xwrSjR4y1ZbAw'
plotly.tools.set_credentials_file(username='SATraceur', api_key='416oD3sXzlvfc2oI5AZ4')

class StdOutListener(StreamListener):
    def __init__(self):
        self.last_tweet_printed = time.time()

    def on_data(self, data):
        print(data)
     #   data = json.loads(data)
    #    print('Screen Name: {} - Location: {} - Text: {}\n'.format(data['user']['screen_name'], data['user']['location'], data['text']))
        return True

    def on_error(self, status):
        print(status)


l = StdOutListener()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
stream = tweepy.Stream(auth, l)
var = input("Do you want to run the stream (press 1) or read/display (data press 2)? ")

if var == "1":
    stream.filter(track=['watch dogs' or 'Watch Dogs', 'GTA' or 'gta', 'Ghost Recon' or 'ghost recon',
                        'COD' or 'call of duty' or 'Call of Duty', 'battlefield' or 'Battlefield' or 'BATTLEFIELD',
                        'madden' or 'Madden', 'PUBG' or 'Player Unknown\'s Battlegrounds'], languages=["en"])

elif var == "2":
    # read data into array from file
    tweets_data_path = '/home/satraceur/PycharmProjects/Beer2/twitter_data.txt'
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    locations = []

    for tweet in tweets_data:  # for each tweet in the file
        location = tweet['user']['location']  # save the location
        if location == None:  # If location is null, store as none
            location = "None"
        s = tweet['text']
        found = False
        game = ""

        ## save what game was mentioned ##
        if not s.find("Watch Dogs") == -1 or not s.find("watch dogs") == -1:
            game = "Watch Dogs"

        elif not s.find("GTA") == -1 or not s.find("gta") == -1:
            game = "GTA"

        elif not s.find("Ghost Recon") == -1 or not s.find("ghost recon") == -1:
            game = "Ghost Recon"

        elif not s.find("COD") == -1 or not s.find("call of duty") == -1 or not s.find("Call of Duty") == -1:
            game = "Call of Duty"

        elif not s.find("battlefield") == -1 or not s.find("Battlefield") == -1 or not s.find("BATTLEFIELD") == -1:
            game = "Battlefield"

        elif not s.find("madden") == -1 or not s.find("Madden") == -1:
            game = "Madden"

        elif not s.find("PUBG") == -1 or not s.find("Player Unknown\'s Battlegrounds") == -1:
            game = "PUBG"

        for item in locations:  # for each item in the locations list [ LOCATION, GAMES-LIST ]
            if item[0] == location:  # if location exists in list
                found = True
                for gameitem in item[1]:  # search through associated games list
                    if gameitem[0] == game:  # locate mentioned game
                        gameitem[1] = gameitem[1] + 1  # increment number of times it was mentioned

        if not found and game != "":
            temp = [["Watch Dogs", 0], ["GTA", 0], ["Ghost Recon", 0], ["Call of Duty", 0], ["Battlefield", 0],
                    ["Madden", 0], ["PUBG", 0]]
            for item in temp:
                if item[0] == game:
                    item[1] = item[1] + 1
            locations.append([location, temp])

    # Make a nice table to display the results
    tweets = pd.DataFrame(locations, columns=["Location", "Games"])
    print(tweets)

    # Plot graphs for each location
    NUM = 0
    # locations.sort(key = lambda KEY : KEY[0])
    for loc in locations:
        NUM += 1
        X = []
        Y = []

        for item in loc[1]:
            X.append(item[0])  # Save game titles to list
            Y.append(item[1])  # Save occurances to list

        y_pos = np.arange(len(X))
        plt.figure(num=NUM, figsize=(12, 6), dpi=70, facecolor='w', edgecolor='k')
        plt.bar(y_pos, Y, align='center', alpha=0.5)
        plt.xticks(y_pos, X, rotation=0)
        plt.title(loc[0], fontweight="bold", fontsize=25)
        plt.xlabel("Games", fontsize=15)
        plt.ylabel("# Mentions", fontsize=15)
        plt.show()


        # data = [go.Bar(x=X, y=Y)]
        # py.iplot(data, filename='basic-bar')

else:
    print("you screwed up")









