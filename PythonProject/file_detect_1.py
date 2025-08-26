import os

str3=r"C:\Users\Jasper\Desktop\workspace\2.txt"
print(str3)
if os.path.isfile(str3):
    print("is file")
elif os.path.isdir(str3):
    print("is directory")
else:
    print("other")






