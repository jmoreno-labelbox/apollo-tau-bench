# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAuditStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], audit_id, new_status, updated_by, notes = '') -> str:
        """
        Updates the status of an audit.
        """

        if not all([audit_id, new_status, updated_by]):
            return json.dumps({"error": "audit_id, new_status, and updated_by are required"})

        # Check the validity of status values.
        valid_statuses = ['DRAFT', 'IN_PROGRESS', 'PENDING_REVIEW', 'COMPLETED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        # Locate and revise the audit.
        for audit in data.get('audits', []):
            if audit.get('audit_id') == audit_id:
                audit['status'] = new_status
                audit['last_updated'] = datetime.now().isoformat()
                audit['updated_by'] = updated_by
                if notes:
                    audit['notes'] = notes
                return json.dumps({"status": "success", "audit_id": audit_id, "new_status": new_status})

        return json.dumps({"error": f"Audit with ID {audit_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_status",
                "description": "Updates the status of an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to update."},
                        "new_status": {"type": "string", "description": "The new status for the audit."},
                        "updated_by": {"type": "string", "description": "Email of the user updating the status."},
                        "notes": {"type": "string", "description": "Optional notes about the status update."}
                    },
                    "required": ["audit_id", "new_status", "updated_by"]
                }
            }
        }
