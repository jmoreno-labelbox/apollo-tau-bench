from tau_bench.envs.tool import Tool
import json
from typing import Any

class LoadAuditFindings(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "Invalid audit_id parameter"}
            out = json.dumps(payload)
            return out

        #Identify the audit
        audits = data.get("audits", [])
        audit = None
        for a in audits:
            if a.get("audit_id") == audit_id:
                audit = a
                break

        if not audit:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Retrieve details about the audit
        audit_type = audit.get("audit_type")
        artifact_id = audit.get("artifact_id")

        #Locate associated DS findings
        ds_findings = []
        audit_findings_ds = data.get("audit_findings_ds", [])
        for finding in audit_findings_ds:
            if finding.get("audit_id") == audit_id:
                ds_findings.append(
                    {
                        "finding_id": finding.get("finding_id"),
                        "layer_id": finding.get("layer_id"),
                        "layer_name": finding.get("layer_name"),
                        "finding_type": finding.get("finding_type"),
                        "severity": finding.get("severity"),
                    }
                )

        #Locate associated A11Y findings
        a11y_findings = []
        audit_findings_a11y = data.get("audit_findings_a11y", [])
        for finding in audit_findings_a11y:
            if finding.get("audit_id") == audit_id:
                a11y_findings.append(
                    {
                        "finding_id": finding.get("finding_id"),
                        "layer_id": finding.get("layer_id"),
                        "layer_name": finding.get("layer_name"),
                        "violation_type": finding.get("violation_type"),
                        "severity": finding.get("severity"),
                    }
                )
        payload = {
                "audit_id": audit_id,
                "audit_type": audit_type,
                "artifact_id": artifact_id,
                "ds_findings": ds_findings,
                "a11y_findings": a11y_findings,
                "total_ds_findings": len(ds_findings),
                "total_a11y_findings": len(a11y_findings),
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LoadAuditFindings",
                "description": "Load audit information and all associated findings for a given audit ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to load findings for.",
                        }
                    },
                    "required": ["audit_id"],
                },
            },
        }
