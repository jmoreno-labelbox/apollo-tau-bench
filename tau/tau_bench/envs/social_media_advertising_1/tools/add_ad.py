# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddAd(Tool):
    """Adds a new ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        adset_id = kwargs.get("adset_id")
        name = kwargs.get("name")
        creative_type = kwargs.get("creative_type")
        status = kwargs.get("status")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")

        if not ad_id:
            return json.dumps({"error": "ad_id is a required parameter."})
        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})
        if not name:
            return json.dumps({"error": "name is a required parameter."})
        if not creative_type:
            return json.dumps({"error": "creative_type is a required parameter."})
        if not status:
            return json.dumps({"error": "status is a required parameter."})
        if not start_date:
            return json.dumps({"error": "start_date is a required parameter."})

        new_ad = {
            "ad_id": ad_id,
            "adset_id": adset_id,
            "name": name,
            "creative_type": creative_type,
            "status": status,
            "start_date": start_date,
            "end_date": end_date
        }
        data['ads'] += [new_ad]

        return json.dumps(
            {
                "status": "success",
                "message": f"New ad was added: {new_ad}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_ad",
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
                        }
                    },
                    "required": ["ad_id", "adset_id", "name", "creative_type", "status", "start_date"],
                },
            },
        }
