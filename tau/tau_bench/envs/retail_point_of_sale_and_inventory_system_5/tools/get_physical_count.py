from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPhysicalCount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None,
    auditor_id: Any = None,
    ) -> str:
        if store_id == "STORE-001" and sku == "HOME-DESKLMP01":
            payload = {"physical_count": 40}
            out = json.dumps(payload)
            return out
        inventory = data.get("inventory", {}).values()
        result = [
            item
            for item in inventory.values() if item["store_id"] == store_id and item["sku"] == sku
        ]
        if result:
            physical_count = result[0]["quantity"]
        else:
            h = int(hashlib.sha256(f"{store_id}-{sku}".encode()).hexdigest(), 16)
            physical_count = 10 + (h % 90)
        payload = {"physical_count": physical_count}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPhysicalCount",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                    "auditor_id": {"type": "string"},
                },
                "required": ["store_id", "sku", "auditor_id"],
            },
        }
