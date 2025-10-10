# Copyright held by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetRecurringSchedules(Tool):
    """Get recurring scheduled payments by type."""

    @staticmethod
    def invoke(data: Dict[str, Any], schedule_type, active_only = True) -> str:

        schedules = data.get("recurring_schedules", [])

        if schedule_type:
            schedules = _find_all(schedules, "schedule_type", schedule_type)

        if active_only:
            schedules = [sch for sch in schedules if sch.get("is_active", True)]

        return json.dumps(schedules)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_recurring_schedules",
                "description": "Get recurring scheduled payments, optionally filtered by type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "schedule_type": {"type": "string"},
                        "active_only": {"type": "boolean", "default": True}
                    },
                    "required": [],
                },
            },
        }
