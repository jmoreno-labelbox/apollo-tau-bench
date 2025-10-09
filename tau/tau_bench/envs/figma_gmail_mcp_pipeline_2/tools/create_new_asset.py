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

class CreateNewAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, export_profile: str = None, file_size_bytes: int = None, storage_ref: str = None) -> str:
        required = ["artifact_id", "export_profile", "file_size_bytes", "storage_ref"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

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
                "name": "CreateNewAsset",
                "description": "Create a new asset row for an artifact. Defaults: dlp_scan_status=CLEAN, dlp_scan_details_nullable=null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "export_profile": {"type": "string"},
                        "file_size_bytes": {"type": "integer", "minimum": 0},
                        "storage_ref": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "export_profile",
                        "file_size_bytes",
                        "storage_ref",
                    ],
                },
            },
        }
