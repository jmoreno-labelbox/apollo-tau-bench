# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCampaign(Tool):
    """Adds a new campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id, created_date, name, objective, status) -> str:

        if not campaign_id:
            return json.dumps({"error": "campaign_id is a required parameter."})
        if not name:
            return json.dumps({"error": "name is a required parameter."})
        if not objective:
            return json.dumps({"error": "objective is a required parameter."})
        if not created_date:
            return json.dumps({"error": "created_date is a required parameter."})
        if not status:
            return json.dumps({"error": "status is a required parameter."})

        new_campaign = {
            "campaign_id": campaign_id,
            "name": name,
            "objective": objective,
            "created_date": created_date,
            "status": status
        }
        data['campaigns'] += [new_campaign]

        return json.dumps(
            {
                "status": "success",
                "message": f"New campaign was added: {new_campaign}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_campaign",
                "description": "Adds a new campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the new campaign.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the campaign.",
                        },
                        "objective": {
                            "type": "string",
                            "description": "The objective of the campaign (e.g., Sales, Awareness, Traffic).",
                        },
                        "created_date": {
                            "type": "string",
                            "description": "The creation date of the campaign (YYYY-MM-DD format).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the campaign (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["campaign_id", "name", "objective", "created_date", "status"],
                },
            },
        }
