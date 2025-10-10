# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LoadAuditFindings(Tool):  # READING
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str
    ) -> str:
        # Verify input.
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "Invalid audit_id parameter"})

        # Locate the audit.
        audits = list(data.get("audits", {}).values())
        audit = None
        for a in audits:
            if a.get("audit_id") == audit_id:
                audit = a
                break

        if not audit:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found"})

        # Retrieve auditing details.
        audit_type = audit.get("audit_type")
        artifact_id = audit.get("artifact_id")

        # Retrieve associated data science insights.
        ds_findings = []
        audit_findings_ds = list(data.get("audit_findings_ds", {}).values())
        for finding in audit_findings_ds:
            if finding.get("audit_id") == audit_id:
                ds_findings.append({
                    "finding_id": finding.get("finding_id"),
                    "layer_id": finding.get("layer_id"),
                    "layer_name": finding.get("layer_name"),
                    "finding_type": finding.get("finding_type"),
                    "severity": finding.get("severity")
                })

        # Locate associated accessibility issues.
        a11y_findings = []
        audit_findings_a11y = list(data.get("audit_findings_a11y", {}).values())
        for finding in audit_findings_a11y:
            if finding.get("audit_id") == audit_id:
                a11y_findings.append({
                    "finding_id": finding.get("finding_id"),
                    "layer_id": finding.get("layer_id"),
                    "layer_name": finding.get("layer_name"),
                    "violation_type": finding.get("violation_type"),
                    "severity": finding.get("severity")
                })

        return json.dumps({
            "audit_id": audit_id,
            "audit_type": audit_type,
            "artifact_id": artifact_id,
            "ds_findings": ds_findings,
            "a11y_findings": a11y_findings,
            "total_ds_findings": len(ds_findings),
            "total_a11y_findings": len(a11y_findings)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "load_audit_findings",
                "description": "Load audit information and all associated findings for a given audit ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The audit ID to load findings for."}
                    },
                    "required": ["audit_id"]
                }
            }
        }
