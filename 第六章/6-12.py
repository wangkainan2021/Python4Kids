x = int(input("请你输入一个数字:"))
flag = 1 #flag变量做标记使用，值为1表示可以先认为x是质数
for i in range(2, x):
    if x % i == 0:
        flag = 0  #如果x被i整除，那么将标记的置为0，表示x是合数
        break      #出现了一个因数就不需要再往后判断了
if flag == 1:   #出了循环依据标记的值进行输出
    print("{}是一个质数".format(x))
else :
    print("{}是一个合数".format(x))

