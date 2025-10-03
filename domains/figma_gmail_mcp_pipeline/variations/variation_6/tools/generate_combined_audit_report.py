from tau_bench.envs.tool import Tool
import json
from typing import Any

class generate_combined_audit_report(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str,
        artifact_id: str,
        output_format: str,
        timestamp: str,
        request_id: str,
    ) -> str:
        audits = data.get("audits", [])
        arts = data.get("figma_artifacts", [])
        if not any(
            isinstance(a, dict) and a.get("audit_id") == audit_id for a in audits
        ):
            payload = {"error": f"audit_id '{audit_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not any(
            isinstance(a, dict) and a.get("artifact_id") == artifact_id for a in arts
        ):
            payload = {"error": f"artifact_id '{artifact_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        reports = data.setdefault("audit_reports", [])
        assets = data.setdefault("assets", [])

        report_id = _id_from_request("rep", request_id) or _get_next_id(
            "rep", [r.get("report_id", "") for r in reports if isinstance(r, dict)]
        )
        existing_report = next(
            (
                r
                for r in reports
                if isinstance(r, dict) and r.get("report_id") == report_id
            ),
            None,
        )
        if existing_report:
            payload = existing_report
            out = json.dumps(payload, indent=2)
            return out

        asset_id = _id_from_request("asset", request_id) or _get_next_id(
            "asset", [r.get("asset_id", "") for r in assets if isinstance(r, dict)]
        )
        mime = (
            "application/pdf"
            if (output_format or "").upper() == "PDF"
            else "application/octet-stream"
        )
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
        payload = report_row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateCombinedAuditReport",
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
                    "required": [
                        "audit_id",
                        "artifact_id",
                        "output_format",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }
