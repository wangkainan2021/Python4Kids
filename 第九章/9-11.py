def f(n):
    if (n == 0):
        return 1
    else:
        return f(n-1) * n

#调用阶乘函数，打印1到5的阶乘
for i in range(1, 6):
    print(f(i))
