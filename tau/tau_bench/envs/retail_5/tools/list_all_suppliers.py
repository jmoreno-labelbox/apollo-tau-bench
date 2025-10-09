from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class ListAllSuppliers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        suppliers = data["suppliers"]

        # Provide basic supplier information without extensive inventory details
        supplier_list = []
        for supplier in suppliers.values():
            supplier_list.append(
                {
                    "supplier_id": supplier["supplier_id"],
                    "name": supplier["name"],
                    "contact_info": supplier["contact_info"],
                    "total_products": len(supplier["products"]),
                }
            )
        payload = supplier_list
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listAllSuppliers",
                "description": "Get a list of all suppliers with basic information.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
