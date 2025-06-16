# -*- coding:utf-8 -*-

from collections import namedtuple, Counter

point = namedtuple("point", ["x", "y"])  # 常用于创建坐标的函数
print(point)

p = point(1, 2)
print(p.x, p.y)

c = Counter("programming")  # 简单的字符计数器 可以使用c = Counter() 来定义一个空的计数器，配合下面的for语句
print(c)  # 第1次计数
for ch in "programming":
    c[ch] += 1
print(c)  # 第2次计数
c.update("hello")
print(c)  # 第3次计数
print(sorted(c))  # 排序-字符
print(sorted(c.items()))  # 排序-字符+值
print(sorted(c.items(), key=lambda x: x[1]))  # 排序-按值
