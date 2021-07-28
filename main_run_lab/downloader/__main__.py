# coding: utf-8
# @Time : 2021/6/5 8:17 PM

import os
import sys

print(f">>>>{__package__}")

if not __package__:
    print(os.path.dirname(__file__), os.pardir)
    path = os.path.join(os.path.dirname(__file__), os.pardir)
    print(path)
    sys.path.append(path)
    print(sys.path)

from downloader.downloader_handle import DownloaderHandle

print(f"downloader start running...")

url = "https://www.baidu.com"

res = DownloaderHandle.fetch(url)

print(res)
