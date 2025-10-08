from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetNameForCampaign(Tool):
    """Fetches a particular campaign using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        campaigns = data.get("campaigns", [])

        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                payload = {"name": campaign.get("name")}
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
                "name": "GetNameForCampaign",
                "description": "Retrieves a specific campaign by ID.",
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
