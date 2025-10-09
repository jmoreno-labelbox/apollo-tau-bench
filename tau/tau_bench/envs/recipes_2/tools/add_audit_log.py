from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddAuditLog(Tool):
    """Inserts a new record into the audit logs."""

    @staticmethod
    def invoke(data: dict[str, Any], household_id: int, user_id: int, entity_type: str, entity_id: int, action_enum: str, payload_json: dict = {}) -> str:
        logs = data.get("audit_logs", [])
        # Automatically create the next audit_id
        new_id = max([log.get("audit_id", 0) for log in logs]) + 1 if logs else 12001

        new_log = {
            "audit_id": new_id,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action_enum": action_enum,
            "payload_json": payload_json,
            "created_at": "2025-08-25T11:00:05Z",  # Applying a fixed timestamp for reliability
        }
        data["audit_logs"].append(new_log)
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAuditLog",
                "description": "Adds a new entry to the audit logs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "entity_type": {
                            "type": "string",
                            "description": "The type of entity being logged (e.g., meal_plans, orders).",
                        },
                        "entity_id": {"type": "integer"},
                        "action_enum": {
                            "type": "string",
                            "description": "The action performed (e.g., create, update, delete).",
                        },
                        "payload_json": {
                            "type": "object",
                            "description": "JSON object with details about the action.",
                        },
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
