from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateAuditType(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        new_audit_type: str = None,
        updated_by: str = None,
        status: str = "RUNNING",
        notes: str = "",
        updated_ts: str = "2024-08-23T15:00:00Z"
    ) -> str:
        """
        Modifies the audit type and related metadata.
        """
        if not all([audit_id, new_audit_type]):
            payload = {"error": "audit_id and new_audit_type are required."}
            out = json.dumps(payload)
            return out

        payload = {
            "status": "SUCCESS",
            "audit_id": audit_id,
            "previous_audit_type": "A11Y",
            "new_audit_type": new_audit_type,
            "status": status,
            "updated_by": updated_by,
            "notes": notes,
            "updated_ts": updated_ts,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditType",
                "description": "Updates the audit type and associated metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to update.",
                        },
                        "new_audit_type": {
                            "type": "string",
                            "description": "The new audit type (A11Y, DS_MAPPING, COMBINED_DS_A11Y).",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Email of the user updating the audit type.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Optional status update (RUNNING, COMPLETED, FAILED).",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the audit type change.",
                        },
                        "updated_ts": {
                            "type": "string",
                            "description": "Timestamp of the update.",
                        },
                    },
                    "required": ["audit_id", "new_audit_type"],
                },
            },
        }
