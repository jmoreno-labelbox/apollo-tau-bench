# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInventoryAdjustment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], amount, sku, store_id, reason = "audit_discrepancy") -> str:
        # Verify the presence of the inventory record.
        inventory = list(data.get("inventory", {}).values())
        exists = any(item["store_id"] == store_id and item["sku"] == sku for item in inventory)
        if not exists:
            return json.dumps({"error": f"Inventory record not found for store_id {store_id} and sku {sku}"})
        # Utilize hash-based adjustment_id exclusively for every scenario.
        adj_id = f"ADJ-{hashlib.sha256(f'{store_id}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "store_id": store_id,
            "sku": sku,
            "amount": amount,
            "reason": reason
        }
        data.setdefault("inventory_adjustments", []).append(entry)
        resp = {"message": "Inventory adjustment created.", "adjustment_id": adj_id, "entry": entry}
        if amount > 1000:
            resp["dual_approval_required"] = True
        return json.dumps(resp)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "create_inventory_adjustment",
                "description": "Tool function: create_inventory_adjustment",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
