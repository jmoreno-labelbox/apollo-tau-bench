# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSupplier(Tool):
    """Tool to update supplier information."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id, updates) -> str:
        suppliers = list(data.get("supplier_master", {}).values())

        for supplier in suppliers:
            if supplier["supplier_id"] == supplier_id:
                supplier.update(updates)
                return json.dumps({"success": f"supplier {supplier_id} updated"}, indent=2)
        return json.dumps({"error": f"supplier_id {supplier_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_supplier",
                "description": "Update supplier by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The supplier ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["supplier_id", "updates"]
                }
            }
        }
