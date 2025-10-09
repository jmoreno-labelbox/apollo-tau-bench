from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAuditProgress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        progress_percentage: int,
        notes: str = "",
        updated_by: str = None
    ) -> str:
        """
        Modifies audit progress and the percentage of completion.
        """
        if not all([audit_id, progress_percentage is not None]):
            payload = {"error": "audit_id and progress_percentage are required."}
            out = json.dumps(payload)
            return out

        if not (0 <= progress_percentage <= 100):
            payload = {"error": "progress_percentage must be between 0 and 100."}
            out = json.dumps(payload)
            return out

        audits = data.get("audits", {}).values()
        audit_found = False

        for audit in audits.values():
            if audit.get("audit_id") == audit_id:
                audit_found = True
                old_progress = audit.get("progress_percentage", 0)

                # Modify the progress of the audit
                audit["progress_percentage"] = progress_percentage
                audit["last_updated"] = datetime.now().isoformat()

                if updated_by:
                    audit["updated_by"] = updated_by
                if notes:
                    audit["progress_notes"] = notes

                # Automatically modify status according to progress
                if progress_percentage == 100 and audit.get("status") == "RUNNING":
                    audit["status"] = "COMPLETED"
                    audit["completed_at"] = datetime.now().isoformat()
                elif progress_percentage > 0 and audit.get("status") not in [
                    "RUNNING",
                    "COMPLETED",
                ]:
                    audit["status"] = "RUNNING"

                # Include history of progress changes
                if "progress_history" not in audit:
                    audit["progress_history"] = []
                audit["progress_history"].append(
                    {
                        "from_progress": old_progress,
                        "to_progress": progress_percentage,
                        "changed_by": updated_by,
                        "changed_at": datetime.now().isoformat(),
                        "notes": notes,
                    }
                )

                break

        if not audit_found:
            payload = {"error": f"Audit with ID '{audit_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "audit_id": audit_id,
            "old_progress": old_progress,
            "new_progress": progress_percentage,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditProgress",
                "description": "Updates audit progress percentage and automatically manages status transitions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update.",
                        },
                        "progress_percentage": {
                            "type": "number",
                            "description": "Progress percentage (0-100).",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the progress update.",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Optional email of person updating the audit.",
                        },
                    },
                    "required": ["audit_id", "progress_percentage"],
                },
            },
        }
