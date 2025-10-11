# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _money








def _to_number(d: Decimal) -> float:
    return float(d)

def _money(x: Decimal) -> Decimal:
    return x.quantize(_TWOPLACES, rounding=ROUND_HALF_UP)

def _dec(x) -> Decimal:
    return Decimal(str(x))

class GetPriceOfProduct(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], items: Any) -> str:
        items = items
        if not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing or invalid 'items'. Expected a list of {product_id, pricebook_id}."
                },
                indent=2,
            )
        pricebook_entries = list(data.get("pricebook_entries", {}).values())
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
                    if e.get("product_id") == product_id and e.get("pricebook_id") == pricebook_id
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
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_price_of_product",
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