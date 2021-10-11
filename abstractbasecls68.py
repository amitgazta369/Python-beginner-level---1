from abc import ABC, abstractmethod     #abstractmethod is a decorator we can use ABC i place of ABCMeta
class Shape(ABC):

    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 50
        self.breadth = 6

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())