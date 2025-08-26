#python 檔案偵測

import os

str1=r"C:\Users\Jasper\Desktop\workspace"
print(str1)
if os.path.exists(str1):
    print("path exists")
else:
    print("path does not exist")

