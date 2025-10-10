# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierInfo(Tool):
    """Tool to get information about a supplier."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str) -> str:
        """Execute the tool with given parameters."""
        suppliers = data.get("supplier_master", [])
        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                return json.dumps(supplier, indent=2)
        return json.dumps({"error": f"Supplier with ID {supplier_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_info",
                "description": "Retrieves detailed information about a specific supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The ID of the supplier."}
                    },
                    "required": ["supplier_id"],
                },
            },
        }
