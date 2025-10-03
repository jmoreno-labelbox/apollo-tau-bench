from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddMemoToLifecycleQueue(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], memo_id: str = None, hr_id: str = None, event_type: str = None) -> str:
        queue = data.setdefault("lifecycle_queue", [])
        lifecycle_id = _get_next_id(queue, "lifecycle_id", "lcq")
        new_entry = {
            "lifecycle_id": lifecycle_id,
            "memo_id": memo_id,
            "employee_ref": hr_id,
            "event": event_type,
            "status": "queued",
            "created_at": FIXED_NOW,
        }
        queue.append(new_entry)
        payload = new_entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMemoToLifecycleQueue",
                "description": "Adds a new memo to the lifecycle queue to initiate a process like onboarding or offboarding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "memo_id": {"type": "string"},
                        "hr_id": {"type": "string"},
                        "event_type": {"type": "string"},
                    },
                    "required": ["memo_id", "hr_id", "event_type"],
                },
            },
        }
