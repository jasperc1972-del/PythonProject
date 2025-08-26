
str4=r"C:\Users\Jasper\Desktop\workspace\test.txt"
try:
    with open(str4) as f:
     print(f.read())
except FileNotFoundError:
    print("file not found")

