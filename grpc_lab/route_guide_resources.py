# coding: utf-8
# @Time : 2021/3/22 5:18 PM

from loguru import logger

import json

from grpc_lab.grpc_raw_code import route_guide_pb2


def read_route_guide_database():

    feature_list = []
    with open("route_guide_db.json") as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            feature = route_guide_pb2.Feature(
                name=item["name"],
                location=route_guide_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"])
                )
            feature_list.append(feature)
    return feature_list