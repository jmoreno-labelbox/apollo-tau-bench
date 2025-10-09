from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateAd(Tool):
    """Initiates a new ad creative."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, name: str = None, creative_type: str = None, status: str = None, request_id: str = None) -> str:
        ads = data.get("ads", {}).values()
        new_id = max((int(a["ad_id"]) for a in ads.values()), default=1100) + 1
        new_ad = {
            "ad_id": str(new_id),
            "adset_id": adset_id,
            "name": name,
            "creative_type": creative_type,
            "status": status if status is not None else "paused",
            "start_date": "2025-08-15",
            "end_date": None,
        }
        data["ads"][ad_id] = new_ad
        data["ads"] = ads
        payload = new_ad
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAd",
                "description": "Creates a new ad within a specified ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "creative_type": {"type": "string"},
                    },
                    "required": ["adset_id", "name", "creative_type"],
                },
            },
        }
