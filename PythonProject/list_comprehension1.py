#python 列表推導式  (list  comprehension)

# 列表推導式 =>以更少語法創建新列表

# lambda


#成績超過60的列印出來
grades=[100,90,80,87,50,60]
pass_grades=[g for g in grades if g>=60]
print(pass_grades)
