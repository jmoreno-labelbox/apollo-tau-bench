from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateAuditStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, new_status: str = None, updated_by: str = None, notes: str = "") -> str:
        """
        Modifies the status of an audit.
        """
        if not all([audit_id, new_status, updated_by]):
            payload = {"error": "audit_id, new_status, and updated_by are required"}
            out = json.dumps(payload)
            return out

        # Check the validity of status values
        valid_statuses = [
            "DRAFT",
            "IN_PROGRESS",
            "PENDING_REVIEW",
            "COMPLETED",
            "ARCHIVED",
        ]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        # Locate and modify the audit
        for audit in data.get("audits", []):
            if audit.get("audit_id") == audit_id:
                audit["status"] = new_status
                audit["last_updated"] = datetime.now().isoformat()
                audit["updated_by"] = updated_by
                if notes:
                    audit["notes"] = notes
                payload = {
                    "status": "success",
                    "audit_id": audit_id,
                    "new_status": new_status,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Audit with ID {audit_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditStatus",
                "description": "Updates the status of an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the audit.",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Email of the user updating the status.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the status update.",
                        },
                    },
                    "required": ["audit_id", "new_status", "updated_by"],
                },
            },
        }
