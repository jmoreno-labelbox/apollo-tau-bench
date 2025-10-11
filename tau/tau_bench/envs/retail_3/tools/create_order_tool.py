# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrderTool(Tool):
    """
    Create a new retail order by resolving variants from products.json and
    using the customer's default address from users.json (unless overridden).

    Behavior:
    - Validates that user exists (users.json).
    - Validates items: each must include product_id, item_id, optional quantity>=1.
    - Resolves each (product_id, item_id) in products.json; expands by quantity.
    - Appends a new order entry in orders.json:
        {
          "order_id": "#Wxxxxxxx",
          "user_id": "...",
          "address": {...},              # from users.json or replace
          "items": [resolved variants],  # single entry for each unit
          "fulfillments": [],
          "status": "pending",
          "payment_history": [],
          "timestamp": "UTC ISO"
        }

    Input (kwargs):
        user_id (str, required)
        items (List[dict], required) -> {product_id, item_id, quantity?}
        address_override (dict, optional)

    Output:
        JSON string with {"message","order_id","status","items_count"} or {"error":...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], items, supplier_id) -> str:
        items_spec = items

        if not supplier_id or not isinstance(items_spec, list) or not items_spec:
            return json.dumps({"error": "supplier_id and non-empty items are required"}, indent=2)

        suppliers = data.get("suppliers", [])
        if not any(s.get("supplier_id") == supplier_id for s in suppliers):
            return json.dumps(
                {"error": f"supplier_id '{supplier_id}' not found in suppliers"},
                indent=2,
            )

        resolved_items: List[Dict[str, Any]] = []
        products = list(data.get("products", {}).values())
        for line in items_spec:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)
            if not pid or not iid or qty < 1:
                return json.dumps(
                    {"error": "Each item must include product_id, item_id, and quantity>=1"},
                    indent=2,
                )
            variant = None
            for p in products:
                if p.get("product_id") == pid:
                    variant_data = (p.get("variants") or {}).get(iid)
                    if variant_data:
                        variant = {
                            "name": p.get("name"),
                            "product_id": pid,
                            "item_id": iid,
                            "price": variant_data.get("price"),
                            "options": variant_data.get("options", {}),
                        }
                        break
            if not variant:
                return json.dumps(
                    {"error": f"Variant not found for product_id='{pid}', item_id='{iid}'"},
                    indent=2,
                )
            enriched = dict(variant)
            enriched["quantity"] = qty
            resolved_items.append(enriched)

        supply_orders = data.setdefault("supply_orders", [])
        new_so = {
            "supply_order_id": _gen_supply_order_id(),
            "supplier_id": supplier_id,
            "status": "pending",
            "items": resolved_items,
            "created_at": _now_iso(),
            "events": [],
        }
        supply_orders.append(new_so)

        return json.dumps(
            {
                "message": "supply_order_created",
                "supply_order_id": new_so["supply_order_id"],
                "items_count": len(resolved_items),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order",
                "description": "Create a new retail order by resolving product variants and writing into orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Existing user_id from users.json.",
                        },
                        "items": {
                            "type": "array",
                            "description": "Lines to add; each line expands by quantity into separate items.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "item_id": {"type": "string"},
                                    "quantity": {
                                        "type": "integer",
                                        "minimum": 1,
                                        "default": 1,
                                    },
                                },
                                "required": ["product_id", "item_id"],
                            },
                        },
                        "address_override": {
                            "type": "object",
                            "description": "Optional address that replaces the user's default.",
                            "properties": {
                                "address1": {"type": "string"},
                                "address2": {"type": "string"},
                                "city": {"type": "string"},
                                "country": {"type": "string"},
                                "state": {"type": "string"},
                                "zip": {"type": "string"},
                            },
                        },
                    },
                    "required": ["user_id", "items"],
                },
            },
        }
