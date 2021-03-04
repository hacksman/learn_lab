# coding: utf-8
# @Time : 2021/2/25 7:57 AM

import sys

import time

sys.path.append("..")

from loguru import logger

from lru_lab.spider import (ZhihuSpider, V2exSpider, BilibiliSpider)
from lru_lab.parser import JsonFormatParser

from lru_lab.saver import (ExcelSaver, MongoSaver, MysqlSaver)

from cattr import unstructure

from functools import lru_cache

from flask import (Flask, request)


spider_map = {
    "bilibili": BilibiliSpider().spider,
    "v2ex": V2exSpider().spider,
    "zhihu": ZhihuSpider().spider,
}

save_map = {
    "excel":  ExcelSaver().save,
    "mysql": MysqlSaver().save,
    "mongo": MongoSaver().save,
}


class LruCache:

    def __init__(self, maxsize=3, timeout=2):
        self.maxsize = maxsize
        self.timeout = timeout
        self.last_time = int(time.time())

    def __call__(self, func):

        func = lru_cache(maxsize=self.maxsize)(func)

        def wrapper(*args, **kwargs):
            if int(time.time()) - self.last_time > self.timeout:
                logger.debug(func.cache_info())
                func.cache_clear()
                self.last_time = int(time.time())
            return func(*args, **kwargs)
        return wrapper


@LruCache(maxsize=3, timeout=2)
def grab_hot(topic, save_method='excel'):

    spider = spider_map.get(topic)

    save = save_map.get(save_method)

    spider_result = spider()
    parse_result = JsonFormatParser().parse(topic, spider_result)

    save(parse_result)

    return list(map(unstructure, parse_result))


app = Flask(__name__)

# 让中文正常显示
app.config["JSON_AS_ASCII"] = False


@app.route("/", methods=["post"])
def index():
    res = request.json
    topic = res.get("topic")
    if not topic or topic not in spider_map:
        logger.warning(f"topic error:{topic}")
        return {"status": -1, "message": "未知主题"}

    save_method = res.get("save") or "excel"

    result = grab_hot(topic, save_method)

    # logger.info(grab_hot.cache_info())

    return {"status": 1, "results": result}


if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=True)
