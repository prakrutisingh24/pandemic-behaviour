import GetOldTweets3 as got
import pandas as pd
import numpy as np
import tweepy



consumer_key = "mPpDKrZygcWhx6P1E5lAYNNFv"
consumer_secret = "kFkBtX40d8S73Dq9pPbwQU4xFBlpRGCZGxtM15QIWrHEYnP48g"
access_token = "1282555647712571394-ax5KEF4bFOeWcPftwyBIAqrq78MdgV"
access_token_secret = "FyX8skIwpST5fsKkt8m7DfoMBpAp9tICNoi7i8E3FdDa4"


# authorization of consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# set access to user's access key and access secret  
auth.set_access_token(access_token, access_token_secret) 
  
# calling the api  
api = tweepy.API(auth, wait_on_rate_limit=True) 


max_tweets = 3
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
    print(username)
    c = tweepy.Cursor(api.followers, username)
    count = 0
    for follower in c.items(): 
        count += 1
        print(count)
    print(count)    
    followers_num = count

    
    tweetx = [tweet.date ,tweet.username,followers_num,tweet.text]
    listoftweets.append(tweetx)
    
#print(listoftweets) 
dfx = pd.DataFrame(listoftweets,columns=['Date','Username','Followers Count','Tweet'])
print(dfx)


'''
import os
import tweepy as tw
import pandas as pd

consumer_key = "mPpDKrZygcWhx6P1E5lAYNNFv"
consumer_secret = "kFkBtX40d8S73Dq9pPbwQU4xFBlpRGCZGxtM15QIWrHEYnP48g"
access_token = "1282555647712571394-ax5KEF4bFOeWcPftwyBIAqrq78MdgV"
access_token_secret = "FyX8skIwpST5fsKkt8m7DfoMBpAp9tICNoi7i8E3FdDa4"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#lockdown"
date_since = "2018-11-16"

new_search = search_words + " -filter:retweets"
#new_search

tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items(100)

users_locs = [[tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.created_at, tweet.text] for tweet in tweets]


tweet_text = pd.DataFrame(data=users_locs, columns=['user_id', "location", "followers", "posted at", "text"])
tweet_text
'''