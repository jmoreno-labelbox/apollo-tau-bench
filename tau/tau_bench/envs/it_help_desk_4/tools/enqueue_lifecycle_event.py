# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _append_row(table: List[Dict[str, Any]], row: Dict[str, Any]) -> None:
    table.append(row)

class EnqueueLifecycleEvent(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], lifecycle_id: str, memo_id: str, employee_ref: str, event: str, status: str, created_at: str
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
        return json.dumps({"status": "ok", "lifecycle": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enqueue_lifecycle_event",
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
                    "required": ["lifecycle_id", "memo_id", "employee_ref", "event", "status", "created_at"],
                },
            },
        }