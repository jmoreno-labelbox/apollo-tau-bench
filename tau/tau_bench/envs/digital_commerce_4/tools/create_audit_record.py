from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAuditRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject_id: str,
        event_type: str,
        details: dict[str, Any] | None = None,
        bucket: str | None = None
    ) -> str:
        subject_id = _sid(subject_id)
        if bucket is not None:
            bucket = _sid(bucket)
        event_type = _sid(event_type)
        staged_events = _ws(data).get(subject_id, {"events": []}).get("events", [])
        if details is None and bucket is None:
            details = {
                "summary": f"Aggregated evidence for {subject_id}",
                "events": staged_events,
            }
        if isinstance(details, dict) and "timestamp" in details:
            details = {k: v for k, v in details.items() if k != "timestamp"}
        if details is None and bucket is not None:
            details = {"bucket": bucket}

        _append_audit(data, event_type, subject_id, details)
        _ws(data).pop(subject_id, None)
        payload = {"subject_id": subject_id, "event_type": event_type}
        out = json.dumps(
            payload, indent=2
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditRecord",
                "description": "Create a single aggregated audit record for a subject. Caller must provide either details or bucket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "details": {"type": "object"},
                        "bucket": {"type": "string"},
                    },
                    "required": ["subject_id", "event_type"],
                },
            },
        }
