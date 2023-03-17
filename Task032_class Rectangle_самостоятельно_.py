class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def out (self):
        print(self.width," ",self.height," ")
    def changeheight (self, newheight):
        self.height=newheight
obj1 = Rectangle(55,68)
obj1.out()
obj1.changeheight(100)
obj1.out()