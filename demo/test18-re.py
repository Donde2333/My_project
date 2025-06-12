# -*- coding:utf-8 -*-

# \d 数字
# \w 字母
# \s 空格或者tap
# * 全部
# + 至少一个
# ？0个或1个
# {n} 表示n个字符
# {n,m}表示n-m个字符
# []表示范围例如：[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
# A|B A或者B
# ^表示行的开头
# $表示行的结尾

import re
# 常见用法1
test = '用户输入的字符串'  # 用户输入的字符串
if re.match(r'正则表达式', test):  # 返回的是一个match对象，不是bool值
    print('ok')
else:
    print('failed')

# 常见用法2
list_split = re.split(r'[\s\,\;]+', 'a,b;; c  d')
print(list_split)

# re 常用方法： re.match 比对   re.split 切分 re.group 获取分组 re.compile 预编译
