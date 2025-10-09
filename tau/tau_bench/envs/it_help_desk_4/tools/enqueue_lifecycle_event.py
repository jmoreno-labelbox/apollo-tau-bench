from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnqueueLifecycleEvent(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        lifecycle_id: str,
        memo_id: str,
        employee_ref: str,
        event: str,
        status: str,
        created_at: str,
    ) -> str:
        row = {
            "lifecycle_id": lifecycle_id,
            "memo_id": memo_id,
            "employee_ref": employee_ref,
            "event": event,
            "status": status,
            "created_at": created_at,
        }
        _append_row(data["lifecycle_queue"], row)
        _append_row(
            data["lifecycle_audit"],
            {
                "audit_id": f"lcaud_{lifecycle_id}_created",
                "lifecycle_id": lifecycle_id,
                "event": f"{event}_created",
                "timestamp": created_at,
                "actor": "system_policy",
            },
        )
        payload = {"status": "ok", "lifecycle": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnqueueLifecycleEvent",
                "description": "Append a lifecycle_queue entry and a created audit record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "memo_id": {"type": "string"},
                        "employee_ref": {"type": "string"},
                        "event": {"type": "string"},
                        "status": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "lifecycle_id",
                        "memo_id",
                        "employee_ref",
                        "event",
                        "status",
                        "created_at",
                    ],
                },
            },
        }
