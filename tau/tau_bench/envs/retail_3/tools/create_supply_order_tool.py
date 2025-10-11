# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

def _gen_supply_order_id(seed: Optional[int] = None) -> str:
    """
    Generate a synthetic supply order identifier (#SOxxxx) for simulations.
    """
    base = seed if isinstance(seed, int) else int(datetime.utcnow().timestamp())
    return f"#SO{base % 10_000:04d}"

class CreateSupplyOrderTool(Tool):
    """
    Create a new supply order in supply_orders.json for restocking purposes.

    Behavior:
    - Accepts a supplier_id and a list of items {product_id, item_id, quantity}.
    - Resolves each variant from products.json to carry forward name/price/options.
    - Writes a new entry to supply_orders.json with:
        {
          "supply_order_id": "#SOxxxx",
          "supplier_id": "...",
          "status": "pending",
          "items": [ {variant..., "quantity": int} ],
          "created_at": "UTC ISO",
          "events": []
        }

    Input (kwargs):
        supplier_id (str, required)
        items (List[dict], required) -> {product_id, item_id, quantity>=1}

    Output:
        JSON string with {"message","supply_order_id","items_count"} or {"error":...}.
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

        products = list(list(list(data.get("products", {}).values())) if isinstance(data.get("products"), dict) else data.get("products", []))
        resolved_items: List[Dict[str, Any]] = []

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
                "name": "create_supply_order",
                "description": "Create a new supply order with resolved product variants and write to supply_orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "items": {
                            "type": "array",
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
                    },
                    "required": ["supplier_id", "items"],
                },
            },
        }