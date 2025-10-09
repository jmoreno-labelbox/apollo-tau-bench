from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateCampaignStatus(Tool):
    """Modifies the status of a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, new_status: str = None) -> str:
        campaigns = data.get("campaigns", [])
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                old_status = campaign["status"]
                campaign["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Campaign status updated from '{old_status}' to '{new_status}'",
                }
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
                "name": "updateCampaignStatus",
                "description": "Updates the status of a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["campaign_id", "new_status"],
                },
            },
        }
