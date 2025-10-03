from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class DeleteCampaign(Tool):
    """Removes a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        if not campaign_id:
            payload = {"error": "campaign_id is a required parameter."}
            out = json.dumps(payload)
            return out

        campaigns = data.get("campaigns", [])
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                data["campaigns"] = [
                    d for d in data["campaigns"] if d["campaign_id"] != campaign_id
                ]
                payload = {
                    "status": "success",
                    "message": f"Campaign with id {campaign_id} deleted successfully",
                }
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
                "name": "deleteCampaign",
                "description": "Deletes a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign to delete.",
                        },
                    },
                    "required": ["campaign_id"],
                },
            },
        }
