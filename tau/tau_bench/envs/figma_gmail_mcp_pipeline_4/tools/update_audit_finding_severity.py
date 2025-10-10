# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAuditFindingSeverity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], finding_id, new_severity, updated_by, notes = "", updated_ts = "2024-08-23T15:00:00Z") -> str:
        """
        Updates the severity level of an audit finding.
        """

        if not all([finding_id, new_severity]):
            return json.dumps({"error": "finding_id and new_severity are required."})

        return json.dumps({
            "status": "SUCCESS",
            "finding_id": finding_id,
            "previous_severity": "MEDIUM",
            "new_severity": new_severity,
            "updated_by": updated_by,
            "notes": notes,
            "updated_ts": updated_ts
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_audit_finding_severity",
                "description": "Updates the severity level of an audit finding (DS or A11y).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_id": {"type": "string", "description": "The ID of the audit finding to update."},
                        "new_severity": {"type": "string", "description": "The new severity level (LOW, MEDIUM, HIGH, CRITICAL)."},
                        "updated_by": {"type": "string", "description": "Email of the user updating the severity."},
                        "notes": {"type": "string", "description": "Optional notes about the severity change."},
                        "updated_ts": {"type": "string", "description": "Timestamp of the update."}
                    },
                    "required": ["finding_id", "new_severity"]
                }
            }
        }
