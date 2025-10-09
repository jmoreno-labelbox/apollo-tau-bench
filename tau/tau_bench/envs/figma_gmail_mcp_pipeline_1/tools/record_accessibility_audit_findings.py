from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RecordAccessibilityAuditFindings(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        layer_id: str,
        layer_name: str,
        violation_type: str,
        violation_details_json: str,
        severity: str,
        recommended_fix_summary: str,
    ) -> str:
        pass
        #Check the parameters for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(layer_id, str) or not layer_id:
            payload = {"error": "layer_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(layer_name, str) or not layer_name:
            payload = {"error": "layer_name must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(violation_type, str) or not violation_type:
            payload = {"error": "violation_type must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(recommended_fix_summary, str) or not recommended_fix_summary:
            payload = {"error": "recommended_fix_summary must be a non-empty string"}
            out = json.dumps(
                payload)
            return out

        #Check the violation_type for validity
        allowed_violation_types = ["TOUCH_TARGET", "CONTRAST", "TEXT_SIZING", "RTL"]
        if violation_type not in allowed_violation_types:
            payload = {"error": f"Invalid violation_type. Allowed: {allowed_violation_types}"}
            out = json.dumps(
                payload)
            return out

        #Check the severity for validity
        allowed_severities = ["HIGH", "MEDIUM", "LOW"]
        if severity not in allowed_severities:
            payload = {"error": f"Invalid severity. Allowed: {allowed_severities}"}
            out = json.dumps(
                payload)
            return out

        #Check if the audit_id is present
        audits = data.get("audits", {}).values()
        audit_exists = any(audit.get("audit_id") == audit_id for audit in audits.values())
        if not audit_exists:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Retrieve audit_findings_a11y data
        audit_findings_a11y = data.get("audit_findings_a11y", {}).values()

        #Create a new finding_id
        next_num = len(audit_findings_a11y) + 1
        finding_id = f"finding_a11y_{next_num:03d}"

        #Establish a new finding entry
        new_finding = {
            "finding_id": finding_id,
            "audit_id": audit_id,
            "layer_id": layer_id,
            "layer_name": layer_name,
            "violation_type": violation_type,
            "violation_details_json": violation_details_json,
            "severity": severity,
            "recommended_fix_summary": recommended_fix_summary,
        }

        #Include in data
        data["audit_findings_a11y"][new_finding["audit_findings_a11y_id"]] = new_finding
        payload = {"new_finding": new_finding}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAccessibilityAuditFindings",
                "description": "Record accessibility audit findings for a specific layer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to record findings for.",
                        },
                        "layer_id": {
                            "type": "string",
                            "description": "The layer ID in the Figma artifact.",
                        },
                        "layer_name": {
                            "type": "string",
                            "description": "The name of the layer.",
                        },
                        "violation_type": {
                            "type": "string",
                            "description": "Type of violation (TOUCH_TARGET, CONTRAST, TEXT_SIZING, RTL).",
                        },
                        "violation_details_json": {
                            "type": "string",
                            "description": "JSON string containing violation details.",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Severity level (HIGH, MEDIUM, LOW).",
                        },
                        "recommended_fix_summary": {
                            "type": "string",
                            "description": "Summary of recommended fix for the violation.",
                        },
                    },
                    "required": [
                        "audit_id",
                        "layer_id",
                        "layer_name",
                        "violation_type",
                        "violation_details_json",
                        "severity",
                        "recommended_fix_summary",
                    ],
                },
            },
        }
