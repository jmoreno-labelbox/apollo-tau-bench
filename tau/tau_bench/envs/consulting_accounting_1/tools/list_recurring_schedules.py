# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRecurringSchedules(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], horizon_months = 3) -> str:
        horizon = int(horizon_months)
        schedules = [s for s in list(data.get("recurring_schedules", {}).values()) if s.get("is_active", False)]
        return json.dumps({"horizon_months": horizon,"active_schedules": schedules}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "list_recurring_schedules","description": "List active recurring schedules considered for the forecast horizon.","parameters": {"type": "object","properties": {"horizon_months": {"type": "integer"}}}}}
