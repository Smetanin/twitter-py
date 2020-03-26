
from twitterscraper.query import query_user_info
from twitterscraper.query import query_tweets_from_user
from twitterscraper.query import query_tweets_once
from twitterscraper.query import query_tweets
import pandas as pd
from multiprocessing import Pool
import time
from IPython.display import display
import json
import collections
import datetime as dt
from datetime import datetime
import openpyxl


def main():

    with open("data2.json", "w") as f:
        f.write("Current time {} START!!!\n".format(datetime.now().ctime()))
    user = '@realDonaldTrump'
    json_object_array = []
    data = {}
    tweet_count_old = 0
    for tweet in query_tweets(user,limit=None,begindate=dt.date(2019,12,10),enddate=dt.date(2019,12,11),poolsize=20,lang='english'):
        data['screen_name'] = tweet.screen_name.encode('utf-8')
        data['timestamp'] = tweet.timestamp.ctime()
        data['text'] = tweet.text.encode('utf-8')
        json_dump = json.dumps(data)
        json_object_array.append(json.loads(json_dump))
        with open("data2.json", "a") as f:
            f.write("Got {} tweets from username {}\n".format(
                len(json_object_array) - tweet_count_old, user))
        tweet_count_old = len(json_object_array)
    with open('data2.json', 'a') as f:
        json.dump(json_object_array, f,  indent=2)


print("Done!")

if __name__ == '__main__':
    main()
