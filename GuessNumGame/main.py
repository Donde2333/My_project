# -*- coding:utf-8 -*-

from my_package import *
import os

user_system = User()
Rank_system = RankingManager()


def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_header(title):
    """显示带标题的头部"""
    clear_screen()
    print(f"\n=== {title} ===")
    print("=" * 30)


def type_to_retune():
    """按回车返回"""
    input("按回车返回……")


def register_flow():
    """用户注册流程"""
    while True:
        show_header("用户注册")
        username = input("请输入用户名 (输入q返回主菜单): ")
        if username.lower() == 'q':
            return False

        password = input("请输入密码: ")

        success, message = user_system.register(username, password)

        if success:
            print(f"\n{message}")
            return username  # 返回注册成功的用户名
        else:
            print(f"\n注册失败: {message}")
            retry = input("是否重试? (Y/N): ")
            if retry.lower() != 'y':
                return False


def login_flow():
    """用户登录流程"""
    attempts = 3  # 最多尝试3次
    while attempts > 0:
        show_header("用户登录")
        username = input("请输入用户名 (输入q返回主菜单): ")
        if username.lower() == 'q':
            return None

        password = input("请输入密码: ")

        success, message = user_system.login(username, password)

        if success:
            print(f"\n{message}")
            type_to_retune()
            return username  # 返回登录成功的用户名
        else:
            attempts -= 1
            print(f"\n登录失败: {message}")
            if attempts > 0:
                print(f"您还有{attempts}次尝试机会")
            type_to_retune()
    print("\n登录失败次数过多，返回主菜单")
    type_to_retune()
    return None


def main_menu():
    """主菜单"""
    current_user = None  # 当前登录用户

    while True:
        show_header("Python游戏")

        if current_user:
            print(f"当前用户: {current_user}")

        print("1. 用户注册")
        print("2. 用户登录")
        print("3. 开始游戏-猜数字")
        print("4. 排行榜")
        print("5. 退出系统")
        print("6. 切换用户")
        print("=" * 30)

        choice = input("请选择操作: ")

        if choice == "1":  # 注册
            new_user = register_flow()
            if new_user:
                current_user = new_user  # 注册成功并自动登录

        elif choice == "2":  # 登录
            logged_user = login_flow()
            if logged_user:
                current_user = logged_user

        elif choice == "3":  # 开始游戏
            if not current_user:
                print("请先登录!")
                type_to_retune()
            else:
                print("进入游戏中...")
                result_name, result_scores = guess_number_game(current_user)
                Rank_system.add_record(result_name, result_scores)
                type_to_retune()

        elif choice == "4":  # 排行榜
            show_header("排行榜")
            # 显示排行榜逻辑
            type_to_retune()

        elif choice == "5":  # 退出
            type_to_retune()
            break

        elif choice == "6":  # 切换用户
            current_user = None
            print("已退出当前用户")
            type_to_retune()

        else:
            print("无效选择，请重新输入")
            type_to_retune()


if __name__ == "__main__":
    main_menu()
