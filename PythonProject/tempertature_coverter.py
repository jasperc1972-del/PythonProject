# python 溫度轉換器

unit=input("請輸入當前的溫度單位(攝氏C,華氏F):  ")
temp=float(input("請輸入當前的溫度 :"))
print(f"目前溫度是{temp}{unit}")
if unit == "C":
    temp=round(9*temp/5+32)
    print(f"轉換華氏溫度為: {temp} F度")
elif unit == "F":
    temp=round((temp-32)*5/9)
    print(f"轉換攝氏溫度為: {temp} C度")
else:
    print("無效溫度單位")
