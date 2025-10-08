from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CreateCampaign(Tool):
    """Initiates a new advertising campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, objective: str = None) -> str:
        campaigns = data.get("campaigns", [])
        new_id = max((int(c["campaign_id"]) for c in campaigns), default=0) + 1
        new_campaign = {
            "campaign_id": str(new_id),
            "name": name,
            "objective": objective,
            "created_date": "2025-08-15",
            "status": "paused",
        }
        campaigns.append(new_campaign)
        data["campaigns"] = campaigns
        payload = new_campaign
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCampaign",
                "description": "Creates a new advertising campaign. New campaigns always start with a 'paused' status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "objective": {"type": "string"},
                    },
                    "required": ["name", "objective"],
                },
            },
        }
