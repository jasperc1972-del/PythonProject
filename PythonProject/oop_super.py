# super method



class Rectangle:
      def __init__(self,length,width):
        self.length=length
        self.width=width
        print("矩形初始化")
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
        print("正方形初始化")


#square=Square(10,10)


# w*h*l
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height
        print(f"立方體的長寬高是{length},{width},{height}")


cube=Cube(60,10,70)


