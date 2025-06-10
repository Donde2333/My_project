# -- coding: utf-8 -*-
import csv


class My_file():
    def __init__(self, path):
        self.path = path  # 存储路径到实例属性

    def file_reads(self):
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                file_read = csv.reader(file)
                return list(file_read)  # 读取所有内容并返回列表
        except FileNotFoundError:
            return None  # 文件不存在时返回None

    def file_writes(self, data):
        with open(self.path, "w", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)  # 直接写入数据


# 使用示例
fpath = "demo/packing_list.csv"  # 使用相对路径
data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

new_file = My_file(fpath)
try:
    content = new_file.file_reads()
    if content is None:  # 检查文件是否存在
        print("未找到装箱单文件。正在创建一个新的……")
        new_file.file_writes(data)
    else:
        for row in content:
            print(row)
finally:
    print("运行结束……")
