# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["artifact_id", "export_profile", "file_size_bytes", "storage_ref"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        artifact_id = kwargs.get("artifact_id")
        export_profile = kwargs.get("export_profile")
        file_size_bytes = kwargs.get("file_size_bytes")
        storage_ref = kwargs.get("storage_ref")

        assets = data.get("assets", [])
        asset_id = get_next_asset_id(data)
        created_ts = get_now_timestamp()

        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": export_profile,
            "file_size_bytes": file_size_bytes,
            "storage_ref": storage_ref,
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
                "name": "create_new_asset",
                "description": "Create a new asset row for an artifact. Defaults: dlp_scan_status=CLEAN, dlp_scan_details_nullable=null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "export_profile": {"type": "string"},
                        "file_size_bytes": {"type": "integer", "minimum": 0},
                        "storage_ref": {"type": "string"}
                    },
                    "required": ["artifact_id", "export_profile", "file_size_bytes", "storage_ref"]
                }
            }
        }
