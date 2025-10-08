from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateSupplier(Tool):
    """Utility for modifying supplier details."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, updates: dict[str, Any] = None) -> str:
        suppliers = data.get("supplier_master", [])

        for supplier in suppliers:
            if supplier["supplier_id"] == supplier_id:
                supplier.update(updates)
                payload = {"success": f"supplier {supplier_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"supplier_id {supplier_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSupplier",
                "description": "Update supplier by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The supplier ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["supplier_id", "updates"],
                },
            },
        }
