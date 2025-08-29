# method overriding

class Animal:
    def eat(self):
        print('動物正在吃東西')
#哺乳類

class Mammel(Animal):
  def hi(self):
      print("我是哺乳類")
#貓
class Cat(Mammel):
  def eat(self):
      print("小貓正在吃魚")
#狗
class Dog(Mammel):
  def eat(self):
      print("小狗正在啃骨頭")

cat = Cat()
cat.eat()
dog = Dog()
dog.eat()

m=Mammel()
m.eat()




