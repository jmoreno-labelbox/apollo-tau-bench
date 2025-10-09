from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2GetRecurringSchedules(Tool):
    """Retrieve recurring scheduled payments categorized by type."""

    @staticmethod
    def invoke(data: dict[str, Any], schedule_type: str = None, active_only: bool = True) -> str:
        schedules = data.get("recurring_schedules", [])

        if schedule_type:
            schedules = _find_all(schedules, "schedule_type", schedule_type)

        if active_only:
            schedules = [sch for sch in schedules if sch.get("is_active", True)]
        payload = schedules
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetRecurringSchedules",
                "description": "Get recurring scheduled payments, optionally filtered by type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "schedule_type": {"type": "string"},
                        "active_only": {"type": "boolean", "default": True},
                    },
                    "required": [],
                },
            },
        }
