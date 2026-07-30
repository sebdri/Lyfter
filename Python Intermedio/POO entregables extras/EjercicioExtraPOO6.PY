import datetime

class Car:
    def __init__(self, brand , model, year):
        if year <= 1885:
            raise ValueError ("This is not a valid year")

        self.brand = brand
        self.model = model
        self.year = year

    def car_information(self):
        return f'Brand: {self.brand}\n Model: {self.model}\n Year: {self.year}'

    def is_classic(self):
            current_year = datetime.datetime.now().year
            age = current_year - self.year

            if age>25:
                return "This car is classic"
            else:
                return "This is not a classic car"




#   ----<PARTE INTERACTIVA>----

while True:
    try:
        brand = input("Enter the brand of your car: ")
        model = input("Enter the model of the car: ")
        year = int(input("Enter the year of your car: "))

        car = Car(brand,model,year)
        break

    except ValueError as error:
        print(error)


print("\n===== CAR INFORMATION =====")
print(car.car_information())
print(car.is_classic())