list_of_keys = ['access_level', 'age', 'status']

employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28,
    'status': 'alone',
}

for key in list_of_keys:
    employee.pop(key)

print(employee)