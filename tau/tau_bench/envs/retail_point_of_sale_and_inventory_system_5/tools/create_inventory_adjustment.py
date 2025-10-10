# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInventoryAdjustment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs["store_id"]
        sku = kwargs["sku"]
        amount = kwargs["amount"]
        # Check if the inventory record exists
        inventory = list(data.get("inventory", {}).values())
        exists = any(item["store_id"] == store_id and item["sku"] == sku for item in inventory)
        if not exists:
            return json.dumps({"error": f"Inventory record not found for store_id {store_id} and sku {sku}"})
        # Only use hash-based adjustment_id for all cases
        adj_id = f"ADJ-{hashlib.sha256(f'{store_id}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "store_id": store_id,
            "sku": sku,
            "amount": amount,
            "reason": kwargs.get("reason", "audit_discrepancy")
        }
        data.setdefault("inventory_adjustments", []).append(entry)
        resp = {"message": "Inventory adjustment created.", "adjustment_id": adj_id, "entry": entry}
        if amount > 1000:
            resp["dual_approval_required"] = True
        return json.dumps(resp)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_inventory_adjustment", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "amount": {"type": "number"}, "reason": {"type": "string"}}, "required": ["store_id", "sku", "amount"]}}
