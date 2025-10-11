# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddAuditLog(Tool):
    """Adds a new entry to the audit logs."""
    @staticmethod
    def invoke(data: Dict[str, Any], action_enum, entity_id, entity_type, household_id, user_id, payload_json = {}) -> str:
        
        logs = data.get("audit_logs", [])
        # Auto-generate the subsequent audit_id.
        new_id = max([log.get("audit_id", 0) for log in logs]) + 1 if logs else 12001

        new_log = {
            "audit_id": new_id,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action_enum": action_enum,
            "payload_json": payload_json,
            "created_at": "2025-08-25T11:00:05Z" # Employing a static timestamp for uniformity.
        }
        data["audit_logs"].append(new_log)
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_audit_log",
                "description": "Adds a new entry to the audit logs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "entity_type": {"type": "string", "description": "The type of entity being logged (e.g., meal_plans, orders)."},
                        "entity_id": {"type": "integer"},
                        "action_enum": {"type": "string", "description": "The action performed (e.g., create, update, delete)."},
                        "payload_json": {"type": "object", "description": "JSON object with details about the action."},
                    },
                    "required": ["household_id", "user_id", "entity_type", "entity_id", "action_enum"],
                },
            },
        }
