from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SearchAdSetsByCampaignId(Tool):
    """Looks for ad sets that are part of a specific campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []

        for adset in adsets:
            if adset.get("campaign_id") == campaign_id:
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByCampaignId",
                "description": "Searches for ad sets belonging to a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The campaign ID to search for ad sets.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }
