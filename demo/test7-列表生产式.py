import os

dict1 = {'x': '1', 'y': '2', 'z': '3'}
l = ['Hello', 'World', 'IBM', 'Apple']

list1 = [x*x for x in range(1, 11)]
list2 = [m+n for m in "ABC" for n in "123"]
list3 = [x*x for x in range(1, 11) if x % 2 == 0]
list4 = [d for d in os.listdir('.')]
list5 = [f"{key} = {value}" for key, value in dict1.items()]
list6 = [s.lower() for s in l]
list7 = [x if x % 2 == 0 else -x for x in range(1, 11)]

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
