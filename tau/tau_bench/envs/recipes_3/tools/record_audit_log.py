from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordAuditLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        user_id: int,
        entity_type: str,
        entity_id: int,
        action_enum: str,
        payload_json: dict[str, Any]
    ) -> str:
        table = _get_table(data, "audit_logs")
        next_id = _max_int(table, "audit_id", 0) + 1
        rec = {
            "audit_id": next_id,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action_enum": action_enum,
            "payload_json": payload_json,
            "created_at": "FIXED",
        }
        table.append(rec)
        payload = {"audit_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "audit_logs")
        next_id = _max_int(table, "audit_id", 0) + 1
        rec = {
            "audit_id": next_id,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action_enum": action_enum,
            "payload_json": payload_json,
            "created_at": "FIXED",
        }
        table.append(rec)
        payload = {"audit_id": next_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAuditLog",
                "description": "Appends an audit log entry with next audit_id.",
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
                        "payload_json",
                    ],
                },
            },
        }
