# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_inventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory = list(data.get("inventory", {}).values())

        # A timestamp must be included for database entries.
        timestamp = kwargs.get("timestamp")

        # These values are required to be transmitted.
        required_cols = [
            "sku",
            "store_id",
            "quantity",
            "reserved_quantity",
            "reorder_level",
            "safety_stock",
            "location",
        ]

        # Default values are used if none are provided.
        optional_cols = []

        required_values = {k: kwargs.get(k) for k in required_cols}
        optional_values = {}
        optional_values.update({k: kwargs[k] for k in optional_cols if k in kwargs})

        # The function computes these values.
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

        # Trigger an error if any necessary values are absent.
        if any([required_values[k] is None for k in required_values.keys()]):
            return json.dumps(
                {
                    "error": "required values not sent: "
                    + ", ".join(
                        [k for k in required_values if required_values[k] is None]
                    )
                },
                indent=2,
            )

        # This reflects the sequence in which the items are stored in the database.
        # While dictionaries are unordered, maintaining a consistent item order can simplify validation.
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

        # Sort the items.
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        inventory.append(json.dumps(row_final, indent=2))

        # Retrieve the complete row for reference.
        return json.dumps(row_final, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inventory",
                "description": "Adds a new inventory item to the store. This is for items the store has never stocked before, to update the quantity of an existing item, use update_stock_quantity",
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
