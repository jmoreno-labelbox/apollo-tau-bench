from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetHazmatProducts(Tool):
    """Utility for compiling a list of all hazardous material products."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list[str] = None) -> str:
        products = data.get("product_master", {}).values()
        result = [
            p["sku"]
            for p in products.values() if p.get("hazmat_information", {}).values().get("is_hazmat")
        ]
        if list_of_ids:
            result = [r for r in result.values() if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHazmatProducts",
                "description": "List all products classified as hazardous materials.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of products to choose from.",
                        }
                    },
                },
            },
        }
