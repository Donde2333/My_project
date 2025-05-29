# -- coding: utf-8 -*-

total = 0
number = int(input("你给我说给数:"))

for x in range(1, number+1):
    total = total + x ** 2
print("这个数的平方和是：", total)
