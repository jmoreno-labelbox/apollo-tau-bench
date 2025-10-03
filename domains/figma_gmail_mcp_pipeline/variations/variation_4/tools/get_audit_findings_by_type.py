from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetAuditFindingsByType(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        finding_type: str = None,
        violation_type: str = None,
        severity: str = None,
        audit_id: str = None,
        limit: int = 10
    ) -> str:
        """
        Obtains audit findings filtered by type and additional criteria.
        """
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        results = []

        # Handle design system findings
        if not violation_type:  # Check design system findings only if no violation_type is given
            for finding in audit_findings_ds:
                if finding_type and finding.get("finding_type") != finding_type:
                    continue
                if severity and finding.get("severity") != severity:
                    continue
                if audit_id and finding.get("audit_id") != audit_id:
                    continue

                results.append({"source": "DS", "finding": finding})

        # Handle accessibility findings
        if not finding_type:  # Check accessibility findings only if no finding_type is given
            for finding in audit_findings_a11y:
                if violation_type and finding.get("violation_type") != violation_type:
                    continue
                if severity and finding.get("severity") != severity:
                    continue
                if audit_id and finding.get("audit_id") != audit_id:
                    continue

                results.append({"source": "A11Y", "finding": finding})

        # Enforce limit
        results = results[:limit]
        payload = {"total_found": len(results), "findings": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditFindingsByType",
                "description": "Retrieves audit findings filtered by type, violation type, severity and other criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_type": {
                            "type": "string",
                            "description": "DS finding type filter (UNMAPPED, AMBIGUOUS, SUBSTITUTE_RECOMMENDED).",
                        },
                        "violation_type": {
                            "type": "string",
                            "description": "A11y violation type filter (TOUCH_TARGET, CONTRAST, TEXT_SIZING, RTL).",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Severity level filter (LOW, MEDIUM, HIGH, CRITICAL).",
                        },
                        "audit_id": {
                            "type": "string",
                            "description": "Filter by specific audit ID.",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of results to return (default 10).",
                        },
                    },
                    "required": [],
                },
            },
        }
