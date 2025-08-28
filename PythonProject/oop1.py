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
    #定義方法
    def drive(self):
        print(self.model+"正在行駛")
    def stop(self):
        print(self.model+"煞車")

car1=Car("toyota","ALtis",2021,"藍色")
car2=Car("ford","kuga",2020,"白色")

#呼叫方法
car1.drive()
car2.drive()
car1.stop()
car2.stop()

