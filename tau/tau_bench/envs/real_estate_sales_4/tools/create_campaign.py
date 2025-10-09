from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateCampaign(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, campaign_type: str = None, created_by: str = None,
    type: Any = None,
    ) -> str:
        if not all([name, campaign_type, created_by]):
            payload = {"error": "name, type, and created_by are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        campaign = {
            "campaign_id": 101,
            "name": name,
            "type": campaign_type,
            "created_by": created_by,
            "status": "active",
            "created_at": "2024-08-21T00:00:00Z",
        }
        payload = {"success": True, "campaign_id": 101, "campaign": campaign}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCampaign",
                "description": "Create a marketing campaign for client outreach",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Campaign name"},
                        "type": {
                            "type": "string",
                            "description": "Campaign type (likely_buyer, general_update, etc.)",
                        },
                        "created_by": {
                            "type": "integer",
                            "description": "Broker ID creating the campaign",
                        },
                    },
                    "required": ["name", "type", "created_by"],
                },
            },
        }
