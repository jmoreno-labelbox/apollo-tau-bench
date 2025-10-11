# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _ymd(iso_ts: str) -> str:
    # '2024-08-23T10:00:00Z' -> '2024-08-23'
    return (iso_ts or "").split("T")[0]

def _id_from_request(prefix: str, request_id: str) -> str:
    rid = (request_id or "").strip()
    if not rid:
        return None
    return f"{prefix}_{rid}"

def _get_next_id(prefix: str, existing_ids: List[str]) -> str:
    max_id_num = 0
    seen = False
    for s in existing_ids:
        if isinstance(s, str) and s.startswith(prefix + "_"):
            seen = True
            try:
                n = int(s.split("_")[-1])
                if n > max_id_num:
                    max_id_num = n
            except Exception:
                pass
    return f"{prefix}_{(1 if not seen else max_id_num + 1):03d}"

class generate_combined_audit_report(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], audit_id: str, artifact_id: str, output_format: str, timestamp: str, request_id: str) -> str:
        audits = data.get("audits", [])
        arts = data.get("figma_artifacts", [])
        if not any(isinstance(a, dict) and a.get("audit_id") == audit_id for a in audits):
            return json.dumps({"error": f"audit_id '{audit_id}' not found"}, indent=2)
        if not any(isinstance(a, dict) and a.get("artifact_id") == artifact_id for a in arts):
            return json.dumps({"error": f"artifact_id '{artifact_id}' not found"}, indent=2)

        reports = data.setdefault("audit_reports", [])
        assets = data.setdefault("assets", [])

        report_id = _id_from_request("rep", request_id) or _get_next_id("rep", [r.get("report_id", "") for r in reports if isinstance(r, dict)])
        existing_report = next((r for r in reports if isinstance(r, dict) and r.get("report_id") == report_id), None)
        if existing_report:
            return json.dumps(existing_report, indent=2)

        asset_id = _id_from_request("asset", request_id) or _get_next_id("asset", [r.get("asset_id", "") for r in assets if isinstance(r, dict)])
        mime = "application/pdf" if (output_format or "").upper() == "PDF" else "application/octet-stream"
        asset_row = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": f"REPORT_{(output_format or '').upper()}",
            "mime_type": mime,
            "file_name": f"{audit_id}_{artifact_id}_combined_report.{(output_format or 'bin').lower()}",
            "size_bytes": 0,
            "day": _ymd(timestamp),
        }
        assets.append(asset_row)

        report_row = {
            "report_id": report_id,
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "report_asset_id": asset_id,
            "format": (output_format or "").upper(),
            "day": _ymd(timestamp),
        }
        reports.append(report_row)

        return json.dumps(report_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_combined_audit_report",
                "description": "Produce a combined DS + A11Y audit report for an artifact and persist a report asset deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                        "output_format": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["audit_id", "artifact_id", "output_format", "timestamp", "request_id"],
                },
            },
        }