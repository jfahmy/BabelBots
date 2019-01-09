# this is just a test file
from __future__ import print_function

import grpc
import twitterapi

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

from time import sleep

file_location = 'http://www.gutenberg.org/cache/epub/996/pg996.html'
# file_location = 'https://en.wikipedia.org/wiki/Abraham_Lincoln'
# file_location = 'https://www.manrepeller.com/2019/01/january-horoscope-2019-man-repeller.html'

# block_of_text = ["Last April, Abbi Jacobson and Ilana Glazer, the creators, writers and stars of Comedy Central’s Broad City announced that the fifth season, slated to air on January 24th of this year, would be the show’s last in spite of its successful stats — the show averages 1.2 million viewers per episode and has consistently won awards season after season since its launch in 2014. In an interview with the New York Times that ran last Thursday, Glazer and Jacobson explained their ending. Before, part of the joke was, ha ha, these white girls don’t have to grow.", "Because in your early 20s, you’re the same idiot, over and over and over again. And then Season 4, we couldn’t help but grow because we were so angry and disgusted with ourselves,” Glazer said, adding, We needed to set these personal and creative boundaries, to keep the show as high-quality as it remains. That takes a limb. It takes an entire arm. I’ve got no limbs left.",
# "My head's cut off on the fifth [season]. I’ve got left to give. There’s just a torso on the floor. ", "The interview goes on to share some information on the creative pursuits that will follow, peppering in more elaborate details on precisely why Broad City couldn’t make sense past a season 5, but more interesting than the isolated anecdote of their show’s end is the seeming power play — and trend — of an elective shutdown. In November of last year, Tavi Gevinson announced that she would be closing Rookie because it was no longer “financially sustainable,” but then again — she wrote, “it is my decision—to not do the things that might make it financially sustainable, like selling it to new owners, taking money from investors, or asking readers for donations or subscriptions.", "In July 2017, Business of Fashion announced that Paris’ Colette, largely lauded for having carved the way for the concept shop, would be closing the following December in spite of reported earnings to the tune.

# def gen_tweet_space(text):
#     for tweet in text:
#         yield tweet

def run():
 channel = grpc.insecure_channel('localhost:50050')
 stub = ProseAndBabel_pb2_grpc.ProseAndBabelStub(channel)

 while True:
     users = twitterapi.new_mentions()
     for user in users:
         full_text = twitterapi.get_timeline(user[0])
         response = stub.UserMarkov(ProseAndBabel_pb2.UserTweets(tweets=full_text))
         twitterapi.post_mention(user[0], response.prose, user[1])
     # friends = twitterapi.new_friends
     # print(friends)
     # response = stub.UserMarkov(ProseAndBabel_pb2.UserTweets(tweets=twitterquery.usertweets(user)))

     #
     # iterator = iter(block_of_text)
     # response = stub.UserMarkov(ProseAndBabel_pb2.UserTweets(tweets=iterator))
     # response = stub.GetHaiku(ProseAndBabel_pb2.BabelRequest(ask=file_location))
     # # api.update_status(response.response + "#Haiku")
     # print("~~~~~~~~~~~~~")
     # print("Haiku posted:")
     # print(response.prose)
     # response = stub.GetBabel(ProseAndBabel_pb2.BabelRequest(ask=file_location))
     # print("~~~~~~~~~~~~~")
     # print("Markovian Babel:")
     # print(response.prose)
     # print("\n")
     sleep(20)

 # response = stub.GetHaiku(ProseAndBabel_pb2.BabelRequest(ask=file_location))
 # print("A Haiku 4 U:")
 # print(response.response)
 # response = stub.GetBabel(ProseAndBabel_pb2.BabelRequest(ask=file_location))
 # print("Markovian Babel:")
 # print(response.response)

if __name__ == '__main__':
  run()
