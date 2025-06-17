# -*- coding:utf-8 -*-

from hashlib import md5
import random

db = {}


class User():
    def __init__(self, username, password):
        self.__username = username
        self.__salt = ''.join([chr(random.randint(48, 122))
                              for i in range(20)])
        _password_with_salt = password + self.__salt
        self.__password_md5 = md5(
            _password_with_salt.encode("utf-8")).hexdigest()

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password_md5

    def get_salt(self):
        return self.__salt

    def check_password(self, password):
        _input_password_with_salt = password + self.__salt
        input_md5 = md5(_input_password_with_salt.encode("utf-8")).hexdigest()
        return input_md5 == self.__password_md5


def register(username, password):
    user = User(username, password)
    db[user.get_username()] = user


def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username in db and db[username].check_password(password) == True:
        print(f"欢迎回来，{username}！")
    else:
        print("用户名或密码错误！")


if __name__ == "__main__":
    register("yan", "123")
    register("li", "123")
    login()
