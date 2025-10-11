# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuditFindingDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], audit_id, finding_id, include_resolved = False) -> str:
        """
        Retrieves detailed information about audit findings with optional filtering.
        """

        if not audit_id:
            return json.dumps({"error": "audit_id is required."})

        # Retrieve results from the two datasets.
        ds_findings = data.get('audit_findings_ds', [])
        a11y_findings = data.get('audit_findings_a11y', [])

        # Filter based on audit_id
        ds_results = [f for f in ds_findings if f.get('audit_id') == audit_id]
        a11y_results = [f for f in a11y_findings if f.get('audit_id') == audit_id]

        # Apply a filter based on the specified finding_id if available.
        if finding_id:
            ds_results = [f for f in ds_results if f.get('finding_id') == finding_id]
            a11y_results = [f for f in a11y_results if f.get('finding_id') == finding_id]

        # Exclude resolved findings unless specifically requested.
        if not include_resolved:
            ds_results = [f for f in ds_results if f.get('status', 'OPEN') not in ['RESOLVED', 'VERIFIED']]
            a11y_results = [f for f in a11y_results if f.get('status', 'OPEN') not in ['RESOLVED', 'VERIFIED']]

        # Merge and enhance outcomes.
        all_findings = []

        for finding in ds_results:
            enriched = finding.copy()
            enriched['finding_category'] = 'design_system'
            all_findings.append(enriched)

        for finding in a11y_results:
            enriched = finding.copy()
            enriched['finding_category'] = 'accessibility'
            all_findings.append(enriched)

        # Order by severity and creation date.
        severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        all_findings.sort(key=lambda x: (
            severity_order.get(x.get('severity', 'MEDIUM'), 2),
            x.get('finding_id', '')
        ))

        return json.dumps({
            "audit_id": audit_id,
            "total_findings": len(all_findings),
            "design_system_findings": len(ds_results),
            "accessibility_findings": len(a11y_results),
            "findings": all_findings
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_audit_finding_details",
                "description": "Retrieves detailed audit finding information with filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The ID of the audit to get findings for."},
                        "finding_id": {"type": "string", "description": "Optional specific finding ID to retrieve."},
                        "include_resolved": {"type": "boolean", "description": "Include resolved/verified findings (default false)."}
                    },
                    "required": ["audit_id"]
                }
            }
        }
