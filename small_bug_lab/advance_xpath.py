# coding: utf-8
# @Time : 2021/4/2 3:54 PM

from loguru import logger

# import requests
#
# from lxml.etree import HTML, XML, tostring, tounicode, fromstring, HTMLParser
#
# res = requests.get("http://example.com/")
#
# # doc = HTML(res.text)
#
# doc = fromstring(res.text, parser=HTMLParser())
#
# doc_find = doc.find("./")
#
# print(doc)
#
# q_infos = {"a": "a", "b": "b"}
#
# for q_k, q_v in q_infos.items():
#     r = XML(f"<div {q_k}='{q_v}_234567'></div>")
#     print(r)
#     doc_find.addnext(r)
#
# # doc_find.addnext(XML("<div style='clear: both'>1111111111222222222333333333</div>"))
# print(f"\n")
# print(f"\n")
# print(f"\n")
# print(f"\n")
#
# print(tostring(doc).decode('utf-8'))
#
# a = doc.xpath("string(//div/@a)")
#
# print(f">>>>>>", a)

#
# t = doc.xpath("/*")[0]
# print(t)
# print("resut>>>>\n")
# print(tounicode(t))
# t.addnext(XML("<div>你好</div>"))
#
# print(f"*"*20)
#
# print('\n')
# print('\n')
# print('\n')
# print('\n')
#
#
# print(tounicode(doc))


import elementpath

# translate('The quick brown fox', ' ', ';')

import elementpath
from xml.etree import ElementTree
root = ElementTree.XML('<A><B1/><B2><C1/><C2/><C3/></B2></A>')
a = elementpath.select(root, 'string-join(*)')

from lxml.etree import tostring

for i in a:
    print(i)


