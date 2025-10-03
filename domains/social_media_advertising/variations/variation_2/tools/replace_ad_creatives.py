from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class ReplaceAdCreatives(Tool):
    """Disable one ad while enabling another within the same ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], activate_id: str = None, pause_id: str = None) -> str:
        changed = []
        for ad in data.get("ads", []):
            if ad.get("ad_id") == activate_id:
                ad["status"] = "active"
                changed.append(ad)
            if ad.get("ad_id") == pause_id:
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
                "name": "ReplaceAdCreatives",
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
