#读入一个三位数
a = eval(input("请输入一个三位数："))

#拆分出三位数的个十百位，并保存在变量ge、shi、bai中
ge = a % 10
shi = a // 10 % 10
bai = a // 100

#输出的时候，先输出个位，再输出十位，百位即可。
print(ge, shi, bai, sep = "")
