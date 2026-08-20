from abc import ABC, abstractmethod



class Shape(ABC):


    @abstractmethod
    def calculate_perimeter(self):
            pass



    @abstractmethod
    def calculate_area(self):
        pass




class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_perimeter(self):
        Cperimeter =  2*3.13* self.radius
        return Cperimeter

    def calculate_area(self):
        Carea = 3.13 * self.radius ** 2
        return Carea





class Square(Shape):
    def __init__(self,side):
        self.side = side


    def calculate_perimeter(self):
        Sperimeter = 4 * self.side
        return Sperimeter

    def calculate_area(self):
        Sarea = self.side**2
        return Sarea


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self):
        Pperimeter = 2*(self.width+self.height) 
        return Pperimeter

    def calculate_area(self):
        Rarea = self.width * self.height
        return Rarea
