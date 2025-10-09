from tau_bench.envs.tool import Tool
import json
from typing import Any

class ClassifySubjectForAudit(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject_id: str,
        fallback_bucket: str = "MISC"
    ) -> str:
        subject_id = _sid(subject_id)
        bucket = fallback_bucket
        if ":" in subject_id:
            bucket = "CACHE_ALIGNMENT_EVIDENCE"
        elif subject_id.isdigit():
            staged = _ws(data).get(subject_id, {"events": []}).get("events", [])
            if any(ev.get("event_type") == "PROCESS_RETURN" for ev in staged):
                bucket = "RETURN_EVIDENCE"
            else:
                bucket = "PRICING_EVIDENCE"
        elif subject_id.startswith("sg-"):
            bucket = "SG_EVIDENCE"
        payload = {"subject_id": subject_id, "bucket": bucket}
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "classifySubjectForAudit",
                "description": "Classify a subject_id into an audit bucket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "fallback_bucket": {"type": "string"},
                    },
                    "required": ["subject_id"],
                },
            },
        }
