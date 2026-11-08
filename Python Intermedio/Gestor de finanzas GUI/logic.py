from datetime import date
from model import Category, Movement, INCOME, EXPENSE


class FinanceManager:
    def __init__(self):
        self.categories = []
        self.movements = []

    def add_category(self, name):
        if name.strip() == '':
            raise ValueError('The name cannot be empty')

        for category in self.categories:
            if category.name.lower() == name.lower():
                raise ValueError('The category already exists')
        self.categories.append(Category(name))

    def add_movement(self, title, amount, category, m_type):
        if not self.categories:
            raise ValueError('There are no categories. Add one first')

        # Regla para title
        if title.strip() == '':
            raise ValueError('The title cannot be empty')

        # Regla para m_type
        if m_type not in (INCOME, EXPENSE):
            raise ValueError('Type must be Income or Expense')

        # Regla para amount
        try:
            number = float(amount)
        except ValueError:
            raise ValueError('The amount must be a number. Please try again')

        if number <= 0:
            raise ValueError('The amount must be greater than zero')

        # Regla para category
        found = False
        official_name = category
        for data in self.categories:
            if data.name.lower() == category.lower():
                found = True
                official_name = data.name
        if not found:
            raise ValueError('The category does not exist')

        self.movements.append(
            Movement(title, number, official_name, m_type, date.today())
        )

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







#---Pruebas---

# if __name__ == "__main__":
#     gestor = FinanceManager()

#     try:
#         gestor.add_movement("Salario", 1000, "Trabajo", INCOME)
#     except ValueError as error:
#         print("Error:", error)

#     gestor.add_category("Trabajo")
#     gestor.add_movement("Salario", 1000, "Trabajo", INCOME)
#     print([str(m) for m in gestor.movements])

#     try:
#         gestor.add_movement("   ", 1000, "Trabajo", INCOME)
#     except ValueError as error:
#         print("Error:", error)
#     try:
#         gestor.add_movement("Pizza", 20, "Trabajo", "Ingresso")
#     except ValueError as error:
#         print("Error:", error)

#     print(len(gestor.movements))


#     for bad_amount in ["abc", "-5", "0"]:
#         try:
#             gestor.add_movement("Prueba", bad_amount, "Trabajo", INCOME)
#         except ValueError as error:
#             print("Error:", error)

#     gestor.add_movement("Venta", "250", "Trabajo", INCOME)
#     print(gestor.movements[-1].amount)
#     try:
#         gestor.add_movement("Viaje", 100, "Viajes", EXPENSE)
#     except ValueError as error:
#         print("Error:", error)

#     gestor.add_movement("Bono", 50, "trabajo", INCOME)
#     print(gestor.movements[-1])


#     gestor2 = FinanceManager()
#     print(gestor2.calculate_totals())   # vacío: todo en 0

#     gestor2.add_category("Trabajo")
#     gestor2.add_movement("Salario", 1000, "Trabajo", INCOME)
#     gestor2.add_movement("Comida", 200, "Trabajo", EXPENSE)
#     gestor2.add_movement("Ropa", 50, "Trabajo", EXPENSE)
#     totals = gestor2.calculate_totals()
#     print(totals)
#     print(totals["balance"])