from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateInventoryAdjustment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str, sku: str, amount: int, reason: str = "audit_discrepancy", timestamp: Any = None) -> str:
        # Verify the existence of the inventory record
        inventory = data.get("inventory", {}).values()
        exists = any(
            item["store_id"] == store_id and item["sku"] == sku for item in inventory.values()
        )
        if not exists:
            payload = {
                "error": f"Inventory record not found for store_id {store_id} and sku {sku}"
            }
            out = json.dumps(payload)
            return out
        # Utilize hash-based adjustment_id exclusively in all scenarios
        adj_id = f"ADJ-{hashlib.sha256(f'{store_id}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "store_id": store_id,
            "sku": sku,
            "amount": amount,
            "reason": reason,
        }
        data.setdefault("inventory_adjustments", []).append(entry)
        resp = {
            "message": "Inventory adjustment created.",
            "adjustment_id": adj_id,
            "entry": entry,
        }
        if amount > 1000:
            resp["dual_approval_required"] = True
        payload = resp
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInventoryAdjustment",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "amount": {"type": "number"},
                    "reason": {"type": "string"},
                },
                "required": ["store_id", "sku", "amount"],
            },
        }
