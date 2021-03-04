# coding: utf-8
# @Time : 2021/2/25 5:34 PM

from attr import attrs, attrib, validators

@attrs
class News:
    _platform = attrib(type=str, validator=validators.instance_of(str))

    title = attrib(type=str, validator=validators.instance_of(str))
    url = attrib(type=str, validator=validators.instance_of(str))
    reply_cnt = attrib(type=int, validator=validators.instance_of(int), default=-1)
    summary = attrib(type=str, validator=validators.instance_of(str), default="")
    publish_time = attrib(type=str, validator=validators.instance_of(str), default="")