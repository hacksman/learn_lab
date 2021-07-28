# coding: utf-8
# @Time : 2021/6/5 8:19 PM

import requests


class DownloaderHandle:

    @classmethod
    def fetch(cls, url, **kwargs):
        res = requests.get(url, **kwargs)
        return res


