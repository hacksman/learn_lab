# coding: utf-8
# @Time : 2021/3/27 8:25 AM

import os

from loguru import logger

from tool.victorinox import root_path

from functools import partialmethod

logger.__class__.tback = partialmethod(logger.__class__.log, "TBACK")

logger.level("TBACK", no=35, icon="🤒", color="<light-red>")


class LogExt(object):

    folder = f'{root_path()}/logs'

    __default_file_name = "default.log"

    single_logger = {}

    def __init__(self, filename=None, folder=None, **kwargs):

        self.file_name = filename

        if filename not in self.single_logger:

            filename = filename or self.__default_file_name

            self.folder = folder or self.folder

            if not os.path.exists(self.folder):
                os.mkdir(self.folder)

            self.file = f"{self.folder}/{filename}"

            retention = kwargs.get("retention") or 10

            rotation = kwargs.get("rotation") or "10 MB"

            self.i = logger.add(self.file, retention=retention, rotation=rotation)

            self.single_logger[self.file_name] = logger

    @property
    def get_logger(self):
        return self.single_logger[self.file_name]

