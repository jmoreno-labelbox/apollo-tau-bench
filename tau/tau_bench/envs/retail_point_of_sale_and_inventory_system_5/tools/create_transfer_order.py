from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class CreateTransferOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], from_store: str, to_store: str, sku: str, quantity: int, store_id: Any = None) -> str:
        # Employ hash-based transfer_id solely for all situations
        transfer_id = f"TRF-{hashlib.sha256(f'{from_store}-{to_store}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "from_store": from_store,
            "to_store": to_store,
            "sku": sku,
            "quantity": quantity,
        }
        data.setdefault("transfer_orders", []).append(entry)
        resp = {
            "message": "Transfer order created.",
            "transfer_id": transfer_id,
            "entry": entry,
        }
        if quantity > 25:
            resp["compliance_review_required"] = True
        payload = resp
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTransferOrder",
                "parameters": {
                    "from_store": {"type": "string"},
                    "to_store": {"type": "string"},
                    "sku": {"type": "string"},
                    "quantity": {"type": "number"},
                },
                "required": ["from_store", "to_store", "sku", "quantity"],
            },
        }
