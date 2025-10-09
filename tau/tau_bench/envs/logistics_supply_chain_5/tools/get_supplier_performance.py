from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetSupplierPerformance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, supplier_name: str = None, performance_rating: float = None, 
               on_time_delivery_percentage: float = None, relationship_status: str = None, 
               certifications: list = None, standard_lead_time_days: int = None, payment_terms: str = None) -> str:
        suppliers = data.get("supplier_master", [])

        supplier = next((s for s in suppliers if s.get("supplier_id") == supplier_id), None)

        if not supplier:
            return json.dumps({"error": f"Supplier {supplier_id} not found"})

        performance_data = {
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "performance_rating": supplier.get("performance_rating"),
            "on_time_delivery_percentage": supplier.get("on_time_delivery_percentage"),
            "relationship_status": supplier.get("relationship_status"),
            "certifications": supplier.get("certifications", []),
            "standard_lead_time_days": supplier.get("standard_lead_time_days"),
            "payment_terms": supplier.get("payment_terms")
        }

        return json.dumps(performance_data)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierPerformance",
                "description": "Retrieve supplier performance metrics and details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"}
                    },
                    "required": ["supplier_id"]
                }
            }
        }
