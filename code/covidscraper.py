### TESTING

import GetOldTweets3 as got
import pandas as pd
import numpy as np
import tweepy 


consumer_key = "mPpDKrZygcWhx6P1E5lAYNNFv"
consumer_secret = "kFkBtX40d8S73Dq9pPbwQU4xFBlpRGCZGxtM15QIWrHEYnP48g"
access_token = "1282555647712571394-ax5KEF4bFOeWcPftwyBIAqrq78MdgV"
access_token_secret = "FyX8skIwpST5fsKkt8m7DfoMBpAp9tICNoi7i8E3FdDa4"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth, wait_on_rate_limit=True) 


max_tweets = 2
# this gets us all the tweets for a specific hashtag. Here, it is #equality for testing purposes
tweetCriteria = got.manager.TweetCriteria().setQuerySearch('equality')\
                                           .setSince("2019-01-01")\
                                           .setUntil("2019-07-15")\
                                           .setMaxTweets(max_tweets)
                                        #.setNear('India')

df = pd.DataFrame(columns=['Date', 'Username','Followers Count','Tweet'])

listoftweets = []

for i in range(max_tweets):
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
    
    username = tweet.username
    #print(username)

    ### now i use tweepy to get the no. of followers for a username.
    ### we need the followers count so that we can use it to exclude famous people as the tend to have a high follower count
    c = tweepy.Cursor(api.followers, username)
    count = 0
    
    for follower in c.items(): 
        count += 1
        
    followers_num = count
    print(count)

    
    tweetx = [tweet.date ,tweet.username,followers_num,tweet.text]
    listoftweets.append(tweetx)
    
#print(listoftweets) 
dfx = pd.DataFrame(listoftweets,columns=['Date','Username','Followers Count','Tweet'])
print(dfx)
