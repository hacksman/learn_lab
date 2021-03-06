# coding: utf-8
# @Time : 2021/3/6 8:26 AM


import pandas as pd

from loguru import logger
from faker import Faker
from columnar import columnar
from tabulate import tabulate

fake = Faker()
Faker.seed(4321)


def gen_faker_data():
    datas = []
    for i in range(10):
        item = [
            "".join(fake.file_path(depth=2, extension="").split(".")[:-1]),
            fake.uri(),
            fake.random_int(min=1, max=9),
            fake.pybool(),
            fake.random_element(elements=("on", "off")),
            fake.date_time_this_month(),
            fake.date_time_between(start_date='-10m', end_date="now"),
        ]
        datas.append(item)
    return datas


def raw_log(results, headers):
    for per_item in results:
        log_item = ""
        for idx, head in enumerate(headers):
            log_item += f"{head}={per_item[idx]}\t"
        logger.info(log_item)


def columnar_log(results, headers):
    table = columnar(results, headers, column_sep="\t", terminal_width=5120)
    logger.info(table)


def pandas_log(results, headers):
    pd.options.display.width = None
    pd.options.display.max_colwidth = None
    df_result = pd.DataFrame(results, columns=headers)
    logger.info(f"\n{df_result.to_string(index=False)}")


def tabulate_log(results, headers):
    logger.info(f"\n{tabulate(pd.DataFrame(results), headers=headers, tablefmt='psql', showindex=False)}")


if __name__ == '__main__':
    results = gen_faker_data()
    headers = ["root_path", "url", "priority", "is_once", "switch", "created", "updated"]
    raw_log(results, headers)
    columnar_log(results, headers)
    pandas_log(results, headers)
    tabulate_log(results, headers)
