# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_product(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = list(data.get("products", {}).values())

        # Timestamp needs to be sent for database records
        timestamp = kwargs.get("timestamp")

        # These values must be sent
        required_cols = [
            "sku",
            "name",
            "category",
            "price",
            "description",
            "supplier_id",
            "weight_kg",
            "dimensions_cm",
            "brand",
            "cost",
            "barcode",
            "tax_rate",
        ]

        # These values have defaults if not sent
        optional_cols = ["is_discountable", "status", "expiry_date", "discount_rate"]

        required_values = {k: kwargs.get(k) for k in required_cols}
        optional_values = {
            "is_discountable": False,
            "status": "active",
            "expiry_date": None,
            "discount_rate": 0.0,
        }
        optional_values.update({k: kwargs[k] for k in optional_cols if k in kwargs})

        # These values are calculated by the function
        fill_in = {"created_at": timestamp, "updated_at": timestamp}

        # Throw an error if any of the required values are missing
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

        # This is the order that the items appear in the database
        # May not be necessary since dictionaries are unordered, but it can make valiation easier if the items appear in the same order everytime
        col_order = [
            "sku",
            "name",
            "category",
            "price",
            "is_discountable",
            "description",
            "supplier_id",
            "weight_kg",
            "dimensions_cm",
            "brand",
            "cost",
            "barcode",
            "tax_rate",
            "discount_rate",
            "status",
            "expiry_date",
            "created_at",
            "updated_at",
        ]

        # Order the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Add to the database
        products.append(json.dumps(row_final, indent=2))

        # Return the whole row for reference
        return json.dumps(row_final, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_product",
                "description": "Adds a new product",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "name": {
                            "type": "string",
                            "description": "The human readable name of the product",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the product. Ex: Electronics",
                        },
                        "price": {
                            "type": "number",
                            "description": "The base price the customer pays",
                        },
                        "description": {
                            "type": "string",
                            "description": "A human readable description of the product",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "The supplier id of the supplier that offers the product",
                        },
                        "weight_kg": {
                            "type": "number",
                            "description": "The weight in kilos of the item",
                        },
                        "dimensions_cm": {
                            "type": "string",
                            "description": "The dimensions in cm of the product",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The brand of the product",
                        },
                        "cost": {
                            "type": "string",
                            "description": "The cost the store pays for the product",
                        },
                        "barcode": {
                            "type": "string",
                            "description": "The barcode of the product",
                        },
                        "tax_rate": {
                            "type": "string",
                            "description": "The tax rate of the product",
                        },
                        "is_discountable": {
                            "type": "bool",
                            "description": "OPTIONAL. If the product has an active discount. Ensure that the promotions table is updated with this information. Defaults to False",
                        },
                        "discount_rate": {
                            "type": "number",
                            "description": "OPTIONAL. The rate the product can be discounted at. Ensure that the promotions table is updated with this information. Defaults to 0",
                        },
                        "expiry_date": {
                            "type": "string",
                            "description": "OPTIONAL. If this product has an expiration. Defaults to None",
                        },
                        "status": {
                            "type": "status",
                            "description": "OPTIONAL. Status of the product. Defaults to 'active'",
                        },
                    },
                },
            },
        }
