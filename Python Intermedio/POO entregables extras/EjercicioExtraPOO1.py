class Rectangule:

    def __init__(self, width, height):

        if width <0 or height<0:
            raise ValueError ("Width and Height cannot be negative values")

        self.width = width
        self.height = height


    def get_area(self):
        return self.width* self.height


    def get_perimeter(self):
        return 2*(self.width* self.height)

try:
    width = float(input("Enter the rectangle width: "))
    height = float(input("Enter the rectangle height: "))

    rectangle = Rectangule(width,height)

    print("Area:", rectangle.get_area())
    print("Perimeter:", rectangle.get_perimeter())

except ValueError as error:
    print(error)


