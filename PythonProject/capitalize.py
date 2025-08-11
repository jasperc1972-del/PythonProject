#upper() lower() count() replace()

#help(str)

#使用者的全名
name="apple code"
print(name)

#幾個字元

length=len(name)
print("你的名字共有",length,"字元")

#找到第一個空格
space_pos=name.find(" ")
print("第一個空格出現在第",space_pos,"字元")

#你的全名第一個字母大寫
capitalize=name.capitalize()
print("你的全名第一個字母大寫",capitalize)

#upper()字母全大寫
name_upper=name.upper()
print(name_upper)

#lower()字母全大寫
name_lower=name.lower()
print(name_lower)

#count

# phone_number=input("輸入你的電話號碼:")
# dash_count=phone_number.count("_")
# print("你的電話號碼中總共有",dash_count,"個短橫線")

#replace()
# phone_number=phone_number.replace("_"," ")
# print("你的電話號碼-短橫線換成空格 ",phone_number)

#你的使用者名稱不能超過12個字元
# 你的使用名稱不可以包含空格
# 你的使用名稱不能包含數字
# 如果都符合的話,歡迎顯示+使用者名稱

usename=input("請輸入使用者名稱:")
if usename.isalpha():
    print("全部是英文")
else:
    print("包含其他字元")
# if len(usename)>12:
#     print("你的使用者名稱不能超過12個字元")
# elif " " in usename:
#     print("你的使用名稱不可以包含空格")
#
# else:
#     print("歡迎 "+usename)


