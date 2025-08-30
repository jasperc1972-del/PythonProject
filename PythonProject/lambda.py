#python lambda

# lambda有函式的功能一行就可以寫完

# double
#ex1
# def double(x):
#     return x * 2
# print(double(3))
# print(double(4))
#
# double2=lambda x:x*2
# print(double2(3))

#ex2

# multiply=lambda x,y:x*y
# print(multiply(5,2))

#ex3  if else 條件語句

result=lambda x:f"{x}是偶數" if x%2==0 else f"{x}是奇數"
print(result(0))

#ex4  處裡字串
full_name=lambda first_name,last_name:f"{first_name} {last_name}"
print(full_name("lamis","chou"))


