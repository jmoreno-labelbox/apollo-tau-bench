from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAuditFindingDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, finding_id: str = None, include_resolved: bool = False) -> str:
        """
        Obtains detailed information regarding audit findings with optional filtering.
        """
        if not audit_id:
            payload = {"error": "audit_id is required."}
            out = json.dumps(payload)
            return out

        #Retrieve findings from both datasets
        ds_findings = data.get("audit_findings_ds", {}).values()
        a11y_findings = data.get("audit_findings_a11y", {}).values()

        #Sort by audit_id
        ds_results = [f for f in ds_findings.values() if f.get("audit_id") == audit_id]
        a11y_results = [f for f in a11y_findings.values() if f.get("audit_id") == audit_id]

        #Sort by specific finding_id if supplied
        if finding_id:
            ds_results = [f for f in ds_results.values() if f.get("finding_id") == finding_id]
            a11y_results = [
                f for f in a11y_results if f.get("finding_id") == finding_id
            ]

        #Sort out resolved findings if not requested
        if not include_resolved:
            ds_results = [
                f
                for f in ds_results
                if f.get("status", "OPEN") not in ["RESOLVED", "VERIFIED"]
            ]
            a11y_results = [
                f
                for f in a11y_results
                if f.get("status", "OPEN") not in ["RESOLVED", "VERIFIED"]
            ]

        #Merge and enhance results
        all_findings = []

        for finding in ds_results:
            enriched = finding.copy()
            enriched["finding_category"] = "design_system"
            all_findings.append(enriched)

        for finding in a11y_results:
            enriched = finding.copy()
            enriched["finding_category"] = "accessibility"
            all_findings.append(enriched)

        #Order by severity and creation sequence
        severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
        all_findings.sort(
            key=lambda x: (
                severity_order.get(x.get("severity", "MEDIUM"), 2),
                x.get("finding_id", ""),
            )
        )
        payload = {
                "audit_id": audit_id,
                "total_findings": len(all_findings),
                "design_system_findings": len(ds_results),
                "accessibility_findings": len(a11y_results),
                "findings": all_findings,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuditFindingDetails",
                "description": "Retrieves detailed audit finding information with filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The ID of the audit to get findings for.",
                        },
                        "finding_id": {
                            "type": "string",
                            "description": "Optional specific finding ID to retrieve.",
                        },
                        "include_resolved": {
                            "type": "boolean",
                            "description": "Include resolved/verified findings (default false).",
                        },
                    },
                    "required": ["audit_id"],
                },
            },
        }
