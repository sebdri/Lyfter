import datetime


def only_age(func):
    def wrapper(user):
        if user<18:
            raise ValueError("User must be grater than 18 years old")
        else:
            return func(User)
    return wrapper

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @only_age
    def age(self):
        age = datetime.date.today() - self.date_of_birth
        days = age.days //362
        return days
            

user1 = User(datetime.date(2000, 5, 20))
print(user1.age)