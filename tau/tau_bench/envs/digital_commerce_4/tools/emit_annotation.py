from tau_bench.envs.tool import Tool
import json
from typing import Any

class EmitAnnotation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, note: str) -> str:
        subject_id = _sid(subject_id)
        payload = {"note": note}
        _append_audit(data, "ANNOTATION", subject_id, {"note": note})
        _ws_append(data, subject_id, "ANNOTATION", payload)
        payload = {"subject_id": subject_id, "note": note}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EmitAnnotation",
                "description": "Emit a freeform annotation into workspace evidence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["subject_id", "note"],
                },
            },
        }
