# -*- coding:utf-8 -*-

import random


def guess_number_game(current_user):
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    username = current_user

    while attempts < max_attempts:
        try:
            guess = int(input("请输入你猜的数字（1-100）："))
        except ValueError:
            print("请输入一个有效的整数！")
            continue

        attempts += 1
        if guess < secret:
            print("太小了！")
        elif guess > secret:
            print("太大了！")
        else:
            print(f"恭喜你，第 {attempts} 次猜对了！")
            return username, attempts
    else:
        print(f"很遗憾，正确答案是 {secret}")
        return 0, 0


if __name__ == "__main__":
    guess_number_game()
