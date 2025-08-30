#python 列表推導式  (list  comprehension)

# 列表推導式 =>以更少語法創建新列表

# lambda

# square

def suare(x):
    return x*x
list=[]
for i in range(1,11):
    list.append(suare(i))
print(list)


suares=[i*i for i in range(1,11)]
print("列表推導式")
print(suares)