# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateAuditReportAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["audit_id", "report_storage_ref", "file_size_bytes"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        assets: List[Dict[str, Any]] = data.get("assets", [])
        asset_id = get_next_asset_id(data)
        created_ts = get_now_timestamp()

        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": None,
            "export_profile": "PDF",
            "file_size_bytes": kwargs["file_size_bytes"],
            "storage_ref": kwargs["report_storage_ref"],
            "created_ts": created_ts,
            "dlp_scan_status": "CLEAN",
            "dlp_scan_details_nullable": None
        }

        assets.append(new_asset)
        data["assets"] = assets
        return json.dumps(new_asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_audit_report_asset",
                "description": "Create a PDF report asset for an audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "report_storage_ref": {"type": "string"},
                        "file_size_bytes": {"type": "integer", "minimum": 0}
                    },
                    "required": ["audit_id", "report_storage_ref", "file_size_bytes"]
                }
            }
        }
