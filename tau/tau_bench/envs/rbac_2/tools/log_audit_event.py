# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogAuditEvent(Tool):
    """ Recording actions or events in the system's audit log used for security, compliance, and traceability."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
           audit_logs = data.get('audit_logs', [])
        except (KeyError, json.JSONDecodeError):
            audit_logs = []
        existing_ids = [int(log["log_id"].replace("L-", "")) for log in audit_logs if log.get("log_id", "").startswith("L-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        log_id = f"L-{next_id_num:03d}"

        new_log = {
            "log_id": log_id,
            "actor_id": kwargs.get("actor_id"),
            "action_type": kwargs.get("action_type"),
            "target_id": kwargs.get("target_id"),
            "timestamp": kwargs.get("timestamp"),
            "details": kwargs.get("details")
        }

        audit_logs.append(new_log)
        data["audit_logs.json"] = json.dumps(audit_logs, indent=4)

        return json.dumps({
            "message": "Audit event logged successfully.",
            "log_details": new_log
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_audit_event",
                "description": "Records an action in the system's audit log for compliance and tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "string",
                            "description": "The user ID of the user who performed the action."
                        },
                        "action_type": {
                            "type": "string",
                            "description": "The type of action being logged (e.g., USER_CREATED, ROLE_ASSIGNED, ACCESS_GRANTED)."
                        },
                        "target_id": {
                            "type": "string",
                            "description": "The ID of the entity that was the target of the action (e.g., a user_id, role_id, or request_id)."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of the event, in ISO 8601 format."
                        },
                        "details": {
                            "type": "string",
                            "description": "A human-readable summary of the event."
                        }
                    },
                    "required": ["actor_id", "action_type", "target_id", "timestamp", "details"]
                }
            }
        }
