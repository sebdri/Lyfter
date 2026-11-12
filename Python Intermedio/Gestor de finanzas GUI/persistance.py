import json
import os  

from logic import FinanceManager
from model import Category, Movement

DATA_FILE = os.path.join(os.path.dirname(__file__), "finance_data.json")


def save_data(manager, file_path=DATA_FILE):
    categories_data = [] 
    for category in manager.categories: 
        categories_data.append(category.to_dict()) 
    movements_data = []
    for movement in manager.movements:
        movements_data.append(movement.to_dict())

    data = {  
        "categories": categories_data,
        "movements": movements_data,
    }

    with open(file_path, "w", encoding="utf-8") as file: 
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data(file_path=DATA_FILE):
    manager = FinanceManager()

    if not os.path.exists(file_path):
        return manager

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for category_data in data.get("categories", []):
        manager.categories.append(Category.from_dict(category_data))

    for movement_data in data.get("movements", []):
        manager.movements.append(Movement.from_dict(movement_data))

    return manager