# python 數學


#加減乘除

GUAVAS=3
GUAVAS+=1
print(GUAVAS)
GUAVAS=GUAVAS+1
#GUAVAS+=1 相等 GUAVAS=GUAVAS+1
print(GUAVAS)
print("以上加法----------------------------")

GUAVAS=GUAVAS-1
print(GUAVAS)

GUAVAS-=1
print(GUAVAS)
print("以上減法----------------------------")

GUAVAS=GUAVAS*3
print(GUAVAS)

GUAVAS*=4
print(GUAVAS)
print("以上乘法----------------------------")


GUAVAS=GUAVAS/3
print(GUAVAS)

GUAVAS/=4
print(GUAVAS)
print("以上除法----------------------------")

#指數(平方,三次方)
tomato=3
tomato=tomato**2
print(tomato)
tomato **=2
print(tomato)

print("tomato以上指數----------------------------")





#模數

#10 mod 3 等於3餘1
print(10 % 3)

#11 mod 3 等於3餘2
print(11 % 3)
#12 mod 3 等於4餘0

print(12 % 3)

#內置數學函數

#次方 pow
print(pow(0,3))
print(pow(1,5))
print(pow(2,5))

#最大值 Max  最小值 Min

x=2
y=3
z=6

print(max(x,y,z))
print(min(x,y,z))

#四捨五入 round

a=3.14
print("四捨五入",round(a))

k=5.6
print("四捨五入",round(k))

#絕對值

w=-6.6
print("絕對值",abs(w))