from ctypes import HRESULT

operator=input('please enter your operator: +,-,*,/ ')
n1=float(input('please enter first number: '))
n2=float(input('please enter second number: '))

if operator=='+':
    result=n1+n2
elif operator=='-':
    result=n1-n2
elif operator=='*':
    result=n1*n2
elif operator=='/':
    result=n1/n2
else:
    result = "invalid operator"

print(f"the answer is:",(result))