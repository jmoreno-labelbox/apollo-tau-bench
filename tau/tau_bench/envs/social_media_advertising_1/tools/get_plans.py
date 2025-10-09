from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPlans(Tool):
    """Fetches all IDs of plans."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        plans = data.get("plans", {}).values()
        ids_ = []
        for i in plans:
            ids_ += [i.get("plan_id")]
        payload = {"plan_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlans",
                "description": "Retrieves all plan IDs.",
                "parameters": {},
            },
        }
