from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class PauseOrActivateAd(Tool):
    """Suspend or enable a specific ad using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None, status: str = None) -> str:
        for ad in data.get("ads", []):
            if ad.get("ad_id") == ad_id:
                ad["status"] = status
                payload = ad
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad {ad_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PauseOrActivateAd",
                "description": "Pause or activate a single ad by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["ad_id", "status"],
                },
            },
        }
