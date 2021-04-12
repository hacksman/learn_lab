# coding: utf-8
# @Time : 2021/3/27 8:43 AM


from tool.log_ext import LogExt

log = LogExt().get_logger


def division(a, b):
    return a / b

#
# # 仅捕获原因
# try:
#     d = division(1, 0)
# except Exception as e:
#     log.error(f"error happened reason: {e}")


# 打印堆栈信息
# try:
#     d = division(1, 0)
# except Exception as e:
#     log.exception(e)


# 以每一行的形式打印出来
import sys, traceback
try:
    d = division(1, 0)
except Exception as e:
    for e_info in traceback.format_exception(*sys.exc_info()):
        for _ in e_info[:-1].split("\n"):
            log.tback(_)
