from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCampaignDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str, type: Any = None) -> str:
        c = next(
            (x for x in data.get("campaigns", {}).values() if x.get("campaign_id") == campaign_id), None
        )
        if not c:
            payload = {"error": f"campaign_id {campaign_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCampaignDetails",
                "description": "Fetch a campaign row by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "integer"}},
                    "required": ["campaign_id"],
                },
            },
        }
