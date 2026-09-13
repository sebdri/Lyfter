import datetime


def only_valid_age(func):
    def wrapper(*args, **kwargs):
        for element in args:
            if not isinstance(element, User):
                continue
            if element.age < 18:
                raise ValueError("User must be greater than 18 years old")
        return func(*args, **kwargs)
    return wrapper


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = datetime.date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years


@only_valid_age
def person(user):
    print(f'You have {user.age} years old')


user1 = User(datetime.date(2000, 9, 16))
person(user1)