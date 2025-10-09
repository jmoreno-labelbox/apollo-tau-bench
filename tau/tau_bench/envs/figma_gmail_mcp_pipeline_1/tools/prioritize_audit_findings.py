from tau_bench.envs.tool import Tool
import json
from typing import Any

class PrioritizeAuditFindings(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], finding_ids_list: list[str]) -> str:
        pass
        #Check the input for validity
        if not isinstance(finding_ids_list, list) or not all(
            isinstance(fid, str) for fid in finding_ids_list
        ):
            payload = {"error": "finding_ids_list must be a list of strings"}
            out = json.dumps(payload)
            return out

        if not finding_ids_list:
            payload = {"error": "finding_ids_list cannot be empty"}
            out = json.dumps(payload)
            return out

        #Retrieve findings data
        audit_findings_ds = data.get("audit_findings_ds", [])
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        #Gather all findings along with their details
        findings_with_details = []

        for finding_id in finding_ids_list:
            #Prioritize searching in DS findings
            ds_finding = next(
                (f for f in audit_findings_ds if f.get("finding_id") == finding_id),
                None,
            )
            if ds_finding:
                findings_with_details.append(
                    {
                        "finding_id": finding_id,
                        "severity": ds_finding.get("severity", "MEDIUM"),
                        "finding_type": "DS",
                        "layer_name": ds_finding.get("layer_name", ""),
                        "details": ds_finding,
                    }
                )
                continue

            #Search within A11Y findings
            a11y_finding = next(
                (f for f in audit_findings_a11y if f.get("finding_id") == finding_id),
                None,
            )
            if a11y_finding:
                findings_with_details.append(
                    {
                        "finding_id": finding_id,
                        "severity": a11y_finding.get("severity", "MEDIUM"),
                        "finding_type": "A11Y",
                        "layer_name": a11y_finding.get("layer_name", ""),
                        "details": a11y_finding,
                    }
                )
                continue
            payload = {
                    "error": f"Finding with ID '{finding_id}' not found in either DS or A11Y findings"
                }
            out = json.dumps(
                payload)
            return out

        #Establish severity priority (higher number indicates higher priority)
        severity_priority = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}

        #Obtain the finding number from finding_id for resolving ties
        def get_finding_number(finding_id):
            pass
            try:
                #Retrieve the number from finding_id such as "finding_ds_001" or "finding_a11y_001"
                parts = finding_id.split("_")
                if len(parts) >= 3:
                    return int(parts[-1])
                return 0
            except (ValueError, IndexError):
                return 0

        #Order findings by severity (descending) followed by finding number (ascending)
        sorted_findings = sorted(
            findings_with_details,
            key=lambda x: (
                -severity_priority.get(
                    x["severity"], 0
                ),  #Use negative for descending order
                get_finding_number(x["finding_id"]),  #Use ascending order for resolving ties
            ),
        )

        #Establish a mapping for priorities
        priority_mapping = {}
        for i, finding in enumerate(sorted_findings, 1):
            priority_mapping[finding["finding_id"]] = i

        #Generate a comprehensive result
        prioritized_findings = []
        for i, finding in enumerate(sorted_findings, 1):
            prioritized_findings.append(
                {
                    "priority": i,
                    "finding_id": finding["finding_id"],
                    "severity": finding["severity"],
                }
            )
        payload = {
                "priority_mapping": priority_mapping,
                "prioritized_findings": prioritized_findings,
                "total_findings": len(finding_ids_list),
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PrioritizeAuditFindings",
                "description": "Prioritize a list of audit findings by severity (HIGH > MEDIUM > LOW) and then by finding number for tie-breaking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "finding_ids_list": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of finding IDs from either audit_findings_ds or audit_findings_a11y to prioritize.",
                        }
                    },
                    "required": ["finding_ids_list"],
                },
            },
        }
