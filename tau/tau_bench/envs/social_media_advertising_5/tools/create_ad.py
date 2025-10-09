from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateAd(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, name: str = None, creative_type: str = None, start_date: str = None) -> str:
        ads = data.get("ads", [])
        nid = max((int(a["ad_id"]) for a in ads), default=1100) + 1
        rec = {
            "ad_id": str(nid),
            "adset_id": adset_id,
            "name": name,
            "creative_type": creative_type,
            "status": "paused",
            "start_date": start_date,
            "end_date": None,
        }
        ads.append(rec)
        data["ads"] = ads
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAd",
                "description": "Creates a paused ad in an ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "creative_type": {"type": "string"},
                        "start_date": {"type": "string"},
                    },
                    "required": ["adset_id", "name", "creative_type", "start_date"],
                },
            },
        }
