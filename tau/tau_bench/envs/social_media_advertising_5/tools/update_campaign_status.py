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

class UpdateCampaignStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, status: str = None) -> str:
        cid = campaign_id
        st = status
        for c in data.get("campaigns", []):
            if c.get("campaign_id") == cid:
                c["status"] = st
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"campaign {cid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCampaignStatus",
                "description": "Updates campaign status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["campaign_id", "status"],
                },
            },
        }
