from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetSupplierInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, product_id: str = None) -> str:
        if not supplier_id and not product_id:
            payload = {"error": "Either supplier_id or product_id is required"}
            out = json.dumps(payload)
            return out

        suppliers = data["suppliers"]

        if supplier_id:
            supplier = next(
                (s for s in suppliers.values() if s["supplier_id"] == supplier_id), None
            )
            if not supplier:
                payload = {"error": "Supplier not found"}
                out = json.dumps(payload)
                return out
            payload = supplier
            out = json.dumps(payload, indent=2)
            return out

        if product_id:
            suppliers_for_product = []
            for supplier in suppliers.values():
                if product_id in supplier["products"]:
                    suppliers_for_product.append(
                        {
                            "supplier_id": supplier["supplier_id"],
                            "name": supplier["name"],
                            "contact_info": supplier["contact_info"],
                        }
                    )
            payload = suppliers_for_product
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSupplierInfo",
                "description": "Get supplier information by supplier ID or find suppliers for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to look up",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to find suppliers for",
                        },
                    },
                },
            },
        }
