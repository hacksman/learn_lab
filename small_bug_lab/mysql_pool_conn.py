# coding: utf-8
# @Time : 2021/3/6 2:58 PM

import datetime
from dbutils.pooled_db import PooledDB
from typing import Tuple
import pymysql
import time


class MysqlClient(object):
    __pool_map = {}
    __pool = None

    def __init__(self, host, port,
                 db, user, password,
                 mincached=2, maxcached=12, maxshared=10, maxconnections=100, blocking=True,
                 maxusage=100, setsession=["set autocommit = 1"], reset=True, charset='utf8mb4'
                 ):
        """
        :param host:数据库ip地址
        :param port:数据库端口
        :param db:库名
        :param user:用户名
        :param passwd:密码
        :param mincached:连接池中空闲缓存连接的初始数量
        :param maxcached:连接池中空闲缓存连接的最大数量
        :param maxshared:共享连接的最大数量
        :param maxconnections:创建连接池的最大数量
        :param blocking:超过最大连接数量时候的表现，为True等待连接数量下降，为false直接报错处理
        :param maxusage:单个连接的最大重复使用次数
        :param setsession: 开始会话的前置操作，如. ["set datestyle to ...", "set time zone ..."]
        :param reset: 当连接放回连接池时，是否每次都调用 rollback 以保证事务终止，为 False 或 None 就不额外调用 rollback 方法
        :param charset:字符编码
        """

        if not self.__pool_map.get((host, port, db, user, password)):
            self.__class__.__pool = PooledDB(pymysql,
                                             mincached, maxcached,
                                             maxshared, maxconnections, blocking,
                                             maxusage, setsession, reset,
                                             host=host, port=port, db=db,
                                             user=user, passwd=password,
                                             charset=charset,
                                             cursorclass=pymysql.cursors.DictCursor
                                             )
            self.__class__.__pool_map[(host, port, db, user, password)] = self.__class__.__pool
        else:
            self.__class__.__pool = self.__class__.__pool_map.get((host, port, db, user, password))

        self._conn = None
        self._cursor = None
        self.__get_conn()

    def __get_conn(self):
        self._conn = self.__pool.connection()
        self._cursor = self._conn.cursor()

    def close(self):
        try:
            self._cursor.close()
            self._conn.close()
        except Exception as e:
            print(e)

    @staticmethod
    def __dict_datetime_obj_to_str(result_dict):
        """把字典里面的datatime对象转成字符串，使json转换不出错"""
        if result_dict:
            result_replace = {k: v.__str__() for k, v in result_dict.items() if isinstance(v, datetime.datetime)}
            result_dict.update(result_replace)
        return result_dict

    def select_one(self, sql: str, param: set = ()) -> None or dict:
        """查询单个结果"""
        self.execute(sql, param)
        result = self._cursor.fetchone()
        result = self.__dict_datetime_obj_to_str(result)
        return result

    def select_many(self, sql: str, param: set = ()) -> iter:
        """
        查询多个结果
        :param sql: sql语句
        :param param: sql参数
        :return: 结果的迭代器
        """
        self.execute(sql, param)
        for item in self._cursor._cursor:
            item = self.__dict_datetime_obj_to_str(item)
            yield item

    def execute(self, sql: str, param: set = ()) -> int:
        count = self._cursor.execute(sql, param)
        return count

    def execute_many(self, sql: str, params: list) -> int:
        """
        :param sql:
        :param params:
        :return:
        """
        count = self._cursor.executemany(sql, params)
        return count

    def begin(self):
        """开启事务"""
        self._conn.begin()

    def end(self, succeed=True):
        """结束事务"""
        if succeed:
            self._conn.commit()
        else:
            self._conn.rollback()


if __name__ == "__main__":
    local = {
        "host": "127.0.0.1",
        "port": 3306,
        "db": "test_demo",
        "user": "root",
        "password": "play10086"
    }

    # 测试查看在最小缓存初始化缓存
    local_mysql = MysqlClient(**local)
    # time.sleep(5)
    # 测试查看单例模式
    # local_mysql_again = MysqlClient(**local)
    # time.sleep(5)

    # 测试 insert many
    # values = list(map(lambda x: (f"小姐姐{x}号", x, "女", datetime.datetime.now(), datetime.datetime.now()), range(10)))
    # print(values)
    # insert_many_sql = 'INSERT INTO `anchor` values (%s, %s, %s, %s, %s)'
    # insert_count = local_mysql.execute_many(insert_many_sql, values)
    # print(f"总共插入「{insert_count}」条数据")

    # 测试 select many
    select_many = 'SELECT * FROM `anchor`'
    for item in local_mysql.select_many(select_many):
        print('select_many 数据>>>>', item)

    # # 测试查询不存在的数据
    # select_not_exist = "SELECT * FROM `anchor` WHERE nickname=%s"
    # not_exist_result = local_mysql.select_one(select_not_exist, "鸡仔说")
    # print(f"not exist select one 数据>>>{not_exist_result}")

    # 测试事务操作
    # sql_insert_one = 'INSERT INTO `anchor` value (%s, %s, %s, %s, %s)'
    # insert_one_value = ("小姐姐10号", 10, "女", datetime.datetime.now(), datetime.datetime.now())
    # local_mysql.begin()
    # local_mysql.execute(sql_insert_one, insert_one_value)
    # print(f"事务测试，已经执行了插入操作，快去数据库查看一下，目前数据应该还没有执行，等待确认操作...")
    # time.sleep(10)
    # print(f"即将执行确认操作")
    # time.sleep(1)
    # local_mysql.end(succeed=True)
    # print(f"已确认执行操作，请再次查看数据库...")

