from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindAdsetInPlan(Tool):
    """Deliver allocation details for a single ad set from a particular plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, adset_id: str = None) -> str:
        for plan in data.get("plans", []):
            if plan.get("plan_id") == plan_id:
                for a in plan.get("allocations", []):
                    if a.get("adset_id") == adset_id:
                        payload = a
                        out = json.dumps(payload)
                        return out
        payload = {"error": f"Adset {adset_id} not in plan {plan_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAdsetInPlan",
                "description": "Return allocation info for a single ad set from a plan.",
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
