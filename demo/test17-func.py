# -- coding: utf-8 -*-

import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']  # 姓名前缀
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']  # 姓名后缀


def create_fantasy_name(list_1, list_2):  # 创建随机姓名的函数
    return random.choice(list_1) + ' ' + random.choice(list_2)


def fire_in_name(name):  # 判断姓名中是否包含FIRE的函数
    return "FIRE" in name


def concatenate_names(name1, name2):  # 把列表里的姓名加起来显示的函数
    return name1 + " " + name2


def get_reduce_name_fire(name):
    filter_list = list(filter(fire_in_name, name))
    if filter_list:
        reduce_name = reduce(concatenate_names, filter_list)
        return reduce_name
    else:
        return "oi !It's empty!"


def display_name_info():
    random_names = [create_fantasy_name(
        prefixes, suffixes) for x in range(5)]  # 随机5个姓名
    name_upper = list(map(lambda name: name.upper(),
                          random_names))  # 把随机的名字全部转化为大写
    print(f"随机了5个名字：{name_upper}")
    reduce_name = get_reduce_name_fire(name_upper)
    print(f"里面包含FIRE的名字有：{reduce_name}")


if __name__ == "__main__":
    display_name_info()
