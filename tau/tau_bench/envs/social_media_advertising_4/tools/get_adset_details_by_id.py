from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAdsetDetailsByID(Tool):
    """Obtains the details for an individual ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        for adset in data.get("adsets", {}).values():
            if adset.get("adset_id") == adset_id:
                payload = adset
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetDetailsById",
                "description": "Retrieves the full details for a single ad set using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
