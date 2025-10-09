from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAllocationsForPlan(Tool):
    """Fetches the allocations linked to a specific plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None) -> str:
        plans = data.get("plans", [])

        for plan in plans:
            if plan.get("plan_id") == plan_id:
                payload = {"allocations": plan.get("allocations", [])}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Plan with ID '{plan_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllocationsForPlan",
                "description": "Retrieves the allocations for a specific plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The unique ID of the plan.",
                        }
                    },
                    "required": ["plan_id"],
                },
            },
        }
