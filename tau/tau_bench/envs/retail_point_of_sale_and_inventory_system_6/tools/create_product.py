from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class create_product(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str,
        name: str,
        category: str,
        price: float,
        description: str,
        supplier_id: int,
        weight_kg: float,
        dimensions_cm: str,
        brand: str,
        cost: float,
        barcode: str,
        tax_rate: float,
        timestamp: str = None,
        is_discountable: bool = False,
        status: str = "active",
        expiry_date: str = None,
        discount_rate: float = 0.0,
    ) -> str:
        products = data.get("products", {}).values()

        # A timestamp must be included for database entries

        # These values are required to be provided
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

        # Default values will apply if these are not provided
        optional_cols = ["is_discountable", "status", "expiry_date", "discount_rate"]

        required_values = {
            "sku": sku,
            "name": name,
            "category": category,
            "price": price,
            "description": description,
            "supplier_id": supplier_id,
            "weight_kg": weight_kg,
            "dimensions_cm": dimensions_cm,
            "brand": brand,
            "cost": cost,
            "barcode": barcode,
            "tax_rate": tax_rate,
        }
        optional_values = {
            "is_discountable": is_discountable,
            "status": status,
            "expiry_date": expiry_date,
            "discount_rate": discount_rate,
        }

        # The function computes these values
        fill_in = {"created_at": timestamp, "updated_at": timestamp}

        # Raise an error if any required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            payload = {
                "error": "required values not sent: "
                + ", ".join([k for k in required_values.values() if required_values[k] is None])
            }
            out = json.dumps(
                payload,
                indent=2,
            )
            return out

        # This represents the order of items in the database
        # While not crucial due to the unordered nature of dictionaries, having items in a consistent order can facilitate validation
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

        # Arrange the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        products.append(json.dumps(row_final, indent=2))
        payload = row_final
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateProduct",
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
                            "type": "number",
                            "description": "The cost the store pays for the product",
                        },
                        "barcode": {
                            "type": "string",
                            "description": "The barcode of the product",
                        },
                        "tax_rate": {
                            "type": "number",
                            "description": "The tax rate of the product",
                        },
                        "is_discountable": {
                            "type": "boolean",
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
                            "type": "string",
                            "enum": ["active", "inactive"],
                            "description": "OPTIONAL. Status of the product. Defaults to 'active'",
                        },
                    },
                },
            },
        }
