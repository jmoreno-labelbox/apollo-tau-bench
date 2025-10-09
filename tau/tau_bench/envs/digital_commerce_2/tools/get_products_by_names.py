from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProductsByNames(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], names: list[str]) -> str:
        if not names or not isinstance(names, list):
            payload = {
                "error": "Missing or invalid 'names'. Expected a list of product names."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        products = data.get("products", {}).values()
        results: list[dict[str, Any]] = []
        for n in names:
            match = next((p for p in products.values() if p.get("name") == n), None)
            results.append(
                match if match else {"name": n, "error": "Product not found"}
            )
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsByNames",
                "description": "Fetch multiple products by their exact names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "names": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product names to fetch.",
                        }
                    },
                    "required": ["names"],
                },
            },
        }
