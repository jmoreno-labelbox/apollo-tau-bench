from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCampaignByName(Tool):
    """Obtains the details of a campaign using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for campaign in data.get("campaigns", []):
            if campaign.get("name") == name:
                payload = campaign
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign '{name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCampaignByName",
                "description": "Find a specific campaign by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the campaign.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
