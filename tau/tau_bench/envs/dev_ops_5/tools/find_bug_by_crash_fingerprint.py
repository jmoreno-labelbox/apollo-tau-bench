from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindBugByCrashFingerprint(Tool):
    """Locates a bug/work item linked to a crash fingerprint."""

    @staticmethod
    def invoke(data: dict[str, Any], crash_fingerprint: str = None) -> str:
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("metadata", {}).get("crash_fingerprint") == crash_fingerprint:
                payload = item
                out = json.dumps(payload)
                return out
        payload = {"info": f"No bug found for crash fingerprint '{crash_fingerprint}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindBugByCrashFingerprint",
                "description": "Finds a bug associated with a crash fingerprint.",
                "parameters": {
                    "type": "object",
                    "properties": {"crash_fingerprint": {"type": "string"}},
                    "required": ["crash_fingerprint"],
                },
            },
        }
