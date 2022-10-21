print("---性格大测试---")
total = 0
res_1 = "你幽默得体不失庄重，阳光自信又活泼好动。控制你的脾气，爱你身边的人，你的人生将一帆风顺balabala"
res_2 = "你妙的无法描述，正如这神奇的Pyhon语言"
res_3 = "你...哦编不下去了，你健康的活下去吧"

print("1.你更喜欢的电影演员是？\nA.姜文 B.葛优")
answer = input("::")
if answer == 'A':
    total += 1
elif answer ==  'B':
    total += 2

print("2.你更喜欢的冰激凌口味是？\nA.草莓 B.巧克力")
answer = input("::")
if answer == 'A':
    total += 1
elif answer ==  'B':
    total += 2

print("3.你更喜欢的运动是？\nA.足球 B.篮球")
answer = input("::")
if answer == 'A':
    total += 1
elif answer ==  'B':
    total += 2

if total >= 5:
    print(res_1)

elif total >= 4:
    print(res_2)

else:
    print(res_3)
