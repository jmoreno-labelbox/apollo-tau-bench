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

class GetAdsetAllocationFromPlan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, adset_id: str = None) -> str:
        for p in data.get("plans", {}).values():
            if p.get("plan_id") == plan_id:
                for a in p.get("allocations", []):
                    if a.get("adset_id") == adset_id:
                        payload = a
                        out = json.dumps(payload)
                        return out
        payload = {"error": f"allocation for {adset_id} not in {plan_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetAllocationFromPlan",
                "description": "Gets one ad set allocation from a plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "adset_id": {"type": "string"},
                    },
                    "required": ["plan_id", "adset_id"],
                },
            },
        }
