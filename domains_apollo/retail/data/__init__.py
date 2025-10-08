import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> Dict[str, Any]:
    with open(os.path.join(FOLDER_PATH, "orders.json")) as f:
        orders_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "products.json")) as f:
        products_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "users.json")) as f:
        users_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "couriers.json")) as f:
        couriers_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "suppliers.json")) as f:
        suppliers_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "supply_orders.json")) as f:
        supply_orders_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "tracking.json")) as f:
        tracking_data = json.load(f)
    return {
        "orders": orders_data,
        "products": products_data,
        "users": users_data,
        "couriers": couriers_data,
        "suppliers": suppliers_data,
        "supply_orders": supply_orders_data,
        "tracking": tracking_data,
    }
