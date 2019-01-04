# this is just a test file
from __future__ import print_function

import grpc

import ProseAndBabel_pb2
import ProseAndBabel_pb2_grpc

file_location = 'http://www.gutenberg.org/cache/epub/996/pg996.html'

def run():
 channel = grpc.insecure_channel('localhost:50050')
 stub = ProseAndBabel_pb2_grpc.ProseAndBabelStub(channel)
 response = stub.GetHaiku(ProseAndBabel_pb2.BabelRequest(ask=file_location))
 print("A Haiku 4 U:")
 print(response.response)
 # response = stub.GetBabel(ProseAndBabel_pb2.BabelRequest(ask=file_location))
 # print("Markovian Babel:")
 # print(response.response)

if __name__ == '__main__':
  run()
