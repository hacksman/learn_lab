# coding: utf-8
# @Time : 2021/3/22 5:38 PM


import sys

sys.path.append("..")

from loguru import logger

import random

import grpc

from grpc_lab.grpc_raw_code import route_guide_pb2
from grpc_lab.grpc_raw_code import route_guide_pb2_grpc
from grpc_lab import route_guide_resources


def guide_get_one_feature(stub, point):
    feature = stub.GetFeature(point)
    if not feature.location:
        print(f"Server returned incomplete feature")    
        return 
    if feature.name:
        print(f"Feature called {feature.name} at {feature.location}")
    else:
        print(f"Found no feature at {feature.location}")


def guide_get_feature(stub):
    guide_get_one_feature(stub, route_guide_pb2.Point(latitude=409146138, longitude=-746188906))
    guide_get_one_feature(stub, route_guide_pb2.Point(latitude=0, longitude=0))


def run():

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print(f"-----------------GetFeature----------------")
        guide_get_feature(stub)

if __name__ == '__main__':
    run()


