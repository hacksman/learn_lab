# coding: utf-8
# @Time : 2021/2/25 7:52 AM

from loguru import logger

from abc import ABC, abstractmethod

from cattr import unstructure


class BaseSaver(ABC):

    def _unpack_struct(self, data_obj):
        return unstructure(data_obj)

    @abstractmethod
    def save(self, objs):
        pass


class MongoSaver(BaseSaver):

    def save(self, objs):
        unpack_data = list(map(self._unpack_struct, objs))
        logger.info(f"save all data to mongo {unpack_data}")


class MysqlSaver(BaseSaver):

    def save(self, objs):
        unpack_data = list(map(self._unpack_struct, objs))
        logger.info(f"save all data to mysql {unpack_data}")


class ExcelSaver(BaseSaver):

    def save(self, objs):
        unpack_data = list(map(self._unpack_struct, objs))
        logger.info(f"save all data to excel {unpack_data}")
