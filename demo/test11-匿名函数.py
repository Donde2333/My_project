# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))

# print(L)


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)


def log(func):  # --------装饰器
    def wrapper(*args, **kw):
        print(f"call {func.__name__}():")
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2024-6-1')


now()


def api_handler(path, *args, **query_params):  # *args 和 **kw的使用
    print(f"访问路径: {path}")
    print(f"路径参数: {args}")
    print(f"查询参数: {query_params}")


api_handler("/users", "123", "profile", limit=10, detailed=True)
