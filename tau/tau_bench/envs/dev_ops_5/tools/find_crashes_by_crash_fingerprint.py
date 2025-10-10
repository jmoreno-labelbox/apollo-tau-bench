# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCrashesByCrashFingerprint(Tool):
    """Finds all crash events that match a specific crash fingerprint."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        crash_fingerprint = kwargs.get("crash_fingerprint")
        crash_events = data.get("crash_events", [])
        
        matching_crashes = [
            crash for crash in crash_events if crash.get("crash_fingerprint") == crash_fingerprint
        ]
        
        return json.dumps({"crashes": matching_crashes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_crashes_by_crash_fingerprint",
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
