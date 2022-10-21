h = float(input("请输入你的身高，单位为米:"))
w = float(input("请输入你的体重，单位为千克:"))
BMI = w / (h * h)
if BMI < 20:
    print("过轻")
elif BMI < 25:
    print("适中")
elif BMI < 30:
    print("过重")
else:
    print("肥胖")
