from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCustomerInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, sku: Any = None) -> str:
        customers = data.get("customers", {}).values()
        result = [item for item in customers.values() if item["customer_id"] == customer_id]
        if result:
            payload = result[0]
            out = json.dumps(payload)
            return out
        payload = {"error": f"Customer {customer_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerInfo",
                "parameters": {"customer_id": {"type": "string"}},
                "required": ["customer_id"],
            },
        }
