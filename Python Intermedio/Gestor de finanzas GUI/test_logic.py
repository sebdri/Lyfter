'''------------UNIT TESTING------------'''





import unittest
from datetime import date
from logic import FinanceManager
from model import Movement, INCOME, EXPENSE

class TestingFinanceManage(unittest.TestCase):
#1
    def test_add_category_valid(self):
        manager = FinanceManager() #gestor
        manager.add_category('Comida')
        self.assertEqual(len(manager.categories), 1)


#2
    def test_add_category_empty_name(self):
        manager = FinanceManager()
        with self.assertRaises(ValueError):
            manager.add_category("")

#3
    def test_add_category_duplicate_ignores_case(self):

        manager =  FinanceManager()
        manager.add_category("Comida")
        with self.assertRaises(ValueError):
            manager.add_category("comida")


#4
    def test_movement_without_category(self):
        manager = FinanceManager() #GESTOR
        with self.assertRaises(ValueError):
            manager.add_movement("Gym",100,"Gym",INCOME)


#5

    def test_if_amount_is_invalid(self):
        manager = FinanceManager()
        manager.add_category("Gasto innecesario")
        with self.assertRaises(ValueError): #lo que está dentro de este bloque debe lanzar un ValueError
            manager.add_movement("Gasto","cien","Gasto innecesario",INCOME) # La prueba pasa porque le estoy dando que es incorrecto con lo que si cumple con la funcion para cual ah sido creada

#6
    def test_safe_valid_movement(self):
        manager = FinanceManager()
        manager.add_category("Pago Claude Code")
        manager.add_movement("Gasto","50","Pago Claude Code",EXPENSE)
        self.assertEqual(len(manager.movements),1)
        self.assertEqual(manager.movements[0].amount,50.0)

#7
    def test_calculate_totals(self):
        manager = FinanceManager()
        manager.add_category("Gastos Varios")
        manager.add_movement("Salario","1000","Gastos Varios",INCOME)
        manager.add_movement("Gasto","200","Gastos Varios",EXPENSE)
        manager.add_movement("Gasto","50","Gastos Varios",EXPENSE)
        totals = manager.calculate_totals()
        self.assertEqual(totals["income"], 1000)
        self.assertEqual(totals["expenses"], 250)
        self.assertEqual(totals["balance"], 750)
        

#8
    def test_movement_to_dict_and_from_dict(self):
        original = Movement("Salario", 50.0, "Trabajo", INCOME, date(2026, 3, 25))
        data = original.to_dict()
        restored = Movement.from_dict(data)
        self.assertEqual(restored.date, original.date)
        self.assertEqual(restored.title, original.title)
        self.assertEqual(restored.amount, original.amount)







if __name__ == "__main__":
    unittest.main()