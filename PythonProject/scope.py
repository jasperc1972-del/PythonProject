# python的作用域
# 變數範圍與作用域
# LEGB作用域順序
from inspect import GEN_CLOSED

# L-local 區域
# E-enclosed
# G-globals
# B-built-in

#變數範圍
a=10
def function1():
    a=1
    print("a:",a)

    def function2():
        b=2
        print("b:",b)
        print("a:",a)

    function2()
function1()
