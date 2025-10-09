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

class UpdateAdsetBidStrategy(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, bid_strategy: str = None, bid_amount: float = None, updated_at: str = None) -> str:
        aid = adset_id
        bs = bid_strategy
        ba = bid_amount
        for a in data.get("adsets", {}).values():
            if a.get("adset_id") == aid:
                a["bid_strategy"] = bs
                a["bid_amount"] = ba
                a["updated_at"] = updated_at
                payload = a
                out = json.dumps(payload)
                return out
        payload = {"error": f"adset {aid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetBidStrategy",
                "description": "Updates bid strategy and bid amount.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": ["number", "null"]},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["adset_id", "bid_strategy", "updated_at"],
                },
            },
        }
