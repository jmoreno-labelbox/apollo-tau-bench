from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReadCampaign(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, type: Any = None) -> str:
        cid = campaign_id
        c = next(
            (x for x in data.get("campaigns", []) if x.get("campaign_id") == cid), None
        )
        if not c:
            payload = {"error": f"campaign_id {cid} not found"}
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
                "name": "ReadCampaign",
                "description": "Fetch a campaign row by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "integer"}},
                    "required": ["campaign_id"],
                },
            },
        }
