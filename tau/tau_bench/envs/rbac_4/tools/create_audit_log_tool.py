from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateAuditLogTool(Tool):
    """Generate a permanent, predictable audit log entry."""

    @staticmethod
    def invoke(data: dict[str, Any], actor_id: str = None, action_type: str = None, target_id: str = None, timestamp: str = None, details: str = None,
    target_ref: Any = None,
    ) -> str:
        pass
        # Mandatory fields
        # Create log_id in a deterministic manner (e.g., sequentially or by hashing inputs)
        logs = data.get("audit_logs", {}).values()
        next_id = f"L-{len(logs) + 1:03d}"

        log = {
            "log_id": next_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": timestamp,
            "details": details,
        }
        data["audit_logs"][log["audit_log_id"]] = log
        data["audit_logs"] = logs
        payload = log
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditLog",
                "description": "Create a deterministic, immutable audit log entry in the audit_logs table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "string",
                            "description": "User ID performing the action",
                        },
                        "action_type": {
                            "type": "string",
                            "description": "Type of action performed (e.g. ROLE_REVOKED, ACCESS_GRANTED, POLICY_EXCEPTION_REQUESTED)",
                        },
                        "target_id": {
                            "type": "string",
                            "description": "ID of the affected entity (role, resource, user, or policy exception ID)",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Deterministic ISO8601 UTC timestamp",
                        },
                        "details": {
                            "type": "string",
                            "description": "Deterministic, canonical event description",
                        },
                    },
                    "required": [
                        "actor_id",
                        "action_type",
                        "target_id",
                        "timestamp",
                        "details",
                    ],
                },
            },
        }
