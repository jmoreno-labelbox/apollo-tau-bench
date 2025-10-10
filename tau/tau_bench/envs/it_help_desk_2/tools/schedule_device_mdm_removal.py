# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScheduleDeviceMDMRemoval(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id, last_day) -> str:
        return json.dumps({"asset_id": asset_id, "removal_scheduled_for": last_day, "status": "pending_removal"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "schedule_device_mdm_removal", "description": "Schedules a device for removal from MDM on a specific date.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}, "last_day": {"type": "string"}}, "required": ["asset_id", "last_day"]}}}
