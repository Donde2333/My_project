# -- coding: utf-8 -*-
import os


def find_files(search_string):
    """
    在当前目录和所有子目录中查找文件名包含指定字符串的文件
    :param search_string: 要查找的字符串
    """
    # 获取当前工作目录的绝对路径，作为参考点
    base_dir = os.path.abspath('.')

    # 遍历所有目录和子目录
    for root, dirs, files in os.walk('.'):
        for filename in files:
            # 检查文件名是否包含搜索字符串
            if search_string in filename:
                # 构建文件的完整绝对路径
                abs_path = os.path.join(base_dir, root, filename)
                # 转换为相对于当前目录的路径
                rel_path = os.path.relpath(abs_path, base_dir)
                # 在Windows上可能需要规范化路径分隔符
                if os.sep == '\\':
                    rel_path = rel_path.replace('\\', '/')
                print(rel_path)


if __name__ == "__main__":
    search_str = input("请输入要查找的字符串: ")
    print(f"正在查找包含 '{search_str}' 的文件...")
    find_files(search_str)
