from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConsolidateWorkspaceEvents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, event_types: list[str]) -> str:
        subject_id = _sid(subject_id)
        staged = _ws(data).get(subject_id, {"events": []}).get("events", [])
        filt = [e for e in staged.values() if e.get("event_type") in set(event_types)]
        # Provide only a predictable subset
        slim = [
            {
                "event_type": e.get("event_type"),
                "payload": e.get("payload"),
                "ts": e.get("ts"),
            }
            for e in filt
        ]
        payload = {"subject_id": subject_id, "events": slim}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConsolidateWorkspaceEvents",
                "description": "Return filtered staged events for a subject.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "event_types": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["subject_id", "event_types"],
                },
            },
        }
