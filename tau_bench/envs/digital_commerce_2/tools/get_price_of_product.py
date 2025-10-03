from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class GetPriceOfProduct(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], items: list[dict[str, Any]]) -> str:
        if not items or not isinstance(items, list):
            payload = {
                "error": "Missing or invalid 'items'. Expected a list of {product_id, pricebook_id}."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        pricebook_entries = data.get("pricebook_entries", [])
        results = []
        for item in items:
            product_id = item.get("product_id")
            pricebook_id = item.get("pricebook_id")
            if not product_id or not pricebook_id:
                results.append({"error": "Missing product_id or pricebook_id in item"})
                continue
            match = next(
                (
                    e
                    for e in pricebook_entries
                    if e.get("product_id") == product_id
                    and e.get("pricebook_id") == pricebook_id
                ),
                None,
            )
            if match:
                price = _money(_dec(match.get("price")))
                results.append({"product_id": product_id, "price": _to_number(price)})
            else:
                results.append(
                    {
                        "product_id": product_id,
                        "error": f"No price found in pricebook_id '{pricebook_id}'",
                    }
                )
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPriceOfProduct",
                "description": "Fetch the prices of multiple products for given pricebook_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "description": "List of products with pricebook_ids to fetch prices for.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {
                                        "type": "string",
                                        "description": "Exact product ID to retrieve price for.",
                                    },
                                    "pricebook_id": {
                                        "type": "string",
                                        "description": "Pricebook ID to look in.",
                                    },
                                },
                                "required": ["product_id", "pricebook_id"],
                            },
                        }
                    },
                    "required": ["items"],
                },
            },
        }
