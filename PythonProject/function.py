#方法
def say_hello():
    print("hi!  hello world")

say_hello()

#傳遞參數
def greeting(name):
    print(f"Hello ,{name} !")

greeting("Mary")

#add

def add(a,b):
    return a+b


resultA = add(1,2)
print(resultA)

#subtract
def subtract(a,b):
    return a-b
resultS = subtract(1,2)
print(resultS)

#multiply

def multiply(a,b):
    return a*b
resultM = multiply(1,2)
print(resultM)

#divide
def divide(a,b):
    return a/b
resultD = divide(1,2)
print(resultD)


def create_name(first_name,last_name):
    first=first_name.capitalize()
    last=last_name.capitalize()
    return first+" "+ last
print(create_name("mary","smith"))


