# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PriceAndApplyOfferByNames(Tool):
    """
    Price items by product name and pricebook, then apply an offer code.
    Inputs:
      - pricebook_id: str
      - items_by_name: [{ "name": str, "quantity": int }]
      - offer_code: str
    Returns:
      {
        "items": [
          {"product_id": "...", "name": "...", "quantity": int, "unit_price": float, "line_total": float}
        ],
        "subtotal": float,
        "applied_offer_code": str,
        "discount_amount": float,
        "total": float
      }
    """

    @staticmethod
    def invoke(data: Dict[str, Any], pricebook_id: Any, items_by_name: Any, offer_code: Any) -> str:
        def _err(msg):
            return json.dumps({"error": msg}, indent=2)

        if not pricebook_id or not isinstance(items_by_name, list) or not offer_code:
            return _err("Missing required fields: pricebook_id, items_by_name (list), offer_code")

        products = list(data.get("products", {}).values())
        price_entries = data.get("pricebook_entries", []) or data.get("prices", [])
        offers = data.get("offers", [])

        name_to_product = {p.get("name"): p for p in products if p.get("name")}

        def _price_for(pid, pbid):
            for e in price_entries:
                if e.get("product_id") == pid and str(e.get("pricebook_id")) == str(pbid):
                    return float(e.get("price"))
            return None

        offer_rec = None
        for o in offers:
            if o.get("offer_code") == offer_code or o.get("code") == offer_code:
                offer_rec = o
                break
        if offer_rec is None:
            offer_rec = {
                "offer_code": offer_code,
                "discount_type": "PERCENTAGE",
                "discount_value": 0.0,
            }

        lines = []
        subtotal = 0.0
        for item in items_by_name:
            nm = item.get("name")
            qty = int(item.get("quantity", 0))
            prod = name_to_product.get(nm)
            if not prod:
                return _err(f"Product not found by name: {nm}")
            pid = prod.get("product_id")
            unit_price = _price_for(pid, pricebook_id)
            if unit_price is None:
                return _err(f"Price not found for product_id={pid} in pricebook_id={pricebook_id}")
            line_total = unit_price * qty
            subtotal += line_total
            lines.append(
                {
                    "product_id": pid,
                    "name": nm,
                    "quantity": qty,
                    "unit_price": unit_price,
                    "line_total": line_total,
                }
            )
        discount_amount = 0.0
        dtype = str(offer_rec.get("discount_type", "PERCENTAGE")).upper()
        dval = float(offer_rec.get("discount_value", 0.0))
        if dtype == "PERCENTAGE":
            discount_amount = round(subtotal * (dval / 100.0), 2)
        elif dtype == "FIXED_AMOUNT":
            discount_amount = min(subtotal, dval)
        total = round(subtotal - discount_amount, 2)

        result = {
            "items": lines,
            "subtotal": round(subtotal, 2),
            "applied_offer_code": offer_code,
            "discount_amount": discount_amount,
            "total": total,
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "price_and_apply_offer_by_names",
                "description": "Resolve product names via catalog, price by pricebook, compute subtotal, apply offer, and return totals.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pricebook_id": {"type": "string"},
                        "items_by_name": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["name", "quantity"],
                            },
                        },
                        "offer_code": {"type": "string"},
                    },
                    "required": ["pricebook_id", "items_by_name", "offer_code"],
                },
            },
        }
