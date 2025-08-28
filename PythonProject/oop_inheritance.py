#繼承

#父類別 <-> 子類別

#動物
class Animal:
    alive=True
    def eat(self):
        print("這個動物正在吃東西")
    def sleep(self):
        print("這個動物正在睡覺")

#魚
class Fish(Animal):
    def swim(self):
        print("魚正在遊泳")

#兔子
class Rabbit(Animal):
    def jump(self):
        print("這隻兔子正在跳")
# animal=Animal()
# animal.eat()
# animal.sleep()

# rabbit=Rabbit()
# rabbit.jump()
# rabbit.eat()

#老鷹

class Eagle(Animal):
    def fly(self):
        print("老鷹正在飛")



# fish=Fish()
# fish.swim()
# fish.eat()
# fish.sleep()

eagle=Eagle()

eagle.fly()
eagle.eat()
eagle.sleep()

