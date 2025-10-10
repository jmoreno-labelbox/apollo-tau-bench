import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> Dict[str, Any]:
    with open(os.path.join(FOLDER_PATH, "customers.json")) as f:
        customers_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "products.json")) as f:
        products_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "promotions.json")) as f:
        promotions_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "employees.json")) as f:
        employees_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "transactions.json")) as f:
        transactions_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "inventory.json")) as f:
        inventory_data = json.load(f)
    return {
        "customers": customers_data,
        "products": products_data,
        "promotions": promotions_data,
        "employees": employees_data,
        "transactions": transactions_data,
        "inventory": inventory_data
    }
