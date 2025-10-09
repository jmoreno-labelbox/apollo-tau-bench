from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateLifecycleQueueStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], lifecycle_id: str = None, status: str = None) -> str:
        queue = data.get("lifecycle_queue", [])
        entry = next((e for e in queue if e.get("lifecycle_id") == lifecycle_id), None)
        if not entry:
            payload = {"error": f"Lifecycle entry {lifecycle_id} not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        entry["status"] = status
        payload = entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateLifecycleQueueStatus",
                "description": "Updates the status of an event in the lifecycle queue (e.g., to 'completed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["lifecycle_id", "status"],
                },
            },
        }
