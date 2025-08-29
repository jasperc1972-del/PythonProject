#python method chaining 方法鍊

#car,turn_on(),drive(),brake(),turn_off()

class Car:
    def turn_on(self):
        print("啟動引擎")
#回傳物件本身
        return self
    def drive(self):
        print("行駛中")
        return self
    def brake(self):
        print("啟動煞車")
        return self
    def turn_off(self):
        print("關閉引擎")
        return self
#建立物件
car = Car()
car.turn_on().drive().brake().turn_off()
