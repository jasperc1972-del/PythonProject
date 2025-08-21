# list ,set,tuple
# shopping cart

goods=[] #list
prices=[]
#infinite loop
while True:

    good=input("請輸入想購買的物品:")
    if good.lower()=="q":
        break
    price=float(input(f"請輸入{good}的價格:"))
    goods.append(good)
    prices.append(price)

print("物品:" ,goods)
print("價格:" ,prices)

#enumerate

for index,good in enumerate(goods):
    # print("索引:",index)
    # print("物品名稱:",good)
    print(f"第{index+1}商品是{good},價格是:{prices[index]:.2f}")
total=sum(prices)
print(f"總價:${total}元")




