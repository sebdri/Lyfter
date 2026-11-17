'''------------UNIT TESTING LOGIC------------'''

import os
import tempfile
import unittest
from datetime import date

from logic import FinanceManager
from model import Movement, INCOME, EXPENSE
from persistence import save_data, load_data


class TestingFinanceManage(unittest.TestCase):
    # 1
    def test_add_category_valid(self):
        manager = FinanceManager()  # gestor
        manager.add_category('Comida')
        self.assertEqual(len(manager.categories), 1)

    # 2
    def test_add_category_empty_name(self):
        manager = FinanceManager()
        with self.assertRaises(ValueError):
            manager.add_category("")

    # 3
    def test_add_category_duplicate_ignores_case(self):
        manager = FinanceManager()
        manager.add_category("Comida")
        with self.assertRaises(ValueError):
            manager.add_category("comida")

    # 4
    def test_movement_without_category(self):
        manager = FinanceManager()  # gestor
        with self.assertRaises(ValueError):
            manager.add_movement("Gym", 100, "Gym", INCOME)

    # 5
    def test_if_amount_is_invalid(self):
        manager = FinanceManager()
        manager.add_category("Gasto innecesario")
        with self.assertRaises(ValueError):  # lo que está dentro de este bloque debe lanzar un ValueError
            manager.add_movement("Gasto", "cien", "Gasto innecesario", INCOME)

    # 6
    def test_safe_valid_movement(self):
        manager = FinanceManager()
        manager.add_category("Pago Claude Code")
        manager.add_movement("Gasto", "50", "Pago Claude Code", EXPENSE)
        self.assertEqual(len(manager.movements), 1)
        self.assertEqual(manager.movements[0].amount, 50.0)

    # 7
    def test_calculate_totals(self):
        manager = FinanceManager()
        manager.add_category("Gastos Varios")
        manager.add_movement("Salario", "1000", "Gastos Varios", INCOME)
        manager.add_movement("Gasto", "200", "Gastos Varios", EXPENSE)
        manager.add_movement("Gasto", "50", "Gastos Varios", EXPENSE)
        totals = manager.calculate_totals()
        self.assertEqual(totals["income"], 1000)
        self.assertEqual(totals["expenses"], 250)
        self.assertEqual(totals["balance"], 750)

    # 8
    def test_movement_to_dict_and_from_dict(self):
        original = Movement("Salario", 50.0, "Trabajo", INCOME, date(2026, 3, 25))
        data = original.to_dict()
        restored = Movement.from_dict(data)
        self.assertEqual(restored.date, original.date)
        self.assertEqual(restored.title, original.title)
        self.assertEqual(restored.amount, original.amount)

    # 9
    def test_add_category_duplicate_ignores_spaces(self):
        manager = FinanceManager()
        manager.add_category("Comida")
        with self.assertRaises(ValueError):
            manager.add_category("Comida ")
        manager.add_category("  Ropa  ")
        self.assertEqual(manager.categories[-1].name, "Ropa")

    # 10
    def test_amount_zero_or_negative(self):
        manager = FinanceManager()
        manager.add_category("Trabajo")
        for bad_amount in (0, "0", -5, "-5"):
            with self.assertRaises(ValueError):
                manager.add_movement("Prueba", bad_amount, "Trabajo", INCOME)
        self.assertEqual(len(manager.movements), 0)


class TestingPersistence(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, "data.json")

    def tearDown(self):
        self.temp_dir.cleanup()

    # 11
    def test_save_and_load_round_trip(self):
        manager = FinanceManager()
        manager.add_category("Trabajo")
        manager.add_movement("Salario", "1000", "Trabajo", INCOME)
        save_data(manager, self.file_path)

        loaded = load_data(self.file_path)
        self.assertEqual([c.name for c in loaded.categories], ["Trabajo"])
        self.assertEqual(len(loaded.movements), 1)
        self.assertEqual(loaded.movements[0].title, "Salario")
        self.assertEqual(loaded.movements[0].amount, 1000.0)
        self.assertEqual(loaded.movements[0].date, date.today())

    # 12
    def test_load_empty_or_corrupt_file(self):
        for content in ("", "{esto no es json"):
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(content)
            loaded = load_data(self.file_path)
            self.assertEqual(loaded.categories, [])
            self.assertEqual(loaded.movements, [])


if __name__ == "__main__":
    unittest.main()
