import requests
from credentials import *
import twitter
import pytz
from datetime import datetime
import re
import random


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret,
                  tweet_mode='extended')


# records current time in timestamp log
def record_current_time():
    time_tracker = open('previous_run_time.txt','w')
    time = datetime.utcnow().replace(tzinfo=pytz.utc)
    time_string = datetime.strftime(time, "%a %b %d %H:%M:%S %z %Y")
    time_tracker.write(time_string)

# reads time string from file
def read_timestamp():
    time_tracker = open('previous_run_time.txt', 'r')
    time_string = time_tracker.readline()
    return parse_time(time_string)

# converse time string to datetime
def parse_time(time_string):
    time = datetime.strptime(time_string, "%a %b %d %H:%M:%S %z %Y")
    return time

# Returns true/false if the mention has occured since last run time
def needs_response(time_of_mention):
    return parse_time(time_of_mention) > read_timestamp()

def new_mentions():
    mentions = api.GetSearch(raw_query="q=%40botquixotic&src=typd")

    mentions_list = []
    for mention in mentions:
        user_mention = []
        if needs_response(mention.created_at):
            user_mention.append(mention.user.screen_name)
            user_mention.append(mention.id)
            mentions_list.append(user_mention)

    record_current_time()
    return mentions_list

def check_punctuation(tweet):
    punctuation = [".","!","?"]
    if tweet[-1] in punctuation:
        return tweet
    else:
        return tweet + random.choice(punctuation)


def get_timeline(screen_name):
    all_updates = api.GetUserTimeline(screen_name=screen_name, count=5, exclude_replies=True)

    text = []
    for status in all_updates:
        tweet = re.sub(r'^https?:\/\/.*[\r\n]*', '', status.full_text)
        if tweet == "":
            pass
        else:
            tweet = re.sub(r'&amp;','&', tweet)
            tweet = check_punctuation(tweet)
            text.append(tweet)

    text = " ".join(text)
    return text


def new_friends():
    results = api.GetFollowers()
    return "stuff"

def post_mention(screen_name, prose, id):
    prose = "@" + screen_name + " " + prose + screen_name
    api.PostUpdate(prose, in_reply_to_status_id=id)
