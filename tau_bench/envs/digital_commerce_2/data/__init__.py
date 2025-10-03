import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # auto-generated from files present in data/
    tables = ['accounts', 'aws_elasticache_clusters', 'aws_security_group_rules', 'aws_subnet_groups', 'cache_jobs', 'cart_items', 'carts', 'cases', 'catalogs', 'categories', 'connected_apps', 'contacts', 'custom_settings', 'offers', 'order_items', 'orders', 'pricebook_entries', 'pricebooks', 'products', 'salesforce_orgs', 'trace_flags']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

