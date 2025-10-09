from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RecordAuditFindings(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        ds_findings: list[dict[str, Any]] = None,
        a11y_findings: list[dict[str, Any]] = None
    ) -> str:
        if not audit_id:
            payload = {"error": "Missing required field: audit_id"}
            out = json.dumps(payload, indent=2)
            return out
        if not ds_findings and not a11y_findings:
            payload = {"error": "At least one of ds_findings or a11y_findings is required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        ds_findings_in: list[dict[str, Any]] = ds_findings or []
        a11y_findings_in: list[dict[str, Any]] = a11y_findings or []

        ds_table: list[dict[str, Any]] = data.get("audit_findings_ds", [])
        a11y_table: list[dict[str, Any]] = data.get("audit_findings_a11y", [])

        ds_ids: list[str] = []
        for item in ds_findings_in:
            fid = get_next_finding_ds_id(data)
            row = {
                "finding_id": fid,
                "audit_id": audit_id,
                "layer_id": item.get("layer_id"),
                "layer_name": item.get("layer_name"),
                "finding_type": item.get("finding_type"),
                "recommended_component_id_nullable": item.get(
                    "recommended_component_id"
                ),
                "code_connect_link_nullable": item.get("code_connect_link"),
                "severity": item.get("severity"),
            }
            ds_table.append(row)
            ds_ids.append(fid)

        a11y_ids: list[str] = []
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
                "recommended_fix_summary": item.get("recommended_fix_summary"),
            }
            a11y_table.append(row)
            a11y_ids.append(fid)

        data["audit_findings_ds"] = ds_table
        data["audit_findings_a11y"] = a11y_table
        payload = {
                "audit_id": audit_id,
                "ds_count": len(ds_ids),
                "a11y_count": len(a11y_ids),
                "ds_finding_ids": ds_ids,
                "a11y_finding_ids": a11y_ids,
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
                "name": "recordAuditFindings",
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
                                    "finding_type": {
                                        "type": "string",
                                        "enum": [
                                            "UNMAPPED",
                                            "SUBSTITUTE_RECOMMENDED",
                                            "AMBIGUOUS",
                                        ],
                                    },
                                    "recommended_component_id": {
                                        "type": ["string", "null"]
                                    },
                                    "code_connect_link": {"type": ["string", "null"]},
                                    "severity": {
                                        "type": "string",
                                        "enum": ["LOW", "MEDIUM", "HIGH"],
                                    },
                                },
                            },
                        },
                        "a11y_findings": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "layer_id": {"type": "string"},
                                    "layer_name": {"type": "string"},
                                    "violation_type": {
                                        "type": "string",
                                        "enum": [
                                            "TOUCH_TARGET",
                                            "CONTRAST",
                                            "TEXT_SIZING",
                                            "RTL",
                                        ],
                                    },
                                    "violation_details_json": {"type": "string"},
                                    "severity": {
                                        "type": "string",
                                        "enum": ["LOW", "MEDIUM", "HIGH"],
                                    },
                                    "recommended_fix_summary": {"type": "string"},
                                },
                            },
                        },
                    },
                    "required": ["audit_id"],
                },
            },
        }
