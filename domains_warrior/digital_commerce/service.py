import json
from pathlib import Path
from typing import List, Dict, Any
import copy

from domains.base import BaseDomain
from domains.dto import Tool


class DigitalCommerceSystem(BaseDomain):
    def __init__(self, tools: List[Tool]):
        super().__init__(tools)
        self.master_database = self._load_data()
        self.database = copy.deepcopy(self.master_database)

    def reset_database(self):
        self.database = copy.deepcopy(self.master_database)
        return True

    def _load_data(self) -> Dict[str, Any]:
        db = {}
        data_path = Path(__file__).parent / "data"

        table_files = [
            "accounts",
            "aws_elasticache_clusters",
            "aws_security_group_rules",
            "aws_subnet_groups",
            "cache_jobs",
            "cart_items",
            "carts",
            "cases",
            "catalogs",
            "categories",
            "connected_apps",
            "contacts",
            "custom_settings",
            "offers",
            "order_items",
            "orders",
            "pricebook_entries",
            "pricebooks",
            "products",
            "salesforce_orgs",
            "trace_flags",
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
                if table_name in [
                    "accounts",
                    "aws_elasticache_clusters",
                    "aws_security_group_rules",
                    "aws_subnet_groups",
                    "cache_jobs",
                    "cart_items",
                    "carts",
                    "cases",
                    "catalogs",
                    "categories",
                    "connected_apps",
                    "contacts",
                    "custom_settings",
                    "offers",
                    "order_items",
                    "orders",
                    "pricebook_entries",
                    "pricebooks",
                    "products",
                    "salesforce_orgs",
                    "trace_flags",
                ]:
                    raise FileNotFoundError(f"Core data file not found: {file_path}")
                db[table_name] = []
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {file_path}: {e}")
                db[table_name] = []

        return db
