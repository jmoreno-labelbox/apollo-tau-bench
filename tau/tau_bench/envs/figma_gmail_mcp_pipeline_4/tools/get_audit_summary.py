from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAuditSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None) -> str:
        """
        Obtains a summary of audit findings.
        """
        if not audit_id:
            payload = {"error": "audit_id is required"}
            out = json.dumps(payload)
            return out

        # Locate the audit
        for audit in data.get("audits", []):
            if audit.get("audit_id") == audit_id:
                # Tally findings based on severity
                findings = [
                    f
                    for f in data.get("audit_findings", [])
                    if f.get("audit_id") == audit_id
                ]
                severity_counts = {}
                for finding in findings:
                    severity = finding.get("severity", "UNKNOWN")
                    severity_counts[severity] = severity_counts.get(severity, 0) + 1
                payload = {
                    "audit_id": audit_id,
                    "total_findings": len(findings),
                    "severity_counts": severity_counts,
                    "status": audit.get("status"),
                    "last_updated": audit.get("last_updated"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Audit with ID {audit_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditSummary",
                "description": "Retrieves a summary of audit findings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to summarize.",
                        }
                    },
                    "required": ["audit_id"],
                },
            },
        }
