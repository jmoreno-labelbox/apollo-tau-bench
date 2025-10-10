# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordDsAuditFindings(Tool):  # GENERATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str,
        layer_id: str,
        layer_name: str,
        finding_type: str,
        recommended_component_id_nullable: str = None,
        code_connect_link_nullable: str = None,
        severity: str = "MEDIUM"
    ) -> str:
        # Check the validity of input parameters.
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})

        if not isinstance(layer_id, str) or not layer_id:
            return json.dumps({"error": "layer_id must be a non-empty string"})

        if not isinstance(layer_name, str) or not layer_name:
            return json.dumps({"error": "layer_name must be a non-empty string"})

        # Verify finding_type
        allowed_finding_types = ["UNMAPPED", "AMBIGUOUS", "SUBSTITUTE_RECOMMENDED"]
        if finding_type not in allowed_finding_types:
            return json.dumps({"error": f"Invalid finding_type. Allowed: {allowed_finding_types}"})

        # Check severity level.
        allowed_severities = ["HIGH", "MEDIUM", "LOW"]
        if severity not in allowed_severities:
            return json.dumps({"error": f"Invalid severity. Allowed: {allowed_severities}"})

        # Check for the existence of audit_id.
        audits = list(data.get("audits", {}).values())
        audit_exists = any(audit.get("audit_id") == audit_id for audit in audits)
        if not audit_exists:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found"})

        # Check the validity of optional fields.
        if recommended_component_id_nullable is not None and not isinstance(recommended_component_id_nullable, str):
            return json.dumps({"error": "recommended_component_id_nullable must be a string or None"})

        if code_connect_link_nullable is not None and not isinstance(code_connect_link_nullable, str):
            return json.dumps({"error": "code_connect_link_nullable must be a string or None"})

        # Retrieve data from audit_findings_ds.
        audit_findings_ds = list(data.get("audit_findings_ds", {}).values())

        # Create a new finding identifier.
        next_num = len(audit_findings_ds) + 1
        finding_id = f"finding_ds_{next_num:03d}"

        # Add a new finding record.
        new_finding = {
            "finding_id": finding_id,
            "audit_id": audit_id,
            "layer_id": layer_id,
            "layer_name": layer_name,
            "finding_type": finding_type,
            "recommended_component_id_nullable": recommended_component_id_nullable,
            "code_connect_link_nullable": code_connect_link_nullable,
            "severity": severity
        }

        # Append to dataset
        audit_findings_ds.append(new_finding)

        return json.dumps({"new_finding": new_finding})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_ds_audit_findings",
                "description": "Record design system audit findings for a specific layer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The audit ID to record findings for."},
                        "layer_id": {"type": "string", "description": "The layer ID in the Figma artifact."},
                        "layer_name": {"type": "string", "description": "The name of the layer."},
                        "finding_type": {"type": "string", "description": "Type of finding (UNMAPPED, AMBIGUOUS, SUBSTITUTE_RECOMMENDED)."},
                        "recommended_component_id_nullable": {"type": "string", "description": "Optional recommended component ID."},
                        "code_connect_link_nullable": {"type": "string", "description": "Optional code connect link."},
                        "severity": {"type": "string", "description": "Severity level (HIGH, MEDIUM, LOW). Defaults to MEDIUM."}
                    },
                    "required": ["audit_id", "layer_id", "layer_name", "finding_type"]
                }
            }
        }
