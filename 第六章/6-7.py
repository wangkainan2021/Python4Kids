n = eval(input("请输入要打印的行数："))
for i in range(n):
    for j in range(i + 1):
        print("*", end = " ")
    print("")

