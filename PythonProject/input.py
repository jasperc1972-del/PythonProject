# input 取得使用者輸入
from operator import itemgetter

#practice 1 fill word game

# name=input("please input your name:")
# print(f" your name is {name}")



# adj1=input("請輸入第一個形容詞:")
# noun1=input("請輸入第一個名詞:")
#
# verb1=input("請輸入第一個動詞:")
# adj2=input("請輸入第二個形容詞:")
# adj3=input("請輸入第三個形容詞:")

#print(f"今天我去了一個{adj1},在展覽中我看到了{noun1}這個{noun1}很{adj2},正在{verb1}我感到很{adj3}")


#practice 2 calculate square area
# lenth=float(input("請輸入矩形的長度-"))
# width=float(input("請輸入矩形的寬度-"))
#
# area=lenth*width
# print(f"面積為{area}平方公尺")

#practice 3 shopping car program

item=input("你想購買什麼物品:")
price=float(input("價格多少?"))
quantity=int(input("你需要幾件?"))

total=price*quantity
print(f"你購買了{item}{quantity}個,總價為{total}")