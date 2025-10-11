# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordAuditFindings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], a11y_findings, audit_id, ds_findings) -> str:
        if not audit_id:
            return json.dumps({"error": "Missing required field: audit_id"}, indent=2)
        if not ds_findings and not a11y_findings:
            return json.dumps({"error": "At least one of ds_findings or a11y_findings is required"}, indent=2)
        ds_findings_in: List[Dict[str, Any]] = ds_findings or []
        a11y_findings_in: List[Dict[str, Any]] = a11y_findings or []

        ds_table: List[Dict[str, Any]] = data.get("audit_findings_ds", [])
        a11y_table: List[Dict[str, Any]] = data.get("audit_findings_a11y", [])

        ds_ids: List[str] = []
        for item in ds_findings_in:
            fid = get_next_finding_ds_id(data)
            row = {
                "finding_id": fid,
                "audit_id": audit_id,
                "layer_id": item.get("layer_id"),
                "layer_name": item.get("layer_name"),
                "finding_type": item.get("finding_type"),
                "recommended_component_id_nullable": item.get("recommended_component_id"),
                "code_connect_link_nullable": item.get("code_connect_link"),
                "severity": item.get("severity")
            }
            ds_table.append(row)
            ds_ids.append(fid)

        a11y_ids: List[str] = []
        for item in a11y_findings_in:
            fid = get_next_finding_a11y_id(data)
            row = {
                "finding_id": fid,
                "audit_id": audit_id,
                "layer_id": item.get("layer_id"),
                "layer_name": item.get("layer_name"),
                "violation_type": item.get("violation_type"),
                "violation_details_json": item.get("violation_details_json"),
                "severity": item.get("severity"),
                "recommended_fix_summary": item.get("recommended_fix_summary")
            }
            a11y_table.append(row)
            a11y_ids.append(fid)

        data["audit_findings_ds"] = ds_table
        data["audit_findings_a11y"] = a11y_table

        return json.dumps(
            {
                "audit_id": audit_id,
                "ds_count": len(ds_ids),
                "a11y_count": len(a11y_ids),
                "ds_finding_ids": ds_ids,
                "a11y_finding_ids": a11y_ids
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_audit_findings",
                "description": "Record design system mapping findings and accessibility findings for an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "ds_findings": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "layer_id": {"type": "string"},
                                    "layer_name": {"type": "string"},
                                    "finding_type": {"type": "string", "enum": ["UNMAPPED", "SUBSTITUTE_RECOMMENDED", "AMBIGUOUS"]},
                                    "recommended_component_id": {"type": ["string", "null"]},
                                    "code_connect_link": {"type": ["string", "null"]},
                                    "severity": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]}
                                }
                            }
                        },
                        "a11y_findings": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "layer_id": {"type": "string"},
                                    "layer_name": {"type": "string"},
                                    "violation_type": {"type": "string", "enum": ["TOUCH_TARGET", "CONTRAST", "TEXT_SIZING", "RTL"]},
                                    "violation_details_json": {"type": "string"},
                                    "severity": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]},
                                    "recommended_fix_summary": {"type": "string"}
                                }
                            }
                        }
                    },
                    "required": ["audit_id"]
                }
            }
        }
