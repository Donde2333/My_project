# -*- coding: utf-8 -*-
from functools import reduce


def f(x):
    return x * x


def fn(x, y):
    return x * 10 + y


def add(x, y):
    return x + y


# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
r1 = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r1))

r2 = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(r2)

r3 = reduce(add, [1, 3, 5, 7, 9])
r4 = sum([1, 3, 5, 7, 9])
print(r3, r4)

r5 = reduce(fn, [1, 3, 5, 7, 9])
print(r5)


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


r6 = reduce(fn, map(char2num, '13579'))

print(r6)


# 检查一个整数是否是回数 filter函数
def is_palindrome(n):
    return str(n) == str(n)[::-1]  # 将数字转换为字符串后比较正反序


palindromes = list(filter(is_palindrome, range(100)))
print(palindromes)


# 排序 sorted函数 key=条件函数 reverse=
s3 = sorted([36, 5, -12, 9, -21])
print("排序:", s3)

s4 = sorted([36, 5, -12, 9, -21], key=abs)
print("绝对值排序：", s4)

name2 = ['bob', 'about', 'Zoo', 'Credit']
s5 = sorted(name2, key=str.lower)
s6 = sorted(name2, key=str.lower, reverse=True)
print(s5)
print(s6)
