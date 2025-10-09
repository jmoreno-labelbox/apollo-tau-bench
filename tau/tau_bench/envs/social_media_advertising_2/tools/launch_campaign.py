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

class LaunchCampaign(Tool):
    """Enable a campaign using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, reason: Any = None) -> str:
        cid = campaign_id
        for c in data.get("campaigns", {}).values():
            if c.get("campaign_id") == cid:
                c["status"] = "active"
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign {cid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LaunchCampaign",
                "description": "Activate a campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }
