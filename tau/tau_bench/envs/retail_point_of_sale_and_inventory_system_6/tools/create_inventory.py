from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class create_inventory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str = None,
        store_id: str = None,
        quantity: int = None,
        reserved_quantity: int = None,
        reorder_level: int = None,
        safety_stock: int = None,
        location: str = None,
        timestamp: str = None
    ) -> str:
        inventory = data.get("inventory", [])

        # A timestamp is required for database records

        # These values are required to be sent
        required_cols = [
            "sku",
            "store_id",
            "quantity",
            "reserved_quantity",
            "reorder_level",
            "safety_stock",
            "location",
        ]

        # Default values will apply if these are not provided
        optional_cols = []

        required_values = {
            "sku": sku,
            "store_id": store_id,
            "quantity": quantity,
            "reserved_quantity": reserved_quantity,
            "reorder_level": reorder_level,
            "safety_stock": safety_stock,
            "location": location,
        }
        optional_values = {}

        # The function computes these values
        if required_values["quantity"] > required_values["reorder_level"]:
            status = "in_stock"
        elif required_values["quantity"] > required_values["safety_stock"]:
            status = "low_stock"
        else:
            status = "critical"
        fill_in = {
            "id": "INV-{inv_id:04}".format(
                inv_id=max([int(x["id"].split("-")[1][1:]) for x in inventory]) + 1
            ),
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": status,
            "last_stock_count": timestamp[:10],
        }

        # Raise an error if any required values are absent
        if any([required_values[k] is None for k in required_values.keys()]):
            payload = {
                "error": "required values not sent: "
                + ", ".join([k for k in required_values if required_values[k] is None])
            }
            out = json.dumps(
                payload,
                indent=2,
            )
            return out

        # This indicates the sequence of items in the database
        # Although not essential due to the unordered nature of dictionaries, maintaining the same order can simplify validation
        col_order = [
            "id",
            "sku",
            "store_id",
            "quantity",
            "reserved_quantity",
            "reorder_level",
            "safety_stock",
            "location",
            "status",
            "last_stock_count",
            "created_at",
            "updated_at",
        ]

        # Arrange the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        inventory.append(json.dumps(row_final, indent=2))
        payload = row_final
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createInventory",
                "description": "Adds a new inventory item to the store. This is for items the store has never stocked before, to update the quantity of an existing item, use UpdateStockQuantity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The sku of the item being added",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The id of the store adding the inventory",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "The amount that the store starts with",
                        },
                        "reserved_quantity": {
                            "type": "integer",
                            "description": "The amount in reserve",
                        },
                        "reorder_level": {
                            "type": "integer",
                            "description": "The amount to start reordering products",
                        },
                        "safety_stock": {
                            "type": "integer",
                            "description": "The amount to consider critical stock",
                        },
                        "location": {
                            "type": "string",
                            "description": "The shelf location of the item",
                        },
                    },
                },
            },
        }
