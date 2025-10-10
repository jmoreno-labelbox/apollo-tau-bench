import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # automatically created from files located in data/
    tables = ['audit_logs', 'grocery_list_items', 'grocery_lists', 'households', 'ingredients', 'inventory_items', 'meal_history', 'meal_plan_entries', 'meal_plans', 'members', 'order_items', 'orders', 'recipe_ingredients', 'recipes', 'store_products', 'stores', 'users']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

