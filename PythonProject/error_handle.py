#python 中例外處理(error handleing,異常處理)

# exception

#10/0
try:
    x=int(input("enter first integer number:"))
    y=int(input("enter second integer number:"))

    print(x/y)
# except ValueError:
#     print("value error please key in interger")
# except ZeroDivisionError:
#     print("division by zero")
except(ZeroDivisionError,ValueError):
    print("error ,please try again")
finally:

    print("Will be executed regardless of whether an exception occurs")






