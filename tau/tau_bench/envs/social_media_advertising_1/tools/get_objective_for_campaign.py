from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetObjectiveForCampaign(Tool):
    """Fetches the goal of a specific campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        campaigns = data.get("campaigns", {}).values()

        for campaign in campaigns.values():
            if campaign.get("campaign_id") == campaign_id:
                payload = {"objective": campaign.get("objective")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign with ID '{campaign_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getObjectiveForCampaign",
                "description": "Retrieves the objective for a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }
