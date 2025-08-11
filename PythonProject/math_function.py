#python 數學
import math
#四捨五入,無條件進入,無條件捨去
x=9.5
print(round(9.5))
print(math.ceil(9.5))
print(math.floor(9.5))


#圓週率
print(math.pi)
print(math.ceil(math.pi))
print(math.floor(math.pi))




#圓的 周長= 2πR
radius=float(input("請輸入圓的半徑:"))
perimeter=2*math.pi*radius
print("圓的周長:",round(perimeter,2))

#圓的 面積=πR2
radius=float(input("請輸入圓的半徑:"))
area=math.pi*(radius**2)
print("圓的面積:",round(area,2))
