# -*- coding: utf-8 -*-
# Individual Assignment 2
# Predict 452
# Toni Moore

# Original code, tweet_dumper.py, came from GitHub
# https://gist.github.com/yanofsky/5436496
# I modified the code to collect tweets from the four front runners
# in the 2016 U.S. Presidential election.

# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import sys
#Twitter API credentials
consumer_key="blah"
consumer_secret="blah"
access_key="blah"
access_secret="blah"
def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=1)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id -1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        
        #all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id -1
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [] #initialize master list to hold our ready tweets
    for tweet in alltweets:
        outtweets.append([tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])
    
    #write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    pass
    
# Collecting tweets from Clinton's official twitter handle
print "Collecting tweets from Clinton's official twitter handle"
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("HillaryClinton")

# Collecting tweets from Sanders' official twitter handle
print "Collecting tweets from Sanders' official twitter handle"
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("BernieSanders")
    
# Collecting tweets from Trump's official twitter handle
print "Collecting tweets from Trump's official twitter handle"
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("realDonaldTrump")
    
# Collecting tweets from Cruz's official twitter handle
print "Collecting tweets from Cruz's official twitter handle"
if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("tedcruz")    

print "Program complete. Check working directory for output files."
