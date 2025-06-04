# -*- coding: utf-8 -*-

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
s1 = ['adam', 'LISA', 'barT']


def normalize(name):
    return name[0].upper() + name[1:].lower()


s2 = list(map(normalize, s1))
print(s2)
