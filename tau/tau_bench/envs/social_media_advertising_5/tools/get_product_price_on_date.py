from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProductPriceOnDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, date: str = None) -> str:
        pid = product_id
        d = date
        for r in data.get("f_price", {}).values():
            if r.get("product_id") == pid and r.get("date") == d:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": "price_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductPriceOnDate",
                "description": "Gets product price on a date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["product_id", "date"],
                },
            },
        }
