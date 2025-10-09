from tau_bench.envs.tool import Tool
import json
from typing import Any

class LogAuditEvent(Tool):
    """Add a row to audit_logs with a deterministic timestamp; returns audit_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int = None,
        user_id: int = None,
        entity_type: str = None,
        entity_id: int = None,
        action_enum: str = None,
        payload_json: dict = {}
,
    created_at: Any = None,
    ) -> str:
        if (
            household_id is None
            or user_id is None
            or not entity_type
            or entity_id is None
            or not action_enum
        ):
            return _json_dump(
                {
                    "error": "household_id, user_id, entity_type, entity_id, action_enum are required"
                }
            )
        tbl = data.setdefault("audit_logs", [])
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": str(entity_type),
            "entity_id": int(entity_id),
            "action_enum": str(action_enum),
            "payload_json": payload_json,
            "created_at": "2025-01-03T10:00:00Z",
        }
        tbl.append(row)
        return _json_dump({"audit_id": next_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogAuditEvent",
                "description": "Append an audit log entry with a deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "entity_type": {"type": "string"},
                        "entity_id": {"type": "integer"},
                        "action_enum": {"type": "string"},
                        "payload_json": {"type": "object"},
                    },
                    "required": [
                        "household_id",
                        "user_id",
                        "entity_type",
                        "entity_id",
                        "action_enum",
                    ],
                },
            },
        }
