from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetSupplierDetails(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        name: str = None,
        contact_info: dict[str, Any] = None,
        performance_metrics: dict[str, Any] = None,
        notes: str = "",
        products: list[str] = None,
        item_stock: dict[str, Any] = None,
        last_updated: str = "Never"
    ) -> str:
        """
        Retrieve comprehensive supplier information and performance metrics

        Data Sources: suppliers.json (supplier_id, name, contact_info, products, item_stock)
        """
        suppliers = data.get("suppliers", [])
        supplier_found = None

        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                supplier_found = supplier
                break

        if not supplier_found:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "not_found"}
            out = json.dumps(payload)
            return out

        # Calculate stock metrics
        item_stock = supplier_found.get("item_stock", {})
        total_items = len(item_stock)
        available_items = 0
        out_of_stock_items = 0
        discontinued_items = 0
        total_stock_value = 0

        for item_id, stock_level in item_stock.items():
            if stock_level == "out_of_stock":
                out_of_stock_items += 1
            elif stock_level == "discontinued":
                discontinued_items += 1
            elif isinstance(stock_level, (int, str)) and str(stock_level).isdigit():
                available_items += 1
                total_stock_value += int(stock_level)

        # Calculate availability rate
        availability_rate = (
            (available_items / total_items * 100) if total_items > 0 else 0
        )

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_info": {
                "name": supplier_found.get("name"),
                "contact_info": supplier_found.get("contact_info", {}),
                "performance_metrics": supplier_found.get("performance_metrics", {}),
                "notes": supplier_found.get("notes", ""),
            },
            "product_portfolio": {
                "total_products": len(supplier_found.get("products", [])),
                "product_ids": supplier_found.get("products", []),
            },
            "inventory_summary": {
                "total_items": total_items,
                "available_items": available_items,
                "out_of_stock_items": out_of_stock_items,
                "discontinued_items": discontinued_items,
                "availability_rate_percent": round(availability_rate, 1),
                "total_stock_units": total_stock_value,
            },
            "last_updated": supplier_found.get("last_updated", "Never"),
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierDetails",
                "description": "Retrieve comprehensive supplier information and performance metrics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
