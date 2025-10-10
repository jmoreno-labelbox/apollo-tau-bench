# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindBugByCrashFingerprint(Tool):
    """Finds a bug/work item associated with a crash fingerprint."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        fingerprint = kwargs.get("crash_fingerprint")
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("metadata", {}).get("crash_fingerprint") == fingerprint:
                return json.dumps(item)
        return json.dumps({"info": f"No bug found for crash fingerprint '{fingerprint}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_bug_by_crash_fingerprint",
                "description": "Finds a bug associated with a crash fingerprint.",
                "parameters": {
                    "type": "object",
                    "properties": {"crash_fingerprint": {"type": "string"}},
                    "required": ["crash_fingerprint"],
                },
            },
        }
