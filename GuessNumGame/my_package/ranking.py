# -*- coding:utf-8 -*-
import csv
import os
from datetime import datetime


class RankingManager():
    def __init__(self, path="GuessNumGame/data/scores.csv"):
        self.__path = path

        # 首次使用时创建带标题的文件
        if not os.path.exists(self.__path):
            with open(self.__path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["姓名", "尝试次数", "记录时间"])

    def _print_list(self, ranklist):
        """格式化输出结果"""
        # print("排行榜前10名：")
        print("-" * 40)
        print(f"{'排名':<3}{'姓名':<6}{'尝试次数':<10}{'记录时间'}")
        print("-" * 40)

        for i, (name, score, time) in enumerate(ranklist[:10], 1):
            print(f"{i:<5}{name:<10}{score:<10}{time}")

    def add_record(self, name, score):
        """添加一条记录"""
        record_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.__path, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, score, record_time])

    def get_ranklist(self):
        """获取排序后的排行榜"""
        records = []

        if os.path.exists(self.__path):
            with open(self.__path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # 跳过标题行

                for row in reader:
                    # 确保行数据格式正确
                    if len(row) >= 3:
                        try:
                            records.append((row[0], float(row[1]), row[2]))
                        except ValueError:
                            continue
        # 按分数降序排序
        return self._print_list(sorted(records, key=lambda x: x[1]))


if __name__ == "__main__":
    # 创建管理器
    manager = RankingManager()

    # 添加多条记录
    manager.add_record("yan", 3)
    manager.add_record("li", 4)
    manager.add_record("wang", 5)
    manager.add_record("zhao", 6)

    # 只调用一次获取全部排行数据
    ranklist = manager.get_ranklist()
