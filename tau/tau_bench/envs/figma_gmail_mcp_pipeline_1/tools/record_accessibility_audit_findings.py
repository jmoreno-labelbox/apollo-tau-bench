# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordAccessibilityAuditFindings(Tool):  # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str,
        layer_id: str,
        layer_name: str,
        violation_type: str,
        violation_details_json: str,
        severity: str,
        recommended_fix_summary: str
    ) -> str:
        # Verify input arguments.
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})

        if not isinstance(layer_id, str) or not layer_id:
            return json.dumps({"error": "layer_id must be a non-empty string"})

        if not isinstance(layer_name, str) or not layer_name:
            return json.dumps({"error": "layer_name must be a non-empty string"})

        if not isinstance(violation_type, str) or not violation_type:
            return json.dumps({"error": "violation_type must be a non-empty string"})

        if not isinstance(recommended_fix_summary, str) or not recommended_fix_summary:
            return json.dumps({"error": "recommended_fix_summary must be a non-empty string"})

        # Check the validity of violation_type.
        allowed_violation_types = ["TOUCH_TARGET", "CONTRAST", "TEXT_SIZING", "RTL"]
        if violation_type not in allowed_violation_types:
            return json.dumps({"error": f"Invalid violation_type. Allowed: {allowed_violation_types}"})

        # Check severity level.
        allowed_severities = ["HIGH", "MEDIUM", "LOW"]
        if severity not in allowed_severities:
            return json.dumps({"error": f"Invalid severity. Allowed: {allowed_severities}"})

        # Check if audit_id is present.
        audits = data.get("audits", [])
        audit_exists = any(audit.get("audit_id") == audit_id for audit in audits)
        if not audit_exists:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found"})

        # Retrieve audit_findings_a11y information.
        audit_findings_a11y = data.get("audit_findings_a11y", [])

        # Create a new finding_id.
        next_num = len(audit_findings_a11y) + 1
        finding_id = f"finding_a11y_{next_num:03d}"

        # Generate a new discovery record.
        new_finding = {
            "finding_id": finding_id,
            "audit_id": audit_id,
            "layer_id": layer_id,
            "layer_name": layer_name,
            "violation_type": violation_type,
            "violation_details_json": violation_details_json,
            "severity": severity,
            "recommended_fix_summary": recommended_fix_summary
        }

        # Append to dataset
        audit_findings_a11y.append(new_finding)

        return json.dumps({"new_finding": new_finding})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_accessibility_audit_findings",
                "description": "Record accessibility audit findings for a specific layer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The audit ID to record findings for."},
                        "layer_id": {"type": "string", "description": "The layer ID in the Figma artifact."},
                        "layer_name": {"type": "string", "description": "The name of the layer."},
                        "violation_type": {"type": "string", "description": "Type of violation (TOUCH_TARGET, CONTRAST, TEXT_SIZING, RTL)."},
                        "violation_details_json": {"type": "string", "description": "JSON string containing violation details."},
                        "severity": {"type": "string", "description": "Severity level (HIGH, MEDIUM, LOW)."},
                        "recommended_fix_summary": {"type": "string", "description": "Summary of recommended fix for the violation."}
                    },
                    "required": ["audit_id", "layer_id", "layer_name", "violation_type", "violation_details_json", "severity", "recommended_fix_summary"]
                }
            }
        }
