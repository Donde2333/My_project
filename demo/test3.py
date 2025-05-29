# -*- coding: utf-8 -*-

# 创建一个python程序，输出从 1 到 100 的数字。
# 问题在于：
# 对于 3 的倍数，打印“Fizz”而不是数字。
# 对于 5 的倍数，打印“Buzz”而不是数字。
# 这是棘手的部分：对于 3和5 的倍数，打印“FizzBu​​zz”。

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
