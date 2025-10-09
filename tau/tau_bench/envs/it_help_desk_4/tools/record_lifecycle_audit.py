from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordLifecycleAudit(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], lifecycle_id: str, event: str, timestamp: str, actor: str
    ) -> str:
        row = {
            "audit_id": f"lcaud_{lifecycle_id}_{event}",
            "lifecycle_id": lifecycle_id,
            "event": event,
            "timestamp": timestamp,
            "actor": actor,
        }
        _append_row(data["lifecycle_audit"], row)
        payload = {"status": "ok", "audit": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordLifecycleAudit",
                "description": "Append a lifecycle_audit record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "event": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "actor": {"type": "string"},
                    },
                    "required": ["lifecycle_id", "event", "timestamp", "actor"],
                },
            },
        }
