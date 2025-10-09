from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateCampaignStatus(Tool):
    """Modifies the status of a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, status: str = None) -> str:
        for campaign in data.get("campaigns", {}).values():
            if campaign.get("campaign_id") == campaign_id:
                campaign["status"] = status
                payload = campaign
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign ID '{campaign_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCampaignStatus",
                "description": "Updates the status of a campaign (e.g., 'active', 'paused', 'archived').",
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
