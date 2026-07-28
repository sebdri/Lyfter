#    ------------<CAMBIOS SOLICITADOS>------------


class Circle: 
    

    def __init__(self, radius):
        self.radius = radius

        
    def get_area(self):
        area =  3.1416 *self.radius*self.radius     
        return area

circle = Circle(5)
print(circle.get_area())