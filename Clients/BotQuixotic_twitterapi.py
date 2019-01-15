import requests
from quixotic_credentials import *
import twitter
import pytz
from datetime import datetime
import re
import random


api = twitter.Api(consumer_key=quix_consumer_key,
                  consumer_secret=quix_consumer_secret,
                  access_token_key=quix_access_token,
                  access_token_secret=quix_access_token_secret,
                  tweet_mode='extended')


# records current time in timestamp log
def record_current_time():
    time_tracker = open('BabelBots/Clients/quixotic_run_time.txt','w')
    time = datetime.utcnow().replace(tzinfo=pytz.utc)
    time_string = datetime.strftime(time, "%a %b %d %H:%M:%S %Y")
    time_tracker.write(time_string)

# reads time string from file
def read_timestamp():
    time_tracker = open('BabelBots/Clients/quixotic_run_time.txt', 'r')
    time_string = time_tracker.readline()
    return parse_time(time_string)

# converse time string to datetime
def parse_time(time_string):
    time = datetime.strptime(time_string.rstrip(), "%a %b %d %H:%M:%S %Y")
    return time

# Returns true/false if the mention has occured since last run time
def needs_response(time_of_mention):
    return parse_time(time_of_mention) > read_timestamp()

def new_mentions():
    mentions = api.GetSearch(raw_query="q=%40botquixotic&src=typd")
    print(mentions)

    mentions_list = []
    for mention in mentions:
        if "RT" in mention.full_text:
            pass
        else:
            user_mention = []
            timestamp = re.sub(r'\+0000 ', '', mention.created_at)
            if needs_response(timestamp):
                user_mention.append(mention.user.screen_name)
                user_mention.append(mention.id)
                mentions_list.append(user_mention)
                print("FOUND RECENT MENTION")
                print(user_mention)

    return mentions_list

def check_punctuation(tweet):
    punctuation = [".","!","?"]
    if tweet[-1] in punctuation:
        return tweet
    else:
        return tweet + random.choice(punctuation)


def get_timeline(screen_name):
    all_updates = api.GetUserTimeline(screen_name=screen_name, count=200, exclude_replies=True, include_rts=False)
    text = []
    for status in all_updates:
        tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', status.full_text)
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
    for friend in results:
        pending = api.OutgoingFriendship()
        if friend.id in pending:
            pass
        else:
            api.CreateFriendship(user_id=friend.id)
            print("friended: " + friend.screen_name)


def post_mention(screen_name, prose, id):
    prose = "@" + screen_name + " " + prose + screen_name
    api.PostUpdate(prose, in_reply_to_status_id=id)
    print("POSTED:")
    print(prose)
    record_current_time()
    print("NEW TIMESTAMP:")
    print(read_timestamp())

def post_prose(prose):
    api.PostUpdate(prose)



new_mentions()
