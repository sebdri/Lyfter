import datetime


def only_age(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, User):
                continue  #salta de valor al sigiente por ser validado 
            

            if i.age<18:
                raise ValueError("User must be greater than 18 years old")
        return func(*args,**kwargs)
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