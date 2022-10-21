while gift != guess:
    if gift > guess:
        print("猜少了")
        guess = eval(input("再猜:"))
    if gift < guess:
        print("猜多了")
        guess = eval(input("再猜:"))
print("呼~终于猜对了")

