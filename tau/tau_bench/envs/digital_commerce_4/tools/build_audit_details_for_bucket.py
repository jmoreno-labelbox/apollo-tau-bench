from tau_bench.envs.tool import Tool
import json
from typing import Any

class BuildAuditDetailsForBucket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, bucket: str) -> str:
        subject_id = _sid(subject_id)
        staged = _ws(data).get(subject_id, {"events": []}).get("events", [])
        try:
            from .rules import build_audit_details as _build

            details = _build(bucket=bucket, subject_id=subject_id, staged_events=staged)
        except Exception:
            details = {"bucket": bucket, "subject_id": subject_id, "events": staged}
        payload = details
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildAuditDetailsForBucket",
                "description": "Build deterministic details for create_audit_record based on bucket rules in rules.py.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "bucket": {"type": "string"},
                    },
                    "required": ["subject_id", "bucket"],
                },
            },
        }
