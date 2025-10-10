# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAuditStatus(Tool):  # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str,
        status: str
    ) -> str:
        # Verify input data.
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})

        if not isinstance(status, str) or not status:
            return json.dumps({"error": "status must be a non-empty string"})

        # Check the validity of the status value.
        allowed_statuses = ["RUNNING", "COMPLETED", "FAILED", "CANCELLED"]
        if status not in allowed_statuses:
            return json.dumps({"error": f"Invalid status. Allowed: {allowed_statuses}"})

        # Retrieve audit information.
        audits = list(data.get("audits", {}).values())

        # Locate the audit for updating.
        audit_to_update = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_to_update = audit
                break

        if not audit_to_update:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found"})

        # Revise the status.
        old_status = audit_to_update.get("status")
        audit_to_update["status"] = status

        return json.dumps({
            "updated_audit": audit_to_update,
            "old_status": old_status,
            "new_status": status
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_status",
                "description": "Update the status of an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The audit ID to update."},
                        "status": {"type": "string", "description": "New status (RUNNING, COMPLETED, FAILED, CANCELLED)."}
                    },
                    "required": ["audit_id", "status"]
                }
            }
        }
