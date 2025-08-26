#python 中例外處理(error handleing,異常處理)

# exception

#10/0
try:
    x=int(input("enter first integer number:"))
    y=int(input("enter second integer number:"))

    print(x/y)

except(ZeroDivisionError,ValueError):
    print("error ,please try again")
else:
    print("error ,please try again")
finally:
    print("else")
# finally:
#
#     print("Will be executed regardless of whether an exception occurs")






