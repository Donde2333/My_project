# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time
import functools


def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 调用原函数
        end_time = time.time()  # 记录结束时间
        print(f"执行时间: {end_time - start_time:.4f}秒")  # 打印执行时间
        return result  # 返回原函数的结果
    return wrapper


@time_decorator
def example_function(n):
    """一个示例函数,计算从1到n的和"""
    total = sum(range(1, n + 1))
    return total


# 测试装饰器
result = example_function(1000000)  # 输出结果
print(f"计算结果: {result}")  # 打印计算结果
print(example_function.__name__)
