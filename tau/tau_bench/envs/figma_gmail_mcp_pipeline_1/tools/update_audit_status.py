from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateAuditStatus(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str, status: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(status, str) or not status:
            payload = {"error": "status must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Check the status value for validity
        allowed_statuses = ["RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
        if status not in allowed_statuses:
            payload = {"error": f"Invalid status. Allowed: {allowed_statuses}"}
            out = json.dumps(payload)
            return out

        #Retrieve audits data
        audits = data.get("audits", [])

        #Identify the audit that needs updating
        audit_to_update = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_to_update = audit
                break

        if not audit_to_update:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Modify the status
        old_status = audit_to_update.get("status")
        audit_to_update["status"] = status
        payload = {
                "updated_audit": audit_to_update,
                "old_status": old_status,
                "new_status": status,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditStatus",
                "description": "Update the status of an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status (RUNNING, COMPLETED, FAILED, CANCELLED).",
                        },
                    },
                    "required": ["audit_id", "status"],
                },
            },
        }
