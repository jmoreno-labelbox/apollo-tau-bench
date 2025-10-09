from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetNextOrderId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], orders: list = None) -> str:
        if orders is None:
            orders = data.get("orders", [])
        if not orders:
            next_id = 9017
        else:
            max_id = max(int(o.get("order_id", "0")) for o in orders)
            next_id = max_id + 1
        payload = {"next_order_id": f"{next_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNextOrderId",
                "description": "Return the next available order_id as a zero-padded string.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
