# f_string 字串格式化

price1=3.5471
price2=-5.74132
price3=4.78995

#小數點精確度+-號
# print(f"價格1: {price1 :+.2f}\n"
#        f"價格2: {price2:+.2f} \n"
#        f"價格3: {price3 :+.2f} ")

#對齊<>^

# print(f"價格1: {price1:>10.2f}\n"
#         f"價格2: {price2:>10.2f} \n"
#         f"價格3: {price3:>10.2f} ")

# 混合不同符號

print(f"價格1: {price1:>+.2f}\n"
        f"價格2: {price2:>+.2f} \n"
        f"價格3: {price3:>+.2f} ")