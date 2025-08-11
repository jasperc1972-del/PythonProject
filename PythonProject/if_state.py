# if else elif 控制流程


#boolean
appleOnSale=False
if appleOnSale:
    print('apple is on sale')
else:
    print('apple do not on sale')


#if else

# age=int(input("please enter your age:"))
# if age>=18:
#     print('you can register')
# else:
#     print('Only individuals who are 18 years old or older can register')


#elif=> else if 縮寫
age=int(input("please enter your age:"))
if age>=100:
    print('you are older than 100,can not register')
elif age<=18:
    print('you can not register')
elif age<=0:
    print('unborn')
else:
    print('You are already over 18 years old, so you can register')



# practice