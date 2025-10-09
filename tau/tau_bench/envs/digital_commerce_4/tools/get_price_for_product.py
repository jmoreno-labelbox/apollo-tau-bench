from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPriceForProduct(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], pricebook_id: str, product_id: str) -> str:
        pricebook_id, product_id = _sid(pricebook_id), _sid(product_id)
        pbes = data.get("pricebook_entries", [])
        pbe = next(
            (
                p
                for p in pbes
                if p.get("pricebook_id") == pricebook_id
                and p.get("product_id") == product_id
            ),
            None,
        )
        payload = pbe or {"error": "price not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPriceForProduct",
                "description": "Get price for a product from a pricebook.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pricebook_id": {"type": "string"},
                        "product_id": {"type": "string"},
                    },
                    "required": ["pricebook_id", "product_id"],
                },
            },
        }
