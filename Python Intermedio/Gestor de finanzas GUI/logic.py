'''---Logic---'''

from datetime import date
from model import Category, Movement, INCOME, EXPENSE


class FinanceManager:
    def __init__(self):
        self.categories = []
        self.movements = []

    def add_category(self, name):
        name = name.strip()
        if name == '':
            raise ValueError('El nombre no puede estar vacío')

        for category in self.categories:
            if category.name.strip().lower() == name.lower():
                raise ValueError('La categoría ya existe')
        self.categories.append(Category(name))

    def add_movement(self, title, amount, category, m_type):
        if not self.categories:
            raise ValueError('No hay categorías. Agregue una primero')

        # Regla para title
        if title.strip() == '':
            raise ValueError('El título no puede estar vacío')

        # Regla para m_type
        if m_type not in (INCOME, EXPENSE):
            raise ValueError('El tipo debe ser Ingreso o Gasto')

        # Regla para amount
        try:
            number = float(amount)
        except ValueError:
            raise ValueError('El monto debe ser un número. Intente de nuevo')

        if number <= 0:
            raise ValueError('El monto debe ser mayor que cero')

        # Regla para category
        found = False
        official_name = category
        for data in self.categories:
            if data.name.lower() == category.lower():
                found = True
                official_name = data.name
        if not found:
            raise ValueError('La categoría no existe')

        self.movements.append(Movement(title, number, official_name, m_type, date.today()))

    def calculate_totals(self):
        entries = 0
        outcomes = 0

        for movement in self.movements:
            if movement.m_type == INCOME:
                entries = entries + movement.amount
            elif movement.m_type == EXPENSE:
                outcomes = outcomes + movement.amount
        balance = entries - outcomes
        return {
            "income": entries,
            "expenses": outcomes,
            "balance": balance
        }
