from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateCrashEventStatus(Tool):
    """Modifies the status of a crash event."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crash_id: str = None,
        id: Any = None,
        new_status: str = None,
        status: str = None
    ) -> str:
        # Support 'status' as an alternative to 'new_status'
        if status is not None:
            new_status = status
        crashes = data.get("crash_events", {}).values()
        for crash in crashes.values():
            if crash.get("id") == crash_id:
                crash["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Status for crash '{crash_id}' updated to '{new_status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Crash with ID '{crash_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrashEventStatus",
                "description": "Updates the status of a crash event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["id", "status"],
                },
            },
        }
