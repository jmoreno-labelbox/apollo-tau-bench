from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateDeviceWorkflow(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        asset_id: str = None,
        process: str = None,
        workflow_id: str = None,
        status: str = None,
        pickup_code: str = None,
        created_at: str = FIXED_NOW,
        completed_at: str = None
    ) -> str:
        if status is None:
            status = "pending_pickup" if process == "onboarding" else "pending_return"

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
            "completed_at": completed_at,
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
                "name": "CreateDeviceWorkflow",
                "description": "Create a device workflow entry for provisioning and pickup or for return.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "asset_id": {"type": "string"},
                        "process": {"type": "string"},
                    },
                    "required": ["employee_id", "asset_id", "process"],
                },
            },
        }
