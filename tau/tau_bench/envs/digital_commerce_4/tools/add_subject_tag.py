from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddSubjectTag(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, tag: str) -> str:
        subject_id = _sid(subject_id)
        payload = {"tag": tag}
        _ws_append(data, subject_id, "TAG_ADDED", payload)
        _append_audit(data, "TAG_ADDED", subject_id, payload)
        payload = {"subject_id": subject_id, "tag": tag, "ok": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSubjectTag",
                "description": "Attach a tag to the subject and stage to evidence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "tag": {"type": "string"},
                    },
                    "required": ["subject_id", "tag"],
                },
            },
        }
