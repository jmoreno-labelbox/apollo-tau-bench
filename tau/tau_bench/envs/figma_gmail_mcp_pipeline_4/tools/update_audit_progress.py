# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAuditProgress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], audit_id, progress_percentage, updated_by, notes = '') -> str:
        """
        Updates audit progress and completion percentage.
        """

        if not all([audit_id, progress_percentage is not None]):
            return json.dumps({"error": "audit_id and progress_percentage are required."})

        if not (0 <= progress_percentage <= 100):
            return json.dumps({"error": "progress_percentage must be between 0 and 100."})

        audits = data.get('audits', [])
        audit_found = False

        for audit in audits:
            if audit.get('audit_id') == audit_id:
                audit_found = True
                old_progress = audit.get('progress_percentage', 0)

                # Revise audit status
                audit['progress_percentage'] = progress_percentage
                audit['last_updated'] = datetime.now().isoformat()

                if updated_by:
                    audit['updated_by'] = updated_by
                if notes:
                    audit['progress_notes'] = notes

                # Automatically refresh status according to progress.
                if progress_percentage == 100 and audit.get('status') == 'RUNNING':
                    audit['status'] = 'COMPLETED'
                    audit['completed_at'] = datetime.now().isoformat()
                elif progress_percentage > 0 and audit.get('status') not in ['RUNNING', 'COMPLETED']:
                    audit['status'] = 'RUNNING'

                # Include progress tracking history.
                if 'progress_history' not in audit:
                    audit['progress_history'] = []
                audit['progress_history'].append({
                    "from_progress": old_progress,
                    "to_progress": progress_percentage,
                    "changed_by": updated_by,
                    "changed_at": datetime.now().isoformat(),
                    "notes": notes
                })

                break

        if not audit_found:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

        return json.dumps({
            "success": True,
            "audit_id": audit_id,
            "old_progress": old_progress,
            "new_progress": progress_percentage,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_progress",
                "description": "Updates audit progress percentage and automatically manages status transitions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to update."},
                        "progress_percentage": {"type": "number", "description": "Progress percentage (0-100)."},
                        "notes": {"type": "string", "description": "Optional notes about the progress update."},
                        "updated_by": {"type": "string", "description": "Optional email of person updating the audit."}
                    },
                    "required": ["audit_id", "progress_percentage"]
                }
            }
        }
