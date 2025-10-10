# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAssetsForArtifactTool(Tool):
    """List exported assets for a given artifact."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        if not artifact_id:
            return json.dumps({"error":"artifact_id is required"})

        assets = data.get("assets", [])
        out = []
        for a in assets:
            if a.get("artifact_id_nullable") == artifact_id:
                out.append(_small_fields(a, ["asset_id","profile","file_name","mime_type"]))
        out.sort(key=lambda r: r.get("asset_id",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_assets_for_artifact",
            "description":"List exported assets linked to the artifact.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"}
            },"required":["artifact_id"]}
        }}
