from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordDsAuditFindings(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        layer_id: str,
        layer_name: str,
        finding_type: str,
        recommended_component_id_nullable: str = None,
        code_connect_link_nullable: str = None,
        severity: str = "MEDIUM",
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

        #Check the finding_type for validity
        allowed_finding_types = ["UNMAPPED", "AMBIGUOUS", "SUBSTITUTE_RECOMMENDED"]
        if finding_type not in allowed_finding_types:
            payload = {"error": f"Invalid finding_type. Allowed: {allowed_finding_types}"}
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
        audits = data.get("audits", [])
        audit_exists = any(audit.get("audit_id") == audit_id for audit in audits)
        if not audit_exists:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Check the nullable fields for validity
        if recommended_component_id_nullable is not None and not isinstance(
            recommended_component_id_nullable, str
        ):
            payload = {"error": "recommended_component_id_nullable must be a string or None"}
            out = json.dumps(
                payload)
            return out

        if code_connect_link_nullable is not None and not isinstance(
            code_connect_link_nullable, str
        ):
            payload = {"error": "code_connect_link_nullable must be a string or None"}
            out = json.dumps(
                payload)
            return out

        #Retrieve audit_findings_ds data
        audit_findings_ds = data.get("audit_findings_ds", [])

        #Create a new finding_id
        next_num = len(audit_findings_ds) + 1
        finding_id = f"finding_ds_{next_num:03d}"

        #Establish a new finding entry
        new_finding = {
            "finding_id": finding_id,
            "audit_id": audit_id,
            "layer_id": layer_id,
            "layer_name": layer_name,
            "finding_type": finding_type,
            "recommended_component_id_nullable": recommended_component_id_nullable,
            "code_connect_link_nullable": code_connect_link_nullable,
            "severity": severity,
        }

        #Include in data
        audit_findings_ds.append(new_finding)
        payload = {"new_finding": new_finding}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordDsAuditFindings",
                "description": "Record design system audit findings for a specific layer.",
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
                        "finding_type": {
                            "type": "string",
                            "description": "Type of finding (UNMAPPED, AMBIGUOUS, SUBSTITUTE_RECOMMENDED).",
                        },
                        "recommended_component_id_nullable": {
                            "type": "string",
                            "description": "Optional recommended component ID.",
                        },
                        "code_connect_link_nullable": {
                            "type": "string",
                            "description": "Optional code connect link.",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Severity level (HIGH, MEDIUM, LOW). Defaults to MEDIUM.",
                        },
                    },
                    "required": ["audit_id", "layer_id", "layer_name", "finding_type"],
                },
            },
        }
