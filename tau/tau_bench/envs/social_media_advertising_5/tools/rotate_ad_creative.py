from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RotateAdCreative(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ad_id_to_activate: str = None, ad_id_to_pause: str = None, timestamp: Any = None) -> str:
        to_act = ad_id_to_activate
        to_pause = ad_id_to_pause
        ok_a = False
        ok_p = False
        for ad in data.get("ads", []):
            if ad.get("ad_id") == to_act:
                ad["status"] = "active"
                ok_a = True
            if ad.get("ad_id") == to_pause:
                ad["status"] = "paused"
                ok_p = True
        if ok_a and ok_p:
            payload = {"status": "success"}
            out = json.dumps(payload)
            return out
        payload = {"error": "ids_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RotateAdCreative",
                "description": "Activates one ad and pauses another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id_to_activate": {"type": "string"},
                        "ad_id_to_pause": {"type": "string"},
                    },
                    "required": ["ad_id_to_activate", "ad_id_to_pause"],
                },
            },
        }
