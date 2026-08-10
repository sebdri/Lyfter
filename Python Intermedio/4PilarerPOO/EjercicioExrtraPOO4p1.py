class Employee:

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")

        self._salary = new_salary


#                 {Crear empleado}


while True:
    try:
        name = str(input("Enter employee name: "))
        break
    except ValueError:
        print("Invalid input")


while True:
    try:
        salary = float(input("Enter employee salary: "))
        break
    except ValueError:
        print("Invalid input")

employee = Employee(name, salary)

print("\nEmployee created!")
print("Name:", employee._name)
print("Salary:", employee.salary)


# Cambiar salario
new_salary = float(input("\nEnter new salary: "))

employee.salary = new_salary

print("\nUpdated salary:", employee.salary)