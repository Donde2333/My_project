
class student():
    count = 0

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        student.count += 1

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


s1 = student("Yan", 100)
s2 = student("Li", 99)
print(f"姓名：{s1.get_name()}\n成绩：{s1.get_score()}")
print(student.count)
