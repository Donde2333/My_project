# d = {'a': 1, 'b': 2, 'c': 3}
# for key, value in d.items():
#     print(key, value)

l = input("你来输入一行字（前后有空格）：")
l_org = [l]
l_none = len(l)


def itm(str_l):
    if not str_l:
        return ""
    left = 0
    while left < len(str_l) and str_l[left] == " ":
        left += 1
    right = len(str_l) - 1
    while right >= 0 and str_l[right] == " ":
        right -= 1

    if left > right:
        return ""
    return str_l[left:right+1]


l = itm(l)
print(f"你原来写的是{l_org}，现在我帮你变成了{[l]}")
print(f"原本加空格有{l_none}个字，现在去掉了{l_none-len(l)}个空格")
