from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateDeviceWorkflow(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        workflow_id: str,
        employee_id: str,
        asset_id: str,
        process: str,
        status: str,
        pickup_code: str | None,
        created_at: str,
        completed_at: str | None = None,
    ) -> str:
        pass
        row = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": process,
            "status": status,
            "pickup_code": pickup_code,
            "created_at": created_at,
            "completed_at": completed_at,
        }
        _append_row(data["device_workflow"], row)
        payload = {"status": "ok", "workflow": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDeviceWorkflow",
                "description": "Create a device workflow record (e.g., provisioning or return).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "asset_id": {"type": "string"},
                        "process": {"type": "string"},
                        "status": {"type": "string"},
                        "pickup_code": {"type": "string"},
                        "created_at": {"type": "string"},
                        "completed_at": {"type": "string"},
                    },
                    "required": [
                        "workflow_id",
                        "employee_id",
                        "asset_id",
                        "process",
                        "status",
                        "created_at",
                    ],
                },
            },
        }
