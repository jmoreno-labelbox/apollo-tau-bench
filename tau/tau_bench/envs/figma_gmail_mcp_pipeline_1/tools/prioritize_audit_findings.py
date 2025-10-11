# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PrioritizeAuditFindings(Tool):  # ACQUIRE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        finding_ids_list: List[str]
    ) -> str:
        # Check input for correctness.
        if not isinstance(finding_ids_list, list) or not all(isinstance(fid, str) for fid in finding_ids_list):
            return json.dumps({"error": "finding_ids_list must be a list of strings"})

        if not finding_ids_list:
            return json.dumps({"error": "finding_ids_list cannot be empty"})

        # Retrieve findings information.
        audit_findings_ds = list(data.get("audit_findings_ds", {}).values())
        audit_findings_a11y = list(data.get("audit_findings_a11y", {}).values())

        # Gather all results along with their specifics.
        findings_with_details = []

        for finding_id in finding_ids_list:
            # Prioritize searching within DS findings initially.
            ds_finding = next((f for f in audit_findings_ds if f.get("finding_id") == finding_id), None)
            if ds_finding:
                findings_with_details.append({
                    "finding_id": finding_id,
                    "severity": ds_finding.get("severity", "MEDIUM"),
                    "finding_type": "DS",
                    "layer_name": ds_finding.get("layer_name", ""),
                    "details": ds_finding
                })
                continue

            # Look for issues in A11Y results.
            a11y_finding = next((f for f in audit_findings_a11y if f.get("finding_id") == finding_id), None)
            if a11y_finding:
                findings_with_details.append({
                    "finding_id": finding_id,
                    "severity": a11y_finding.get("severity", "MEDIUM"),
                    "finding_type": "A11Y",
                    "layer_name": a11y_finding.get("layer_name", ""),
                    "details": a11y_finding
                })
                continue

            # Search unsuccessful
            return json.dumps({"error": f"Finding with ID '{finding_id}' not found in either DS or A11Y findings"})

        # Establish severity levels (larger number indicates greater priority).
        severity_priority = {
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1
        }

        # Retrieve the finding number from finding_id for resolving ties.
        def get_finding_number(finding_id):
            try:
                # Retrieve the number from finding_id formatted as "finding_ds_001" or "finding_a11y_001".
                parts = finding_id.split('_')
                if len(parts) >= 3:
                    return int(parts[-1])
                return 0
            except (ValueError, IndexError):
                return 0

        # Order findings first by severity in descending order, and then by finding number in ascending order.
        sorted_findings = sorted(
            findings_with_details,
            key=lambda x: (
                -severity_priority.get(x["severity"], 0),  # Indicates descending order with a negative value.
                get_finding_number(x["finding_id"])        # Order in ascending manner for resolving ties.
            )
        )

        # Establish priority assignments.
        priority_mapping = {}
        for i, finding in enumerate(sorted_findings, 1):
            priority_mapping[finding["finding_id"]] = i

        # Generate comprehensive output.
        prioritized_findings = []
        for i, finding in enumerate(sorted_findings, 1):
            prioritized_findings.append({
                "priority": i,
                "finding_id": finding["finding_id"],
                "severity": finding["severity"],
            })

        return json.dumps({
            "priority_mapping": priority_mapping,
            "prioritized_findings": prioritized_findings,
            "total_findings": len(finding_ids_list)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "prioritize_audit_findings",
                "description": "Prioritize a list of audit findings by severity (HIGH > MEDIUM > LOW) and then by finding number for tie-breaking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_ids_list": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of finding IDs from either audit_findings_ds or audit_findings_a11y to prioritize."
                        }
                    },
                    "required": ["finding_ids_list"]
                }
            }
        }
