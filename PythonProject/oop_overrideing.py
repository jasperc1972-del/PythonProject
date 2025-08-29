# method overrideing

class Animal:
    def eat(self):
        print('動物正在吃東西')

class Rabbit(Animal):
    #pass
    def eat(self):
        print('兔子在吃紅蘿蔔')
animal = Animal()
animal.eat()
rabbit = Rabbit()
rabbit.eat()
