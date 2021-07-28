# coding: utf-8
# @Time : 2021/3/27 8:29 AM

import six
import re
import os
from os import path, listdir
from loguru import logger


def root_path(current_path=None, pattern=None):
    DEFAULT_ROOT_FILENAME_MATCH_PATTERN = '.git|requirements.txt'

    current_path = current_path or os.getcwd()
    current_path = path.abspath(path.normpath(path.expanduser(current_path)))
    pattern = pattern or DEFAULT_ROOT_FILENAME_MATCH_PATTERN

    if not path.isdir(current_path):
        current_path = path.dirname(current_path)

    def find_root_path(current_path, pattern=None):
        if isinstance(pattern, six.string_types):
            pattern = re.compile(pattern)

        detecting = True

        while detecting:
            file_names = listdir(current_path)
            found_more_files = bool(len(file_names) > 0)

            if not found_more_files:

                return None

            root_file_names = filter(pattern.match, file_names)
            root_file_names = list(root_file_names)

            found_root = bool(len(root_file_names) > 0)

            if found_root:

                return current_path

            found_system_root = bool(current_path == path.sep)

            if found_system_root:
                return None

            current_path = path.abspath(path.join(current_path, '..'))

    return find_root_path(current_path, pattern)
