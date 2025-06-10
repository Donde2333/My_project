
class Student():
    count = 0
    # __slots__ = ("name", "age", "score")  # 限制实例的属性，对继承的子类无效

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        Student.count += 1

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


s1 = Student("Yan", 100)
s2 = Student("Li", 99)
print(f"姓名：{s1.get_name()}\n成绩：{s1.get_score()}")
print(Student.count)


class Student2():
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s3 = Student2()
s3.score = 99
print(s3.score)
