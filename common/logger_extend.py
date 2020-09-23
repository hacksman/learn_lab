# -*- encoding: utf-8 -*-
# @Time :2020/4/24 3:13 PM

import os

from loguru import logger


class LoggerExtend(object):
    # 存放目录名称
    folder = '../logs'

    def __init__(self, filename, folder=None):

        self.folder = folder or self.folder

        if not os.path.exists(self.folder):
            os.mkdir(self.folder)

        self.file = self.folder + '/' + filename

        logger.add(self.file, rotation="100 MB")

    @property
    def get_logger(self):
        return logger


if __name__ == '__main__':
    logger = LoggerExtend(os.path.basename(__file__).replace(".py", ".log")).get_logger

    logger.info("你好aaa")
