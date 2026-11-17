'''Persistence'''
import json
import os  # Permite hacerle consultas a la computadora

from logic import FinanceManager
from model import Category, Movement

DATA_FILE = os.path.join(os.path.dirname(__file__), "finance_data.json")


def save_data(manager, file_path=DATA_FILE):
    categories_data = []  # La bolsa vacía (lista)
    for category in manager.categories:  # Revisando las categorías ficha por ficha
        categories_data.append(category.to_dict())  # Agregando a la bolsa

    movements_data = []
    for movement in manager.movements:
        movements_data.append(movement.to_dict())

    data = {  # Nueva bolsa (variable) donde vamos a guardar datos
        "categories": categories_data,
        "movements": movements_data,
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data(file_path=DATA_FILE):
    '''Carga el gestor desde el JSON. Si el archivo no existe, está vacío
    o está dañado, devuelve un gestor vacío para que la app arranque igual.'''
    if not os.path.exists(file_path):
        return FinanceManager()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        manager = FinanceManager()
        for category_data in data.get("categories", []):
            manager.categories.append(Category.from_dict(category_data))
        for movement_data in data.get("movements", []):
            manager.movements.append(Movement.from_dict(movement_data))
        return manager
    except (json.JSONDecodeError, AttributeError, KeyError, TypeError, ValueError):
        return FinanceManager()
