# coding: utf-8
# @Time : 2021/2/26 6:04 PM

import inspect
from loguru import logger


class Output:

    def __all_custom_method(self):
        # return filter(lambda x: not x.startswith("_"), dir(self))
        instance_members = inspect.getmembers(self, predicate=inspect.ismethod)
        return map(lambda x: x[0], filter(lambda x: not x[0].startswith("_"), instance_members))

    def save(self, where, result):
        if where in ["save"]:
            raise ValueError(f"Output can not use save")

        all_method = list(self.__all_custom_method())
        if where not in all_method:
            all_method.remove("save")
            raise ValueError(f"Output only support {all_method} but got {where}")
        getattr(self, where)(result)

    def mysql(self, result):
        logger.info(f"save {result} to mysql")
        return

    def mongo(self, result):
        logger.info(f"save {result} to mongo")
        return

    def excel(self, result):
        logger.info(f"save {result} to excel")
        return


if __name__ == '__main__':
    o = Output()
    # o.save("mongo", "→spider data←")
    # o.save("__init__", "→spider data←")
    # o.save("__name__", "→spider data←")
    # o.save("__ne__", "ccc")
    # o.save("save", "ccc")
    o.save("test_name", "→spider data←")
