# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str) -> str:
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
            return json.dumps({
                "error": f"Supplier {supplier_id} not found",
                "status": "not_found"
            })

        # Compute stock indicators.
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

        # Determine the availability ratio.
        availability_rate = (available_items / total_items * 100) if total_items > 0 else 0

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_info": {
                "name": supplier_found.get("name"),
                "contact_info": supplier_found.get("contact_info", {}),
                "performance_metrics": supplier_found.get("performance_metrics", {}),
                "notes": supplier_found.get("notes", "")
            },
            "product_portfolio": {
                "total_products": len(supplier_found.get("products", [])),
                "product_ids": supplier_found.get("products", [])
            },
            "inventory_summary": {
                "total_items": total_items,
                "available_items": available_items,
                "out_of_stock_items": out_of_stock_items,
                "discontinued_items": discontinued_items,
                "availability_rate_percent": round(availability_rate, 1),
                "total_stock_units": total_stock_value
            },
            "last_updated": supplier_found.get("last_updated", "Never")
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_details",
                "description": "Retrieve comprehensive supplier information and performance metrics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier (e.g., '#SUP0001')"}
                    },
                    "required": ["supplier_id"]
                }
            }
        }
