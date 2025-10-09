from tau_bench.envs.tool import Tool
import json
from typing import Any

class ScheduleDeviceReturn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, asset_id: str = None) -> str:
        workflows = data.setdefault("device_workflow", [])
        workflow_id = _get_next_id(workflows, "workflow_id", "dwf")
        return_code = f"RT{workflow_id[-4:]}"
        new_workflow = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": "device_return",
            "status": "pending_return",
            "return_code": return_code,
            "created_at": FIXED_NOW,
            "completed_at": None,
        }
        workflows.append(new_workflow)
        payload = new_workflow
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scheduleDeviceReturn",
                "description": "Schedule device return for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "asset_id": {"type": "string"},
                    },
                    "required": ["employee_id", "asset_id"],
                },
            },
        }
