# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierDetails(Tool):
    """Retrieves the full details for a supplier by their id."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id) -> str:
        suppliers = list(data.get("supplier_master", {}).values())
        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                return json.dumps(supplier)
        return json.dumps({"error": "Supplier not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_details",
                "description": "Retrieves the full record for a supplier by their id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The id of the supplier.",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
