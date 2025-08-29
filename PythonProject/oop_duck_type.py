# duck typing

# 如果他走路像鴨子,聲音像鴨子,那它就是一隻鴨子

class Duck:
    def walk(self):
        print("Duck walking")
    def talk(self):
        print("Duck quak")

class Chicken:
    def walk(self):
        print("Chicken walking")
    def talk(self):
        print("Chicken clucking")

#雞鴨不是同一個類別,也沒有繼承的關係但是可以當作同一個類型的類別使用

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
#duck = Duck()
chicken = Chicken()
person = Person()
person.catch(chicken)

#你有同樣的行為可以視為同一類的物件來操作
