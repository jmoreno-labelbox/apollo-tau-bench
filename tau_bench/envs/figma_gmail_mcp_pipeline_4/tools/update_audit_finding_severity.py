from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateAuditFindingSeverity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], finding_id: str = None, new_severity: str = None, updated_by: str = None, notes: str = "", updated_ts: str = "2024-08-23T15:00:00Z") -> str:
        """
        Modifies the severity level of an audit finding.
        """
        if not all([finding_id, new_severity]):
            payload = {"error": "finding_id and new_severity are required."}
            out = json.dumps(payload)
            return out

        payload = {
                "status": "SUCCESS",
                "finding_id": finding_id,
                "previous_severity": "MEDIUM",
                "new_severity": new_severity,
                "updated_by": updated_by,
                "notes": notes,
                "updated_ts": updated_ts,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditFindingSeverity",
                "description": "Updates the severity level of an audit finding (DS or A11y).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_id": {
                            "type": "string",
                            "description": "The ID of the audit finding to update.",
                        },
                        "new_severity": {
                            "type": "string",
                            "description": "The new severity level (LOW, MEDIUM, HIGH, CRITICAL).",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "Email of the user updating the severity.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about the severity change.",
                        },
                        "updated_ts": {
                            "type": "string",
                            "description": "Timestamp of the update.",
                        },
                    },
                    "required": ["finding_id", "new_severity"],
                },
            },
        }
