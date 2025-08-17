#複利計算機
# 總金額=本金*(1+(利率/100))**時間

# 10000*1.05*1.05
# 10000*1.05**2
# 總金額10000*(1+5/100)**2

amount=0
time=0
rate=0

while amount <= 0:
    amount = float(input("請輸入本金的金額: "))
    if amount <= 0:
        print("輸入本金的金額不能小於等於0.")

while rate <= 0:
    rate=float(input("請輸入利率:"))
    if rate <= 0:
        print("輸入利率的金額不能小於等於0.")

while time <= 0:
    time=int(input("請輸入年限:"))
    if time <= 0:
        print("輸入年限不能小於等於0.")


print("金額:", amount)
print("利率:",rate)
print("年限:",time)

# 總金額10000*(1+5/100)**2
Total =amount*(1+rate/100)**time
print("總金額:",Total)
