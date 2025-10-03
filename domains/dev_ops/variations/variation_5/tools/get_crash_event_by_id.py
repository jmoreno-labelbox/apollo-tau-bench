from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCrashEventById(Tool):
    """Fetches a crash event using its ID."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crash_id: str = None,
        id: Any = None
    ) -> str:
        crashes = data.get("crash_events", [])
        for crash in crashes:
            if crash.get("id") == crash_id:
                payload = crash
                out = json.dumps(payload)
                return out
        payload = {"error": f"Crash event with ID '{crash_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrashEventById",
                "description": "Retrieves a crash event by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
