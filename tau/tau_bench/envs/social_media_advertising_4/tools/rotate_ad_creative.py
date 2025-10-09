from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RotateAdCreative(Tool):
    """Suspends one ad while enabling another."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id_to_activate: str = None, ad_id_to_pause: str = None, timestamp: Any = None) -> str:
        ad_to_activate, ad_to_pause = ad_id_to_activate, ad_id_to_pause
        activated, paused = False, False
        for ad in data.get("ads", {}).values():
            if ad.get("ad_id") == ad_to_activate:
                ad["status"], activated = "active", True
            if ad.get("ad_id") == ad_to_pause:
                ad["status"], paused = "paused", True
        if activated and paused:
            payload = {"status": "success"}
            out = json.dumps(payload)
            return out
        payload = {"error": "One or both ad IDs not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RotateAdCreative",
                "description": "Activates one ad and pauses another, effectively rotating the active creative.",
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
