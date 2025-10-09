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

class GetAuditFindingsSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        finding_type: str = None,
        severity: str = None,
        violation_type: str = None,
        include_resolved: bool = None
    ) -> str:
        """
        Obtains a detailed summary of audit findings, including violations from the design system and accessibility.
        """
        audits = data.get("audits", [])
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        # Return specific audit findings if audit_id is supplied
        if audit_id:
            audit_info = None
            for audit in audits:
                if audit.get("audit_id") == audit_id:
                    audit_info = audit
                    break

            if not audit_info:
                payload = {"error": f"Audit with ID '{audit_id}' not found."}
                out = json.dumps(payload)
                return out

            # Retrieve findings related to this audit
            ds_findings = [
                f for f in audit_findings_ds if f.get("audit_id") == audit_id
            ]
            a11y_findings = [
                f for f in audit_findings_a11y if f.get("audit_id") == audit_id
            ]

            summary = {
                "audit_info": audit_info,
                "design_system_findings": {
                    "total": len(ds_findings),
                    "unmapped": len(
                        [f for f in ds_findings if f.get("finding_type") == "UNMAPPED"]
                    ),
                    "substitute_recommended": len(
                        [
                            f
                            for f in ds_findings
                            if f.get("finding_type") == "SUBSTITUTE_RECOMMENDED"
                        ]
                    ),
                    "ambiguous": len(
                        [f for f in ds_findings if f.get("finding_type") == "AMBIGUOUS"]
                    ),
                },
                "accessibility_findings": {
                    "total": len(a11y_findings),
                    "touch_target": len(
                        [
                            f
                            for f in a11y_findings
                            if f.get("violation_type") == "TOUCH_TARGET"
                        ]
                    ),
                    "contrast": len(
                        [
                            f
                            for f in a11y_findings
                            if f.get("violation_type") == "CONTRAST"
                        ]
                    ),
                    "text_sizing": len(
                        [
                            f
                            for f in a11y_findings
                            if f.get("violation_type") == "TEXT_SIZING"
                        ]
                    ),
                    "rtl": len(
                        [f for f in a11y_findings if f.get("violation_type") == "RTL"]
                    ),
                },
                "findings": {
                    "design_system": ds_findings,
                    "accessibility": a11y_findings,
                },
            }
            payload = summary
            out = json.dumps(payload, indent=2)
            return out

        # Provide a summary for all audits
        all_ds_findings = audit_findings_ds
        all_a11y_findings = audit_findings_a11y

        # Enforce filters
        if finding_type:
            all_ds_findings = [
                f for f in all_ds_findings if f.get("finding_type") == finding_type
            ]

        if violation_type:
            all_a11y_findings = [
                f
                for f in all_a11y_findings
                if f.get("violation_type") == violation_type
            ]

        if severity:
            all_ds_findings = [
                f for f in all_ds_findings if f.get("severity") == severity
            ]
            all_a11y_findings = [
                f for f in all_a11y_findings if f.get("severity") == severity
            ]

        summary = {
            "total_audits": len(audits),
            "design_system_findings": {
                "total": len(all_ds_findings),
                "by_type": {},
                "by_severity": {},
            },
            "accessibility_findings": {
                "total": len(all_a11y_findings),
                "by_type": {},
                "by_severity": {},
            },
        }

        # Categorize findings from the design system
        for finding in all_ds_findings:
            finding_type = finding.get("finding_type")
            severity = finding.get("severity")

            if finding_type not in summary["design_system_findings"]["by_type"]:
                summary["design_system_findings"]["by_type"][finding_type] = 0
            summary["design_system_findings"]["by_type"][finding_type] += 1

            if severity not in summary["design_system_findings"]["by_severity"]:
                summary["design_system_findings"]["by_severity"][severity] = 0
            summary["design_system_findings"]["by_severity"][severity] += 1

        # Classify accessibility findings
        for finding in all_a11y_findings:
            violation_type = finding.get("violation_type")
            severity = finding.get("severity")

            if violation_type not in summary["accessibility_findings"]["by_type"]:
                summary["accessibility_findings"]["by_type"][violation_type] = 0
            summary["accessibility_findings"]["by_type"][violation_type] += 1

            if severity not in summary["accessibility_findings"]["by_severity"]:
                summary["accessibility_findings"]["by_severity"][severity] = 0
            summary["accessibility_findings"]["by_severity"][severity] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditFindingsSummary",
                "description": "Retrieves a comprehensive summary of audit findings including design system and accessibility violations, with filtering and grouping capabilities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of a specific audit to retrieve findings for.",
                        },
                        "finding_type": {
                            "type": "string",
                            "description": "Filter design system findings by type (e.g., 'UNMAPPED', 'SUBSTITUTE_RECOMMENDED', 'AMBIGUOUS').",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Filter findings by severity (e.g., 'HIGH', 'MEDIUM', 'LOW').",
                        },
                        "violation_type": {
                            "type": "string",
                            "description": "Filter accessibility findings by violation type (e.g., 'TOUCH_TARGET', 'CONTRAST', 'TEXT_SIZING', 'RTL').",
                        },
                    },
                },
            },
        }
