#第一步 先将同学们的身高都读入到系统中
ls = []
#用num表示班级共有多少位同学
num = int(input("请老师输入班级里同学的数量："))
for i in range(num):
	#float()将input()读入的字符串转换为浮点型数值
    tmp = float(input("清测量完的同学输入自己的身高(单位cm)："))
    ls.append(tmp)

#第二步 累计全班同学的身高总和
s = 0
for i in ls:
    s = s + i

#第三步 计算全班同学的平均身高
avg = s / num
print(avg)
