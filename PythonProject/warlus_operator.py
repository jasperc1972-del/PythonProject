#python warlus operator  :=

# 獠牙運算符
# 獠牙運算符
# 賦值表達式 :=
# 賦值運算子  =

# python 3.8 version才有的

# happy=True
# print(happy)

print(happy := True)

#print(happy=True) # ng寫法不會傳回值

# foods=[]
# while True:
#     food=input("enter your favorite food ?")
#     if food=="quit":
#         break
#     foods.append(food)
#
# print(foods)


# foods=[]
# while food := input("enter your favorite food ?"):
#     if food=="quit":
#         break
#     foods.append(food)
#
# print(foods)



foods=[]
while (food := input("enter your favorite food ?"))!="quit":

    # if food=="quit":
    #     break
    foods.append(food)

print(foods)
