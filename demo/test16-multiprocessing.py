# -- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os
import time
import random


def write(my_queue):  # 写数据进程执行
    print(f"写入进程[{os.getpid()}]工作中……")
    for value in ["A", "B", "C"]:
        print(f"put[{value}]to queue.")
        my_queue.put(value)
        time.sleep(random.random())


def read(my_queue):  # 读数据进程执行
    print(f"读取进程[{os.getpid()}]工作中……")
    while True:
        value = my_queue.get(True)
        print(f"get[{value} from queue.]")


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    print("主进程结束")
