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

class GenerateAuditReportAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, report_storage_ref: str = None, file_size_bytes: int = None) -> str:
        required = ["audit_id", "report_storage_ref", "file_size_bytes"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        assets: list[dict[str, Any]] = data.get("assets", [])
        asset_id = get_next_asset_id(data)
        created_ts = get_now_timestamp()

        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": None,
            "export_profile": "PDF",
            "file_size_bytes": file_size_bytes,
            "storage_ref": report_storage_ref,
            "created_ts": created_ts,
            "dlp_scan_status": "CLEAN",
            "dlp_scan_details_nullable": None,
        }

        assets.append(new_asset)
        data["assets"] = assets
        payload = new_asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateAuditReportAsset",
                "description": "Create a PDF report asset for an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "report_storage_ref": {"type": "string"},
                        "file_size_bytes": {"type": "integer", "minimum": 0},
                    },
                    "required": ["audit_id", "report_storage_ref", "file_size_bytes"],
                },
            },
        }
