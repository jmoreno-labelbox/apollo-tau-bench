from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListRecurringSchedules(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], horizon_months: int = 3) -> str:
        horizon = int(horizon_months)
        schedules = [
            s for s in data.get("recurring_schedules", []) if s.get("is_active", False)
        ]
        payload = {"horizon_months": horizon, "active_schedules": schedules}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRecurringSchedules",
                "description": "List active recurring schedules considered for the forecast horizon.",
                "parameters": {
                    "type": "object",
                    "properties": {"horizon_months": {"type": "integer"}},
                },
            },
        }
