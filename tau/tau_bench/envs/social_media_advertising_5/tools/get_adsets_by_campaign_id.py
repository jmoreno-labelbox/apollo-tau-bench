from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAdsetsByCampaignID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        rows = [r for r in data.get("adsets", {}).values() if r.get("campaign_id") == campaign_id]
        payload = {"adsets": rows}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetsByCampaignId",
                "description": "Lists ad sets for a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }
