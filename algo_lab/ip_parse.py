# coding: utf-8
# @Time : 8/24/21 9:04 AM

# source：@王争的算法学堂：https://www.xzgedu.com/detail/v_60a0a823e4b01e969a616c38/3?from=term_60ea9bb4ac981_EIkNO1&type=25

# IP 地址解析（拼多多面试）
# 给定一个字符串表示的 IP 地址，比如"123.92.2.34"，判断其是否合法。合法 IP 地址的规则如下：
# a. 除了空格、数字和"."之外，不得包含其他字符。
# b. IP 地址由四个数字构成，由"."分割，每个"."隔开的数字大小在 0~255 之间
# c. 数字前后可以有空格，但中间不能有空格。比如"123 . 92.2 . 34 "合法，" 12 3. 9 2.2. 34" 非法

# 当然，这个问题还可以继续加一些规则，让题目变得更加复杂，比如每个数字不能有前导 0，但可以为 0,比如"021.3.02.34"非法，"0.2.0.33"合法


# 解题过程
# step 1：举例读懂题意，梳理题目要求
# step 2：列出测试用例（测试驱动开发）
# step 3：总结归纳出处理思路（把逻辑中重复的部分抽象出来）
# step 4：第一轮编写代码（写注释，当代码模块化，逻辑更清楚）
# step 5：使用测试用例验证代码，并完善代码

# '123.92.2.34' 合法
# ' 123. 91 .12 .31 ' 合法
# '12. 12 .2 1.12' 非法 - 空格在中间
# '259.123.2.31' 非法 - 数字超过有效范围
# '251。123.2.31' 非法 - 分割段非 "." 字符
# '231.23.1' 非法 - IP 地址段由四段构成
# '233..33.2' 非法 - 子字段无值
# '1a.23.1.21' 非法 - 地址段字符非数字
# "", None 非法 - 为空

def check_ip_valid(ip):
    def _is_valid_ip(single_ip):
        # 校验是否是正整数的情况
        if not single_ip.isdigit():
            return False
        # 校验数字合法范围
        ip_num = int(single_ip)
        if not 0 <= ip_num <= 255:
            return False
        return True

    # 校验空情况
    if not ip:
        return False
    # 分段情况
    if len(ip.split(".")) != 4:
        return False
    # 判断每一段是否合法的情况
    part_ips = ip.split('.')
    for per_ip in part_ips:
        if not _is_valid_ip(per_ip.strip()):
            return False
    return True


assert check_ip_valid('123.92.2.34') is True
assert check_ip_valid(' 123. 91 .12 .31 ') is True
assert check_ip_valid('12. 12 .2 1.12') is False
assert check_ip_valid('259.123.2.31') is False
assert check_ip_valid('251。123.2.31') is False
assert check_ip_valid('231.23.1') is False
assert check_ip_valid('233..33.2') is False
assert check_ip_valid('1a.23.1.21') is False
assert check_ip_valid('') is False

