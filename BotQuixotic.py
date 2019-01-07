# this is just a test file
from __future__ import print_function

import grpc

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

import tweepy
from time import sleep
from credentials import *

file_location = 'http://www.gutenberg.org/cache/epub/996/pg996.html'
# file_location = 'https://en.wikipedia.org/wiki/Abraham_Lincoln'
# file_location = 'https://www.manrepeller.com/2019/01/january-horoscope-2019-man-repeller.html'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def run():
 channel = grpc.insecure_channel('localhost:50050')
 stub = ProseAndBabel_pb2_grpc.ProseAndBabelStub(channel)

 while True:
     response = stub.GetHaiku(ProseAndBabel_pb2.BabelRequest(ask=file_location))
     # api.update_status(response.response + "#Haiku")
     print("~~~~~~~~~~~~~")
     print("Haiku posted:")
     print(response.response)
     response = stub.GetBabel(ProseAndBabel_pb2.BabelRequest(ask=file_location))
     print("~~~~~~~~~~~~~")
     print("Markovian Babel:")
     print(response.response)
     print("\n")
     sleep(5)

 # response = stub.GetHaiku(ProseAndBabel_pb2.BabelRequest(ask=file_location))
 # print("A Haiku 4 U:")
 # print(response.response)
 # response = stub.GetBabel(ProseAndBabel_pb2.BabelRequest(ask=file_location))
 # print("Markovian Babel:")
 # print(response.response)

if __name__ == '__main__':
  run()
