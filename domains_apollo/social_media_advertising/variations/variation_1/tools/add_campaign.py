from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddCampaign(Tool):
    """Creates a new campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, name: str = None, objective: str = None, created_date: str = None, status: str = None) -> str:
        if not campaign_id:
            payload = {"error": "campaign_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not name:
            payload = {"error": "name is a required parameter."}
            out = json.dumps(payload)
            return out
        if not objective:
            payload = {"error": "objective is a required parameter."}
            out = json.dumps(payload)
            return out
        if not created_date:
            payload = {"error": "created_date is a required parameter."}
            out = json.dumps(payload)
            return out
        if not status:
            payload = {"error": "status is a required parameter."}
            out = json.dumps(payload)
            return out

        new_campaign = {
            "campaign_id": campaign_id,
            "name": name,
            "objective": objective,
            "created_date": created_date,
            "status": status,
        }
        data["campaigns"] += [new_campaign]
        payload = {
                "status": "success",
                "message": f"New campaign was added: {new_campaign}",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCampaign",
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
                        },
                    },
                    "required": [
                        "campaign_id",
                        "name",
                        "objective",
                        "created_date",
                        "status",
                    ],
                },
            },
        }
