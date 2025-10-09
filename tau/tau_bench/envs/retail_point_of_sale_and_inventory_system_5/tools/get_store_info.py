from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetStoreInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None) -> str:
        stores = data.get("stores", [])
        result = [item for item in stores if item["store_id"] == store_id]
        if result:
            payload = result[0]
            out = json.dumps(payload)
            return out
        payload = {"error": f"Store {store_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getStoreInfo",
                "parameters": {"store_id": {"type": "string"}},
                "required": ["store_id"],
            },
        }
