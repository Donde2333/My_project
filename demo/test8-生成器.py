# ------------------------
# l1 = ['Hello', 'World', 18, 'Apple', None]
# l2 = [s.lower() for s in l1 if isinstance(s, str)]
# l3 = [s1.lower() if isinstance(s1, str) else str(s1) for s1 in l1]

# print(l2)
# print(l3)

# g = (g1.lower() for g1 in l1 if isinstance(g1, str))
# print(g)
# for n in g:
#     print(n)

# -----------------------
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# f = fib(6)
# for f1 in f:
#     print(f1)

# 生成器生成杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


# 打印杨辉三角的前10行
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
