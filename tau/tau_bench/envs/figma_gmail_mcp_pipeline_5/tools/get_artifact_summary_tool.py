# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _small_fields(row: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    """Return selected fields only (simple outputs)."""
    return {k: row.get(k) for k in fields}

def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

class GetArtifactSummaryTool(Tool):
    """Get summary details for a specific artifact."""

    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        if not artifact_id:
            return json.dumps({"error": "artifact_id is required"})

        rows = data.get("figma_artifacts", [])
        for r in rows:
            if r.get("artifact_id") == artifact_id:
                return json.dumps(_small_fields(r, [
                    "artifact_id", "artifact_name", "artifact_type", "owner_email",
                    "deep_link", "current_tags", "modified_ts"
                ]), indent=2)
        return json.dumps({"error": f"artifact_id {artifact_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_artifact_summary",
            "description":"Return concise details for a given artifact.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"}
            },"required":["artifact_id"]}
        }}