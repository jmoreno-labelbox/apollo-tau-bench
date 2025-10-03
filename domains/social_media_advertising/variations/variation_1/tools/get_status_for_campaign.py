from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetStatusForCampaign(Tool):
    """Fetches the current status of a specific campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        campaigns = data.get("campaigns", [])

        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                payload = {"status": campaign.get("status")}
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
                "name": "getStatusForCampaign",
                "description": "Retrieves the status for a specific campaign.",
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
