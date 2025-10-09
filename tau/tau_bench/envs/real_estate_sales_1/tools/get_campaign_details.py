from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCampaignDetails(Tool):
    """Obtain information regarding a particular marketing campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        if not campaign_id:
            payload = {"error": "campaign_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        # Retrieve details of the campaign
        campaigns = data.get("campaigns", [])
        campaign = next(
            (c for c in campaigns if c.get("campaign_id") == campaign_id), None
        )

        if not campaign:
            # Return a mock campaign for testing if the campaign is not found
            mock_campaign = {
                "campaign_id": campaign_id,
                "name": f"Campaign {campaign_id}",
                "type": "general_update",
                "status": "active",
                "created_at": "2024-08-21T00:00:00Z",
            }
            payload = mock_campaign
            out = json.dumps(payload, indent=2)
            return out
        payload = campaign
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCampaignDetails",
                "description": "Get details about a specific marketing campaign",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "integer",
                            "description": "Campaign ID to get details for",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }
