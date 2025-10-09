from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetApprovedSuppliers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str, preferred_supplier: str = None) -> str:
        suppliers = data.get("supplier_master", {}).values()
        product_master = data.get("product_master", {}).values()

        # Identify the product to determine its category
        product = next((p for p in product_master.values() if p.get("sku") == sku), None)
        if not product:
            return json.dumps({"error": f"Product {sku} not found"})

        product_category = product.get("category", "")

        # Locate suppliers that offer products within this category
        approved_suppliers = []
        for supplier in suppliers.values():
            supplier_categories = supplier.get("product_categories", [])

            if preferred_supplier and supplier.get("supplier_id") == preferred_supplier:
                # When a preferred supplier is indicated, give it priority
                approved_suppliers.insert(0, {
                    "supplier_id": supplier.get("supplier_id"),
                    "supplier_name": supplier.get("supplier_name"),
                    "performance_rating": supplier.get("performance_rating"),
                    "on_time_delivery_percentage": supplier.get("on_time_delivery_percentage"),
                    "standard_lead_time_days": supplier.get("standard_lead_time_days"),
                    "relationship_status": supplier.get("relationship_status"),
                    "product_categories": supplier_categories
                })
                break
            else:
                # Verify if the supplier caters to this product category and is operational
                if (any(cat in product_category for cat in supplier_categories.values() and))
                    supplier.get("relationship_status") == "Active" and
                    supplier.get("performance_rating", 0) >= 4.0):

                    approved_suppliers.append({
                        "supplier_id": supplier.get("supplier_id"),
                        "supplier_name": supplier.get("supplier_name"),
                        "performance_rating": supplier.get("performance_rating"),
                        "on_time_delivery_percentage": supplier.get("on_time_delivery_percentage"),
                        "standard_lead_time_days": supplier.get("standard_lead_time_days"),
                        "relationship_status": supplier.get("relationship_status"),
                        "product_categories": supplier.get("product_categories", [])
                    })

        return json.dumps({
            "sku": sku,
            "product_category": product_category,
            "approved_suppliers": approved_suppliers,
            "supplier_count": len(approved_suppliers)
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetApprovedSuppliers",
                "description": "Get list of approved suppliers for a specific SKU based on product category and performance criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU to find approved suppliers for",
                            "preferred_supplier": {
                                "type": "string",
                                "description": "Optional preferred supplier ID to prioritize in results"
                            }
                        }
                    },
                    "required": ["sku"]
                }
            }
        }
