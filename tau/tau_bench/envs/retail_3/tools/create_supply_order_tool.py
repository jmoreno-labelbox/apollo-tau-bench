from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateSupplyOrderTool(Tool):
    """
    Generate a new supply order in supply_orders.json for restocking needs.

    Behavior:
    - Accepts a supplier_id and a list of items {product_id, item_id, quantity}.
    - Resolves each variant from products.json to retain name/price/options.
    - Creates a new entry in supply_orders.json with:
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
    def invoke(data: dict[str, Any], supplier_id: str = None, items: list = None) -> str:
        if not supplier_id or not isinstance(items, list) or not items:
            payload = {"error": "supplier_id and non-empty items are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        suppliers = data.get("suppliers", {}).values()
        if not any(s.get("supplier_id") == supplier_id for s in suppliers.values()):
            payload = {"error": f"supplier_id '{supplier_id}' not found in suppliers"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        products = data.get("products", {}).values()
        resolved_items: list[dict[str, Any]] = []

        for line in items:
            pid = line.get("product_id")
            iid = line.get("item_id")
            qty = int(line.get("quantity", 1) or 1)
            if not pid or not iid or qty < 1:
                payload = {
                        "error": "Each item must include product_id, item_id, and quantity>=1"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            variant = None
            for p in products.values():
                if p.get("product_id") == pid:
                    variant_data = (p.get("variants") or {}).get(iid)
                    if variant_data:
                        variant = {
                            "name": p.get("name"),
                            "product_id": pid,
                            "item_id": iid,
                            "price": variant_data.get("price"),
                            "options": variant_data.get("options", {}).values()),
                        }
                        break

            if not variant:
                payload = {
                        "error": f"Variant not found for product_id='{pid}', item_id='{iid}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

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
        data["supply_orders"][supply_order_id] = new_so
        payload = {
                "message": "supply_order_created",
                "supply_order_id": new_so["supply_order_id"],
                "items_count": len(resolved_items),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createSupplyOrder",
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
