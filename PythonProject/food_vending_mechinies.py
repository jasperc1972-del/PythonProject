

menu={
    "披薩":199,
    "爆米花":50,
    "薯條":90,
    "洋芋片":50,
    "軟麵包條":120,
    "蘇打水":40,
    "檸檬水":40

}
print("菜單")
print("----------------")
cart=[]
total=int()
for item,price in menu.items():
   print(f"{item},{price}")


while True:
    food=input("請輸入一個菜單項目(q表離開此菜單)")
    if food == "q":
        break
    elif menu.get(food) is None:
        print("沒有這商品")
    else:
        cart.append(food)
        total += menu.get(food)
        print(food,end=" ")
print(f"總共:{total}元")

