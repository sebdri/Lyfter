'''Model'''

from datetime import datetime

# --- Constantes ---
DATE_FORMAT = "%d/%m/%Y"
INCOME = 'Ingreso'
EXPENSE = 'Gasto'


class Category:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {'Name': self.name}

    @classmethod
    def from_dict(cls, data):
        return cls(data["Name"])

    def __str__(self):
        return self.name


class Movement:
    def __init__(self, title, amount, category, m_type, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.m_type = m_type
        self.date = date

    def to_dict(self):
        return {
            'Title': self.title,
            'Amount': self.amount,
            'Category': self.category,
            'Type': self.m_type,
            'Date': self.date.strftime(DATE_FORMAT),
        }

    @classmethod
    def from_dict(cls, data):
        movement_date = datetime.strptime(data["Date"], DATE_FORMAT).date()
        return cls(data["Title"], data["Amount"], data["Category"], data["Type"], movement_date)

    def __str__(self):
        return f'{self.title} | {self.amount} | {self.category} | {self.m_type} | {self.date}'
