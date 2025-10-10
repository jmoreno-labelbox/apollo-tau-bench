# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW, _find_one


class ManageInventoryLevels(Tool):
    """Manage product inventory levels and track stock movements."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        product_id: Any,
        quantity_adjustment: Any = 0,
        movement_type: Any = "adjustment",
    ) -> str:
        product_id = _idstr(product_id)
        quantity_adjustment = int(quantity_adjustment)
        movement_type = f"{movement_type}"

        if not product_id:
            return _error("product_id is required.")

        products = list(data.get("products", {}).values())
        product = _find_one(products, "product_id", product_id)
        if not product:
            return _error(f"Product '{product_id}' not found.")

        inventory = data.setdefault("inventory", [])
        inv_item = _find_one(inventory, "product_id", product_id)
        if not inv_item:
            initial_qty = (
                int(product.get("stock_quantity", 0))
                if isinstance(product.get("stock_quantity"), int)
                else 100
            )
            inv_item = {
                "product_id": product_id,
                "quantity_on_hand": initial_qty,
                "reserved_quantity": 0,
                "last_updated": FIXED_NOW,
            }
            inventory.append(inv_item)

        old_quantity = int(inv_item.get("quantity_on_hand", 0))
        new_quantity = max(0, old_quantity + quantity_adjustment)
        inv_item["quantity_on_hand"] = new_quantity
        inv_item["last_updated"] = FIXED_NOW

        return json.dumps(
            {
                "product_id": product_id,
                "old_quantity": old_quantity,
                "new_quantity": new_quantity,
                "adjustment": quantity_adjustment,
                "movement_type": movement_type,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_inventory_levels",
                "description": "Manage product inventory levels and track stock movements.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "quantity_adjustment": {"type": "integer"},
                        "movement_type": {"type": "string"},
                    },
                    "required": ["product_id"],
                },
            },
        }
