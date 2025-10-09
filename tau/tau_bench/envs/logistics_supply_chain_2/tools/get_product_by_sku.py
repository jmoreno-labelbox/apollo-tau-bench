from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProductBySKU(Tool):
    """Utility for obtaining a product using its SKU."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        products = data.get("product_master", [])
        for product in products:
            if product["sku"] == sku:
                payload = product
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"SKU '{sku}' not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductBySku",
                "description": "Retrieve a product's full details using its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU (e.g., 'PHRM-DRUG-S19')",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
