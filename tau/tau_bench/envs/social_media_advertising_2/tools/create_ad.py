from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateAd(Tool):
    """Establish a new ad within an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, name: str = None, format: str = None, status: str = None, request_id: str = None) -> str:
        ads = data.get("ads", {}).values()
        new_id = str(max((int(a["ad_id"]) for a in ads.values()), default=1000) + 1)
        ad = {
            "ad_id": new_id,
            "adset_id": adset_id,
            "name": name,
            "format": format,
            "status": status if status is not None else "paused",
        }
        data["ads"][ad_id] = ad
        data["ads"] = ads
        payload = ad
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAd",
                "description": "Create a new ad in a given adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "format": {"type": "string"},
                    },
                    "required": ["adset_id", "name", "format"],
                },
            },
        }
