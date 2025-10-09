from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateAuditFindingStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        finding_id: str,
        new_status: str,
        notes: str = "",
        updated_by: str = None
    ) -> str:
        """
        Modifies the status of an audit finding.
        """
        if not all([finding_id, new_status]):
            payload = {"error": "finding_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Acceptable statuses for audit findings
        valid_statuses = ["OPEN", "IN_PROGRESS", "RESOLVED", "DEFERRED", "VERIFIED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        # Examine both design system and accessibility findings
        finding_found = False
        old_status = None
        finding_type = None

        for dataset_name in ["audit_findings_ds", "audit_findings_a11y"]:
            findings = data.get(dataset_name, [])
            for finding in findings:
                if finding.get("finding_id") == finding_id:
                    finding_found = True
                    old_status = finding.get("status", "OPEN")
                    finding_type = dataset_name

                    # Modify the finding
                    finding["status"] = new_status
                    finding["last_updated"] = datetime.now().isoformat()

                    if updated_by:
                        finding["updated_by"] = updated_by
                    if notes:
                        finding["resolution_notes"] = notes

                    # Include history of status changes
                    if "status_history" not in finding:
                        finding["status_history"] = []
                    finding["status_history"].append(
                        {
                            "from_status": old_status,
                            "to_status": new_status,
                            "changed_by": updated_by,
                            "changed_at": datetime.now().isoformat(),
                            "notes": notes,
                        }
                    )

                    break
            if finding_found:
                break

        if not finding_found:
            payload = {"error": f"Audit finding with ID '{finding_id}' not found."}
            out = json.dumps(payload)
            return out

        payload = {
            "success": True,
            "finding_id": finding_id,
            "finding_type": finding_type,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditFindingStatus",
                "description": "Updates the status of an audit finding (design system or accessibility).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_id": {
                            "type": "string",
                            "description": "The ID of the audit finding to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status (OPEN, IN_PROGRESS, RESOLVED, DEFERRED, VERIFIED).",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the status change.",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Optional email of person updating the finding.",
                        },
                    },
                    "required": ["finding_id", "new_status"],
                },
            },
        }
