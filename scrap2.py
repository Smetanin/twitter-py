from twitterscraper.query import query_user_info
from twitterscraper.query import query_tweets_from_user
import pandas as pd
from multiprocessing import Pool
import time
from IPython.display import display
import json
import collections

global twitter_user_info
twitter_user_info = []


def get_user_info(twitter_user):
    """
    An example of using the query_user_info method
    :param twitter_user: the twitter user to capture user data
    :return: twitter_user_data: returns a dictionary of twitter user data
    """
    user_info = query_user_info(user=twitter_user)
    twitter_user_data = {}
    twitter_user_data["user"] = user_info.user
    twitter_user_data["fullname"] = user_info.full_name
    twitter_user_data["location"] = user_info.location
    twitter_user_data["blog"] = user_info.blog
    twitter_user_data["date_joined"] = user_info.date_joined
    twitter_user_data["id"] = user_info.id
    twitter_user_data["num_tweets"] = user_info.tweets
    twitter_user_data["following"] = user_info.following
    twitter_user_data["followers"] = user_info.followers
    twitter_user_data["likes"] = user_info.likes
    twitter_user_data["lists"] = user_info.lists

    return twitter_user_data


def main():
    '''
    start = time.time()
    users = ['realDonaldTrump']

    pool = Pool(8)    
    for user in pool.map(get_user_info,users):
        twitter_user_info.append(user)

    cols=['id','fullname','date_joined','location','blog', 'num_tweets','following','followers','likes','lists']
    data_frame = pd.DataFrame(twitter_user_info, index=users, columns=cols)
    data_frame.index.name = "Users"
    data_frame.sort_values(by="followers", ascending=False, inplace=True, kind='quicksort', na_position='last')
    elapsed = time.time() - start
    print("Elapsed time: ")
    print(elapsed)
    display(data_frame)

    for tweet in query_tweets_from_user("realDonaldTrump", limit=1):
        data['aa'] = "aa"
        data['screen_name'] = tweet.screen_name
        data['timestamp'] = tweet.timestamp
        data['timestamp_epochs'] = tweet.timestamp_epochs
        data['text'] = tweet.text
        #print(tweet.text)
'''

    #data_array[0] = data
    #count = 0


    #data[count] = "aa"
    json_object_array = []
    data = {}
    data['aa'] = "aa"
    data['screen_name'] = "tweet.screen_name"
    s = "fsdf"
    for tweet in query_tweets_from_user("realDonaldTrump", limit=1):
        #print(tweet.text)        
        s = tweet.text
        print(s)
        json_dump = json.dumps(data)
        json_object_array.append(json.loads(json_dump))
    #for count in range(20):
        #data[count] = "ss"
        #json_dump = json.dumps(data)
        #json_object_array.append(json.loads(json_dump))
    #print(data)
    with open('data.json', 'w') as f:
        json.dump(json_object_array, f, ensure_ascii=False, indent=2)


print("Done!")

if __name__ == '__main__':
    main()
