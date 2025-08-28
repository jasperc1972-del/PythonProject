#類別變數

class Car:
    wheels=4
    def __init__(self,color,mileage):
        self.color=color
    #物件變數
    def __init__(self,make,model,year,color):
        #初始化
        self.make=make
        self.year=year
        self.color=color
        self.model=model

car1=Car("ford","focus",2023,"white")
# print(car1.make)
# print(car1.model)
# print(car1.year)
# print(car1.color)

# print(car1.wheels)

#機車
car2=Car("三陽","勁戰",2020,"black")
print(car2.model)
car2.wheels=2
print(car2.wheels)


