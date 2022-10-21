import random
gift = random.randint(1, 1000)
count = 1
guess = eval(input("输入你猜的价格, 小提示价格在1到1000之间:"))
while gift != guess:
    if gift > guess:
        print("猜少了")
        guess = eval(input("再猜:"))
        count += 1
    if gift < guess:
        print("猜多了")
        guess = eval(input("再猜:"))
        count += 1
print("呼~终于猜对了，一共猜了{}次".format(count))

