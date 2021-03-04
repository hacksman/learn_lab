# coding: utf-8
# @Time : 2021/2/25 7:50 AM

from loguru import logger

import inspect

from .obj import News
from glom import glom

from datetime import datetime


class BaseParser:
    pass


class JsonFormatParser(BaseParser):

    def __init__(self):
        pass

    def __get_all_method(self):
        instance_members = inspect.getmembers(self, predicate=inspect.ismethod)
        return map(lambda x: x[0], filter(lambda x: not x[0].startswith("_"), instance_members))

    def parse(self, topic, result):

        # topic 不可以命名成 parse
        if topic in ["parse"]:
            raise ValueError(f"topic 不可以命名成 parse")

        if topic not in self.__get_all_method():
            raise ValueError(f"没有找到可用的解析函数:topic={topic}\tall_method_name={all_method_name}")

        return getattr(self, topic)(result)

    def zhihu(self, result):

        all_result = []

        for per_result in result["data"]:
            try:
                n = News(
                    platform="zhihu",
                    title=glom(per_result, "target.title"),
                    url=glom(per_result, "target.url"),
                    reply_cnt=int(glom(per_result, "target.answer_count")),
                    summary=(glom(per_result, "target.excerpt")),
                )
                all_result.append(n)
            except Exception as e:
                logger.error(f"解析 知乎 数据错误：")
                logger.error(f"per_result={per_result}")
                logger.exception(e)

        return all_result

    def v2ex(self, result):

        all_result = []

        for per_result in result:
            try:
                n = News(
                    platform="v2ex",
                    title=per_result.get("title"),
                    url=per_result.get("url"),
                    publish_time=str(datetime.fromtimestamp(per_result.get("created"))),
                    summary=per_result.get("content"),
                    reply_cnt=int(per_result.get("replies", -1))
                )
                all_result.append(n)
            except Exception as e:
                logger.error(f"解析 v2ex 数据错误:")
                logger.error(f"per_result={per_result}")
                logger.exception(e)
        return all_result

    def bilibili(self, result):

        all_result = []

        for per_result in glom(result, "data.list"):
            try:
                n = News(
                    platform="bilibili",
                    title=per_result.get("title"),
                    url=f"https://www.bilibili.com/video/{per_result.get('bvid')}",
                    summary=per_result.get("desc"),
                    reply_cnt=int(glom(per_result, "stat.reply", default=-1)),
                    publish_time=str(datetime.fromtimestamp(per_result.get("ctime")))
                )
                all_result.append(n)
            except Exception as e:
                logger.error(f"解析 b站 数据错误：")
                logger.error(f"per_result={per_result}")
                logger.exception(e)

        return all_result

