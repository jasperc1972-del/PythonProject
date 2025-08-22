import random
help(random)

#randint() 一到十間的亂數
print(random.randint(1,10))

#random() 0到1間浮點數
print(random.random())

#列表中隨機選擇1個元素
options=["剪刀","石頭","布"]
rand_option=random.choice(options)
print("電腦選擇是:",rand_option)

#將一個列表打亂
cards=["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
random.shuffle(cards)
print(cards)


