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

class GetAuditReportSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, include_details: bool = False, audit_type: str = None) -> str:
        """
        Obtains a detailed summary of the audit report with a breakdown of findings.
        """
        if not audit_id:
            payload = {"error": "audit_id is required."}
            out = json.dumps(payload)
            return out

        audits = data.get("audits", [])
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        #Locate the audit
        audit_info = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_info = audit
                break

        if not audit_info:
            payload = {"error": f"Audit with ID {audit_id} not found."}
            out = json.dumps(payload)
            return out

        #Retrieve findings related to this audit
        ds_findings = [f for f in audit_findings_ds if f.get("audit_id") == audit_id]
        a11y_findings = [
            f for f in audit_findings_a11y if f.get("audit_id") == audit_id
        ]

        #Tally findings based on severity
        severity_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0}

        for finding in ds_findings + a11y_findings:
            severity = finding.get("severity", "MEDIUM")
            if severity in severity_counts:
                severity_counts[severity] += 1

        summary = {
            "audit_info": audit_info,
            "ds_findings_count": len(ds_findings),
            "a11y_findings_count": len(a11y_findings),
            "total_findings": len(ds_findings) + len(a11y_findings),
            "severity_breakdown": severity_counts,
        }

        if include_details:
            summary["ds_findings"] = ds_findings
            summary["a11y_findings"] = a11y_findings
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditReportSummary",
                "description": "Retrieves comprehensive audit report summary with findings breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to generate summary for.",
                        },
                        "include_details": {
                            "type": "boolean",
                            "description": "Include detailed finding information (default false).",
                        },
                    },
                    "required": ["audit_id"],
                },
            },
        }
