import json
from pathlib import Path
from typing import List, Dict, Any

from domains.base import BaseDomain
from domains.dto import Tool

import copy

class RecipesServiceSystem(BaseDomain):
    """
    Domain service for recipes and meal planning system.
    Manages users, households, recipes, ingredients, meal plans, grocery lists,
    inventory, and store orders for comprehensive meal planning workflows.
    """
    def __init__(self, tools: List[Tool]):
        super().__init__(tools)
        self.master_database = self._load_data()
        self.database = copy.deepcopy(self.master_database)

    def reset_database(self):
        self.database = copy.deepcopy(self.master_database)
        return True

    def _load_data(self) -> Dict[str, Any]:
        """
        Loads all data tables from their JSON files for the recipes domain.
        """
        db = {}
        data_path = Path(__file__).parent / "data"

        table_files = [
            "users", "households", "members", "ingredients", "recipes",
            "recipe_ingredients", "meal_plans", "meal_plan_entries",
            "meal_history", "inventory_items", "grocery_lists",
            "grocery_list_items", "stores", "store_products",
            "orders", "order_items", "audit_logs"
        ]

        for table_name in table_files:
            file_path = data_path / f"{table_name}.json"
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content:
                        db[table_name] = json.loads(content)
                    else:
                        db[table_name] = []
            except FileNotFoundError:
                db[table_name] = []
            except json.JSONDecodeError:
                db[table_name] = []
        return db
