# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditFindingsByType(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves audit findings filtered by type and other criteria.
        """
        finding_type = kwargs.get("finding_type")
        violation_type = kwargs.get("violation_type")
        severity = kwargs.get("severity")
        audit_id = kwargs.get("audit_id")
        limit = kwargs.get("limit", 10)

        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        results = []

        # Process DS findings
        if not violation_type:  # Only check DS findings if no violation_type specified
            for finding in audit_findings_ds:
                if finding_type and finding.get("finding_type") != finding_type:
                    continue
                if severity and finding.get("severity") != severity:
                    continue
                if audit_id and finding.get("audit_id") != audit_id:
                    continue

                results.append({
                    "source": "DS",
                    "finding": finding
                })

        # Process A11y findings
        if not finding_type:  # Only check A11y findings if no finding_type specified
            for finding in audit_findings_a11y:
                if violation_type and finding.get("violation_type") != violation_type:
                    continue
                if severity and finding.get("severity") != severity:
                    continue
                if audit_id and finding.get("audit_id") != audit_id:
                    continue

                results.append({
                    "source": "A11Y",
                    "finding": finding
                })

        # Apply limit
        results = results[:limit]

        return json.dumps({
            "total_found": len(results),
            "findings": results
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_findings_by_type",
                "description": "Retrieves audit findings filtered by type, violation type, severity and other criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_type": {"type": "string", "description": "DS finding type filter (UNMAPPED, AMBIGUOUS, SUBSTITUTE_RECOMMENDED)."},
                        "violation_type": {"type": "string", "description": "A11y violation type filter (TOUCH_TARGET, CONTRAST, TEXT_SIZING, RTL)."},
                        "severity": {"type": "string", "description": "Severity level filter (LOW, MEDIUM, HIGH, CRITICAL)."},
                        "audit_id": {"type": "string", "description": "Filter by specific audit ID."},
                        "limit": {"type": "integer", "description": "Maximum number of results to return (default 10)."}
                    },
                    "required": []
                }
            }
        }
