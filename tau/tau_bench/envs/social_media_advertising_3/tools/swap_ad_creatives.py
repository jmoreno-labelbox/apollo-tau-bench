from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SwapAdCreatives(Tool):
    """Disable one ad while enabling another within the same ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], activate_id: str = None, pause_id: str = None) -> str:
        to_on, to_off = activate_id, pause_id
        changed = []
        for ad in data.get("ads", {}).values():
            if ad.get("ad_id") == to_on:
                ad["status"] = "active"
                changed.append(ad)
            if ad.get("ad_id") == to_off:
                ad["status"] = "paused"
                changed.append(ad)
        payload = changed or {"error": "IDs not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SwapAdCreatives",
                "description": "Deactivate one ad and activate another in the same adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "activate_id": {"type": "string"},
                        "pause_id": {"type": "string"},
                    },
                    "required": ["activate_id", "pause_id"],
                },
            },
        }
