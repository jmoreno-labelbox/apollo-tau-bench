# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDeviceWorkflow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id, completed_at, employee_id, pickup_code, process, workflow_id, created_at = FIXED_NOW, status = "pending_pickup" if process == "onboarding" else "pending_return") -> str:

        workflows = data.setdefault("device_workflow", [])

        if not workflow_id:
            workflow_id = _get_next_id(workflows, "workflow_id", "dwf")
        if not pickup_code and process == "onboarding":
            pickup_code = f"PU{workflow_id[-4:]}"

        return_code = f"RT{workflow_id[-4:]}" if "offboarding" in process else None

        new_workflow = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": process,
            "status": status,
            "pickup_code": pickup_code,
            "return_code": return_code,
            "created_at": created_at,
            "completed_at": completed_at
        }
        workflows.append(new_workflow)
        return json.dumps(new_workflow, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_device_workflow", "description": "Create a device workflow entry for provisioning and pickup or for return.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "asset_id": {"type": "string"}, "process": {"type": "string"}}, "required": ["employee_id", "asset_id", "process"]}}}
