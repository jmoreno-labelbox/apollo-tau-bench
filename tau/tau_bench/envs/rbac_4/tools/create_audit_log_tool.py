# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAuditLogTool(Tool):
    """Create an immutable, deterministic audit log entry."""

    @staticmethod
    def invoke(data: Dict[str, Any], action_type, actor_id, details, target_id, timestamp) -> str:

        # Create log_id in a deterministic manner (e.g., using a sequence or hashing input values).
        logs = data.get("audit_logs", [])
        next_id = f"L-{len(logs) + 1:03d}"

        log = {
            "log_id": next_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": timestamp,
            "details": details
        }
        logs.append(log)
        data["audit_logs"] = logs
        return json.dumps(log, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_audit_log",
                "description": "Create a deterministic, immutable audit log entry in the audit_logs table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "string",
                            "description": "User ID performing the action"
                        },
                        "action_type": {
                            "type": "string",
                            "description": "Type of action performed (e.g. ROLE_REVOKED, ACCESS_GRANTED, POLICY_EXCEPTION_REQUESTED)"
                        },
                        "target_id": {
                            "type": "string",
                            "description": "ID of the affected entity (role, resource, user, or policy exception ID)"
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Deterministic ISO8601 UTC timestamp"
                        },
                        "details": {
                            "type": "string",
                            "description": "Deterministic, canonical event description"
                        }
                    },
                    "required": [
                        "actor_id",
                        "action_type",
                        "target_id",
                        "timestamp",
                        "details"
                    ]
                }
            }
        }
