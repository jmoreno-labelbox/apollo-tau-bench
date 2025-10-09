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

class StopCampaign(Tool):
    """Suspend a campaign identified by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None,
    reason: Any = None,
    ) -> str:
        for c in data.get("campaigns", {}).values():
            if c.get("campaign_id") == campaign_id:
                c["status"] = "paused"
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign {campaign_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StopCampaign",
                "description": "Pause a campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }
