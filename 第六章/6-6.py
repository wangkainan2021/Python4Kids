n = eval(input("请输入要打印的行数："))
m = eval(input("请输入要打印的行数："))
for i in range(n):
    for j in range(m):
        print("*", end = " ")  #注意这里要改一下结束字符，默认是换行，格式会乱
    print("") #这里实际上是输出了换行

