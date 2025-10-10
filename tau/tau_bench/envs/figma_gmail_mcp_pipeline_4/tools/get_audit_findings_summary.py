# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditFindingsSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves a comprehensive summary of audit findings including design system and accessibility violations.
        """
        audit_id = kwargs.get('audit_id')
        finding_type = kwargs.get('finding_type')
        severity = kwargs.get('severity')
        violation_type = kwargs.get('violation_type')

        audits = data.get('audits', [])
        audit_findings_ds = data.get('audit_findings_ds', [])
        audit_findings_a11y = data.get('audit_findings_a11y', [])

        # If audit_id is provided, return specific audit findings
        if audit_id:
            audit_info = None
            for audit in audits:
                if audit.get('audit_id') == audit_id:
                    audit_info = audit
                    break

            if not audit_info:
                return json.dumps({"error": f"Audit with ID '{audit_id}' not found."})

            # Get findings for this audit
            ds_findings = [f for f in audit_findings_ds if f.get('audit_id') == audit_id]
            a11y_findings = [f for f in audit_findings_a11y if f.get('audit_id') == audit_id]

            summary = {
                "audit_info": audit_info,
                "design_system_findings": {
                    "total": len(ds_findings),
                    "unmapped": len([f for f in ds_findings if f.get('finding_type') == 'UNMAPPED']),
                    "substitute_recommended": len([f for f in ds_findings if f.get('finding_type') == 'SUBSTITUTE_RECOMMENDED']),
                    "ambiguous": len([f for f in ds_findings if f.get('finding_type') == 'AMBIGUOUS'])
                },
                "accessibility_findings": {
                    "total": len(a11y_findings),
                    "touch_target": len([f for f in a11y_findings if f.get('violation_type') == 'TOUCH_TARGET']),
                    "contrast": len([f for f in a11y_findings if f.get('violation_type') == 'CONTRAST']),
                    "text_sizing": len([f for f in a11y_findings if f.get('violation_type') == 'TEXT_SIZING']),
                    "rtl": len([f for f in a11y_findings if f.get('violation_type') == 'RTL'])
                },
                "findings": {
                    "design_system": ds_findings,
                    "accessibility": a11y_findings
                }
            }

            return json.dumps(summary, indent=2)

        # Return summary across all audits
        all_ds_findings = audit_findings_ds
        all_a11y_findings = audit_findings_a11y

        # Apply filters
        if finding_type:
            all_ds_findings = [f for f in all_ds_findings if f.get('finding_type') == finding_type]

        if violation_type:
            all_a11y_findings = [f for f in all_a11y_findings if f.get('violation_type') == violation_type]

        if severity:
            all_ds_findings = [f for f in all_ds_findings if f.get('severity') == severity]
            all_a11y_findings = [f for f in all_a11y_findings if f.get('severity') == severity]

        summary = {
            "total_audits": len(audits),
            "design_system_findings": {
                "total": len(all_ds_findings),
                "by_type": {},
                "by_severity": {}
            },
            "accessibility_findings": {
                "total": len(all_a11y_findings),
                "by_type": {},
                "by_severity": {}
            }
        }

        # Group design system findings
        for finding in all_ds_findings:
            finding_type = finding.get('finding_type')
            severity = finding.get('severity')

            if finding_type not in summary["design_system_findings"]["by_type"]:
                summary["design_system_findings"]["by_type"][finding_type] = 0
            summary["design_system_findings"]["by_type"][finding_type] += 1

            if severity not in summary["design_system_findings"]["by_severity"]:
                summary["design_system_findings"]["by_severity"][severity] = 0
            summary["design_system_findings"]["by_severity"][severity] += 1

        # Group accessibility findings
        for finding in all_a11y_findings:
            violation_type = finding.get('violation_type')
            severity = finding.get('severity')

            if violation_type not in summary["accessibility_findings"]["by_type"]:
                summary["accessibility_findings"]["by_type"][violation_type] = 0
            summary["accessibility_findings"]["by_type"][violation_type] += 1

            if severity not in summary["accessibility_findings"]["by_severity"]:
                summary["accessibility_findings"]["by_severity"][severity] = 0
            summary["accessibility_findings"]["by_severity"][severity] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_findings_summary",
                "description": "Retrieves a comprehensive summary of audit findings including design system and accessibility violations, with filtering and grouping capabilities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of a specific audit to retrieve findings for."},
                        "finding_type": {"type": "string", "description": "Filter design system findings by type (e.g., 'UNMAPPED', 'SUBSTITUTE_RECOMMENDED', 'AMBIGUOUS')."},
                        "severity": {"type": "string", "description": "Filter findings by severity (e.g., 'HIGH', 'MEDIUM', 'LOW')."},
                        "violation_type": {"type": "string", "description": "Filter accessibility findings by violation type (e.g., 'TOUCH_TARGET', 'CONTRAST', 'TEXT_SIZING', 'RTL')."}
                    }
                }
            }
        }
