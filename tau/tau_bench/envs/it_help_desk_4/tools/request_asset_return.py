from tau_bench.envs.tool import Tool
import json
from typing import Any

class RequestAssetReturn(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        employee_id: str,
        due_ts: str,
        workflow_id: str,
    ) -> str:
        row = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": "return",
            "status": "requested",
            "pickup_code": None,
            "created_at": due_ts,
            "completed_at": None,
        }
        _append_row(data["device_workflow"], row)
        payload = {"status": "ok", "workflow": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestAssetReturn",
                "description": "Create a device return request workflow entry with due timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "due_ts": {"type": "string"},
                        "workflow_id": {"type": "string"},
                    },
                    "required": ["asset_id", "employee_id", "due_ts", "workflow_id"],
                },
            },
        }
