import time

# my_time=int(input("please enter the time(seconds):"))
# for i in range(my_time):
#     print(i)
#     time.sleep(1)
# print("time is up !")


#倒計時
my_time=int(input("please enter the time(seconds):"))
for i in range(my_time,0,-1):
   # 02:00
   seconds=i%60
   minutes=i//60%60 #/是float //維持整數
   print(f"{minutes:02}:{seconds:02}") #補0,2顯示2位數
   time.sleep(1)
print("time is up !")