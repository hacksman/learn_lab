# coding: utf-8
# @Time : 2021/2/25 7:49 AM

from loguru import logger
from abc import (ABC, abstractmethod)

import requests


class BaseSpider(ABC):

    _headers = {
        'accept': 'application/json, text/plain, */*',
        "accept-encoding": "gzip, deflate, br",
        "cache-control": "no-cache",
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Ch'
                      'rome/84.0.4147.135 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        "pragma": "no-cache",
    }

    @abstractmethod
    def spider(self):
        pass


class ZhihuSpider(BaseSpider):

    url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true"

    def spider(self):
        resp = requests.get(self.url, headers=self._headers)
        return resp.json()


class V2exSpider(BaseSpider):

    url = "https://www.v2ex.com/api/topics/hot.json"

    def spider(self):
        resp = requests.get(self.url, headers=self._headers)

        return resp.json()


if __name__ == '__main__':
    z = ZhihuSpider()
    print(z.spider())

    v = V2exSpider()
    print(v.spider())