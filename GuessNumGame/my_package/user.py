# -*- coding:utf-8 -*-

import hmac
import os
import random
import csv


class User():

    def __init__(self, path="GuessNumGame/data/user.csv"):
        self.__path = path

    def _read_users(self):
        """读取所有用户数据"""
        users_data = {}
        if not os.path.exists(self.__path):
            return users_data

        with open(self.__path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 3:  # 验证行数据完整性
                    users_data[row[0]] = (row[1], row[2])
            return users_data

    def _save_user(self, username, password_hash, key):
        """保存单个用户数据"""
        with open(self.__path, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, password_hash, key])

    def register(self, username, password):
        if not username or not password:
            return False, "用户名和密码不能为空"

        users_data = self._read_users()
        if username in users_data:
            return False, "用户名已存在"

        self.__username = username
        self.__key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.__password = hmac.new(self.__key.encode(
            "utf-8"), password.encode("utf-8"), digestmod="SHA256").hexdigest()
        self._save_user(self.__username, self.__password, self.__key)  # 写入数据
        return True, "注册成功！"

    def login(self, username, password):
        user_data = self._read_users()

        if username not in user_data:
            return False, "用户名不存在"

        user_password, user_key = user_data[username]

        input_password = hmac.new(user_key.encode(
            "utf-8"), password.encode("utf-8"), digestmod="SHA256").hexdigest()
        if input_password == user_password:
            return True, "登录成功"
        else:
            return False, "密码错误"


if __name__ == "__main__":
    new_user = User()
    new_user.register("yan", "123")
    print(new_user.register("yan", "123"))
