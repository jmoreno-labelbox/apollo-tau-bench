# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class export_assets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id: str, export_profile: str, timestamp: str, request_id: str) -> str:
        assets = data.setdefault("assets", [])
        day_iso = (timestamp or "").split("T")[0]
        day_compact = day_iso.replace("-", "")
        prof = (export_profile or "").upper()
        fmt = "png" if "PNG" in prof else ("pdf" if "PDF" in prof else "bin")

        asset_id = _id_from_request("asset", request_id) or _get_next_id(
            "asset", [r.get("asset_id", "") for r in assets if isinstance(r, dict)]
        )
        export_id = f"exp-{artifact_id}-{day_compact}-{fmt}-001"

        for a in assets:
            if isinstance(a, dict) and a.get("asset_id") == asset_id:
                a.setdefault("export_id", export_id)
                return json.dumps({"asset_id": asset_id, "export_id": a["export_id"]}, indent=2)

        row = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": export_profile,
            "mime_type": "image/png" if fmt == "png" else ("application/pdf" if fmt == "pdf" else "application/octet-stream"),
            "file_name": f"{artifact_id}_{export_profile.replace(' ', '').lower()}.{fmt}",
            "size_bytes": 0,
            "day": day_iso,
            "export_id": export_id,
        }
        assets.append(row)
        return json.dumps({"asset_id": asset_id, "export_id": export_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"export_assets","description":"Export/reuse an asset deterministically and return both asset_id and export_id.","parameters":{"type":"object","properties":{"artifact_id":{"type":"string"},"export_profile":{"type":"string"},"timestamp":{"type":"string"},"request_id":{"type":"string"}},"required":["artifact_id","export_profile","timestamp","request_id"]}}}
