# coding: utf-8
# @Time : 2021/2/25 7:50 AM

from loguru import logger

from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def parse(self, topic, result):
        pass


class JsonFormatParser(BaseParser):

    def parse(self, topic, result):
        pass
