# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditReportSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves comprehensive audit report summary with findings breakdown.
        """
        audit_id = kwargs.get("audit_id")

        if not audit_id:
            return json.dumps({"error": "audit_id is required."})

        audits = data.get("audits", [])
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        # Find the audit
        audit_info = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_info = audit
                break

        if not audit_info:
            return json.dumps({"error": f"Audit with ID {audit_id} not found."})

        # Get findings for this audit
        ds_findings = [f for f in audit_findings_ds if f.get("audit_id") == audit_id]
        a11y_findings = [f for f in audit_findings_a11y if f.get("audit_id") == audit_id]

        # Count findings by severity
        severity_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0}

        for finding in ds_findings + a11y_findings:
            severity = finding.get("severity", "MEDIUM")
            if severity in severity_counts:
                severity_counts[severity] += 1

        include_details = kwargs.get("include_details", False)

        summary = {
            "audit_info": audit_info,
            "ds_findings_count": len(ds_findings),
            "a11y_findings_count": len(a11y_findings),
            "total_findings": len(ds_findings) + len(a11y_findings),
            "severity_breakdown": severity_counts
        }

        if include_details:
            summary["ds_findings"] = ds_findings
            summary["a11y_findings"] = a11y_findings

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_report_summary",
                "description": "Retrieves comprehensive audit report summary with findings breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to generate summary for."},
                        "include_details": {"type": "boolean", "description": "Include detailed finding information (default false)."}
                    },
                    "required": ["audit_id"]
                }
            }
        }
