# -- coding: utf-8 -*-
import csv

fpath = "demo/packing_list.csv"

data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

try:
    with open(fpath, "r", encoding="utf-8") as file:
        file_read = csv.reader(file)
        for row in file_read:
            print(row)
except FileNotFoundError as e:
    print("未找到装箱单文件。正在创建一个新的……")
    with open(fpath, "w", encoding="utf-8") as file:
        file_write = csv.writer(file)
        file_write.writerow(data)
finally:
    print("运行结束……")
