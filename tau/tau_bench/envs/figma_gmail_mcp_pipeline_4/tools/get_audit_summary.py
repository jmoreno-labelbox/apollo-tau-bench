# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves a summary of audit findings.
        """
        audit_id = kwargs.get('audit_id')

        if not audit_id:
            return json.dumps({"error": "audit_id is required"})

        # Find the audit
        for audit in data.get('audits', []):
            if audit.get('audit_id') == audit_id:
                # Count findings by severity
                findings = [f for f in data.get('audit_findings', []) if f.get('audit_id') == audit_id]
                severity_counts = {}
                for finding in findings:
                    severity = finding.get('severity', 'UNKNOWN')
                    severity_counts[severity] = severity_counts.get(severity, 0) + 1

                return json.dumps({
                    "audit_id": audit_id,
                    "total_findings": len(findings),
                    "severity_counts": severity_counts,
                    "status": audit.get('status'),
                    "last_updated": audit.get('last_updated')
                })

        return json.dumps({"error": f"Audit with ID {audit_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_summary",
                "description": "Retrieves a summary of audit findings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to summarize."}
                    },
                    "required": ["audit_id"]
                }
            }
        }
