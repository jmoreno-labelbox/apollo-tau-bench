from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddAd(Tool):
    """Creates a new ad."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        ad_id: str = None,
        adset_id: str = None,
        name: str = None,
        creative_type: str = None,
        status: str = None,
        start_date: str = None,
        end_date: str = None
    ) -> str:
        if not ad_id:
            payload = {"error": "ad_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not name:
            payload = {"error": "name is a required parameter."}
            out = json.dumps(payload)
            return out
        if not creative_type:
            payload = {"error": "creative_type is a required parameter."}
            out = json.dumps(payload)
            return out
        if not status:
            payload = {"error": "status is a required parameter."}
            out = json.dumps(payload)
            return out
        if not start_date:
            payload = {"error": "start_date is a required parameter."}
            out = json.dumps(payload)
            return out

        new_ad = {
            "ad_id": ad_id,
            "adset_id": adset_id,
            "name": name,
            "creative_type": creative_type,
            "status": status,
            "start_date": start_date,
            "end_date": end_date,
        }
        data["ads"] += [new_ad]
        payload = {
            "status": "success",
            "message": f"New ad was added: {new_ad}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addAd",
                "description": "Adds a new ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the new ad.",
                        },
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set this ad belongs to.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the ad.",
                        },
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type (e.g., image, video, carousel).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the ad (e.g., active, paused, archived).",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the ad (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the ad (YYYY-MM-DD format, optional).",
                        },
                    },
                    "required": [
                        "ad_id",
                        "adset_id",
                        "name",
                        "creative_type",
                        "status",
                        "start_date",
                    ],
                },
            },
        }
