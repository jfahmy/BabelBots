from __future__ import print_function
import grpc
import twitterapi
import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc
from time import sleep

file_location = 'http://www.gutenberg.org/cache/epub/996/pg996.html'

def run():
 channel = grpc.insecure_channel('localhost:50050')
 stub = ProseAndBabel_pb2_grpc.ProseAndBabelStub(channel)

 # response = stub.GetHaiku(ProseAndBabel_pb2.BabelRequest(ask=file_location))
 # twitterapi.post_prose(response.prose + "#QuixoticHaiku")


if __name__ == '__main__':
  run()
