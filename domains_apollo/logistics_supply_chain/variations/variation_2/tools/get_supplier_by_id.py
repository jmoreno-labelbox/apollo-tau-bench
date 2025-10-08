from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetSupplierByID(Tool):
    """Utility for obtaining supplier information using their ID."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str, list_of_ids: list = None) -> str:
        suppliers = data.get("supplier_master", [])
        for supplier in suppliers:
            if supplier["supplier_id"] == supplier_id:
                payload = supplier
                out = json.dumps(payload, indent=2)
                return out
        suppliers = [s for s in suppliers if s in list_of_ids]
        payload = {"error": f"Supplier ID '{supplier_id}' not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierById",
                "description": "Retrieve supplier information using the supplier ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID (e.g., 'SUP-1005')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of suppliers to choose from.",
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }
