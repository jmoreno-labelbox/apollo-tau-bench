from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindCrashesByCrashFingerprint(Tool):
    """Locates all crash events that correspond to a specific crash fingerprint."""

    @staticmethod
    def invoke(data: dict[str, Any], crash_fingerprint: str = None) -> str:
        crash_events = data.get("crash_events", [])

        matching_crashes = [
            crash
            for crash in crash_events
            if crash.get("crash_fingerprint") == crash_fingerprint
        ]
        payload = {"crashes": matching_crashes}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCrashesByCrashFingerprint",
                "description": "Finds all crash events that match a specific crash fingerprint.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crash_fingerprint": {
                            "type": "string",
                            "description": "The unique fingerprint identifier of the crash to search for.",
                        }
                    },
                    "required": ["crash_fingerprint"],
                },
            },
        }
