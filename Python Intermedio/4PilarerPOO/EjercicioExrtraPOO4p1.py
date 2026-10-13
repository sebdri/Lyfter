class Employee:
    def __init__(self, _name, _salary):
        self._name = _name
        self._salary = _salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self , new_salary):
        if new_salary<0:
            raise ValueError('Salary must be grater than 0')

        self._salary = new_salary

    def promote(self, promote):
        self._salary = self._salary*(1+promote)



name = input('Enter your name: ')

while True:
    try:
        salary = float(input('Enter your current salary: '))
        break

    except ValueError:
        print('Invalid data')

employee = Employee(name, salary)

print(f'Hi, dear {employee.name}, is a pleasure to have you here: ')
print('Your current salary is: ', employee.salary)


promotion = float(input('Enter your promotion percentaje:'))

promotion = promotion / 100

employee.promote(promotion)

print(f'Your new salary is: {employee.salary}')

