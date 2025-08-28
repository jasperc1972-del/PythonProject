#物件導向

#object/class/instance
#物件是類別的實例

#車有四個輪子
#車子是類別
# 每一台生產出來的車子是物件

class Car:
    def __init__(self,make,model,year,color):
        #初始化
        self.make=make
        self.model=model
        self.year=year
        self.color=color

car1=Car("toyota","ALtis",2021,"藍色")
car2=Car("ford","kuga",2020,"白色")
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

print(car2.make)
