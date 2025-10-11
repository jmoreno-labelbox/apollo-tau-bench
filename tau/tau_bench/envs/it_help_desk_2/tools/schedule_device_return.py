# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_next_id(table: List[Dict[str, Any]], key: str, prefix: str) -> str:
    if not table:
        return f"{prefix}_00001"
    max_id = 0
    for item in table:
        try:
            num = int(item[key].split('_')[-1])
            if num > max_id:
                max_id = num
        except (ValueError, IndexError):
            continue
    return f"{prefix}_{max_id + 1:05d}"

class ScheduleDeviceReturn(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id, employee_id) -> str:
        workflows = data.setdefault("device_workflow", [])
        workflow_id = _get_next_id(workflows, "workflow_id", "dwf")
        return_code = f"RT{workflow_id[-4:]}"
        new_workflow = {"workflow_id": workflow_id, "employee_id": employee_id, "asset_id": asset_id, "process": "device_return", "status": "pending_return", "return_code": return_code, "created_at": FIXED_NOW, "completed_at": None}
        workflows.append(new_workflow)
        return json.dumps(new_workflow, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "schedule_device_return", "description": "Schedule device return for an employee.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "asset_id": {"type": "string"}}, "required": ["employee_id", "asset_id"]}}}