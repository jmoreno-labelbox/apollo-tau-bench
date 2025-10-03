from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class export_assets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        export_profile: str = None,
        request_id: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "artifact_id": artifact_id,
            "export_profile": export_profile,
            "request_id": request_id,
            "timestamp": timestamp
        })
        miss = _require(p, ["artifact_id", "export_profile", "request_id", "timestamp"])
        if miss:
            return miss
        ext = _export_ext_from_profile(p["export_profile"])
        ymd = _ymd(p["timestamp"])
        export_id = f"exp-{p['artifact_id']}-{ymd}-{ext}-001"
        asset_id = f"asset_{p['request_id']}"
        asset = {
            "asset_id": asset_id,
            "export_id": export_id,
            "artifact_id": p["artifact_id"],
        }
        _ensure(data, "assets", []).append(asset)
        return _ok({"asset_id": asset_id, "export_id": export_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportAssets",
                "description": "Export assets for an artifact using an export profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "export_profile": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "export_profile",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }
