# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScheduleDeviceReturn(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        asset_id = kwargs.get("asset_id")
        workflows = data.setdefault("device_workflow", [])
        workflow_id = _get_next_id(workflows, "workflow_id", "dwf")
        return_code = f"RT{workflow_id[-4:]}"
        new_workflow = {"workflow_id": workflow_id, "employee_id": employee_id, "asset_id": asset_id, "process": "device_return", "status": "pending_return", "return_code": return_code, "created_at": FIXED_NOW, "completed_at": None}
        workflows.append(new_workflow)
        return json.dumps(new_workflow, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "schedule_device_return", "description": "Schedule device return for an employee.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "asset_id": {"type": "string"}}, "required": ["employee_id", "asset_id"]}}}
