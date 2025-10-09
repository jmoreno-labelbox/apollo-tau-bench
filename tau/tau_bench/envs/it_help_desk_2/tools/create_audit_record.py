from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAuditRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        lifecycle_id: str,
        event: str,
        details: str,
        actor: str = "SYSTEM",
        timestamp: str = FIXED_NOW
    ) -> str:
        audit_table = data.setdefault("lifecycle_audit", [])
        audit_id = _get_next_id(audit_table, "audit_id", "lcaud")
        audit_table.append(
            {
                "audit_id": audit_id,
                "lifecycle_id": lifecycle_id,
                "event": event,
                "details": details,
                "timestamp": timestamp,
                "actor": actor,
            }
        )
        payload = {"status": "success", "event_logged": event}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditRecord",
                "description": "Create a deterministic record in the lifecycle audit log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "event": {"type": "string"},
                        "details": {"type": "object"},
                        "actor": {"type": "string"},
                        "timestamp": {"type": "string"},
                    },
                    "required": [
                        "lifecycle_id",
                        "event",
                        "details",
                        "actor",
                        "timestamp",
                    ],
                },
            },
        }
