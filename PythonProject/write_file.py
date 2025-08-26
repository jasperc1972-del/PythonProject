

str5=r"C:\Users\Jasper\Desktop\workspace\test3.txt"

#text="Hi\n祝你生日快樂"
text="\n切蛋糕!"
#write
# w 覆寫 a 新增到最後面
with open(str5,'a') as f:
    f.write(text)