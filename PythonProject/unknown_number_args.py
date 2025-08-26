# args=>arguments 任意數量參數 * =>tuple
# kwarg=> 關鍵字+args(keyword args)  **=>dictionary

# args

# def add(a, b):
#     return a + b
# print(add(1, 2))

def add(*args):
    total = 0
    for arg in args:
        print(f"args:{arg}")
        total += arg
    return total

print(add(1,2,3))

print(add(1,2,3,4))
print(add(1,2,3,4,5))



# kwarg=> 關鍵字+args(keyword args)  **=>dictionary

def print_info(**kwargs):
   for key,value in kwargs.items():
       print(f"key: {key}, value: {value}")
print_info(name="kelly",age="30",occupation="MIS")