# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindSupplierByName(Tool):
    """Finds a supplier's ID and lead time by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_name) -> str:
        suppliers = list(data.get("supplier_master", {}).values())
        for supplier in suppliers:
            if supplier.get("supplier_name") == supplier_name:
                return json.dumps(
                    {
                        "supplier_id": supplier.get("supplier_id"),
                        "standard_lead_time_days": supplier.get(
                            "standard_lead_time_days"
                        ),
                    }
                )
        return json.dumps({"error": "Supplier not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_supplier_by_name",
                "description": "Finds a supplier's ID and standard lead time by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_name": {
                            "type": "string",
                            "description": "The full name of the supplier.",
                        }
                    },
                    "required": ["supplier_name"],
                },
            },
        }
