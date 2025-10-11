# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAuditReportStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], audit_id, new_status, report_asset_id, completion_notes = '') -> str:
        """
        Updates audit report status and manages audit completion workflow.
        """

        if not all([audit_id, new_status]):
            return json.dumps({"error": "audit_id and new_status are required."})

        # Verify status values.
        valid_statuses = ['RUNNING', 'COMPLETED', 'FAILED', 'CANCELLED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        audits = data.get('audits', [])

        # Locate the audit.
        audit_found = False
        for audit in audits:
            if audit.get('audit_id') == audit_id:
                audit_found = True
                old_status = audit.get('status')

                # Revise audit status
                audit['status'] = new_status
                audit['last_updated'] = datetime.now().isoformat()

                # Manage logic based on status conditions.
                if new_status == 'COMPLETED':
                    audit['completed_at'] = datetime.now().isoformat()
                    if report_asset_id:
                        audit['report_asset_id_nullable'] = report_asset_id

                elif new_status == 'FAILED':
                    audit['failed_at'] = datetime.now().isoformat()
                    if completion_notes:
                        audit['failure_reason'] = completion_notes

                # Record the status update.
                if 'status_history' not in audit:
                    audit['status_history'] = []
                audit['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_at": datetime.now().isoformat(),
                    "notes": completion_notes
                })

                break

        if not audit_found:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

        return json.dumps({
            "success": True,
            "audit_id": audit_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_report_status",
                "description": "Updates audit report status and manages audit completion workflow including report asset associations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to update."},
                        "new_status": {"type": "string", "description": "The new status for the audit. Must be one of: RUNNING, COMPLETED, FAILED, CANCELLED."},
                        "report_asset_id": {"type": "string", "description": "Optional asset ID for the generated report."},
                        "completion_notes": {"type": "string", "description": "Optional notes about the completion or failure."}
                    },
                    "required": ["audit_id", "new_status"]
                }
            }
        }
