# -*- coding: utf-8 -*-

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。 map函数
s1 = ['adam', 'LISA', 'barT']


def normalize(name):
    return name[0].upper() + name[1:].lower()


s2 = list(map(normalize, s1))
print(s2)


# 假设我们用一组tuple表示学生名字和成绩 sorted函数
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print("按名字排序:", L2)
