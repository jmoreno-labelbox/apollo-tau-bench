# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierByID(Tool):
    """Tool to retrieve a supplier's details by their ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        list_of_suppliers = kwargs.get("list_of_ids", None)
        suppliers = list(data.get("supplier_master", {}).values())
        for supplier in suppliers:
            if supplier["supplier_id"] == supplier_id:
                return json.dumps(supplier, indent=2)
        suppliers = [s for s in suppliers if s in list_of_suppliers]
        return json.dumps({"error": f"Supplier ID '{supplier_id}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_by_id",
                "description": "Retrieve supplier information using the supplier ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID (e.g., 'SUP-1005')"
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of suppliers to choose from."
                        }
                    },
                    "required": ["supplier_id"]
                }
            }
        }
