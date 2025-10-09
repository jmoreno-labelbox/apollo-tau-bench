from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListAssetsForArtifactTool(Tool):
    """Enumerate exported assets for a specified artifact."""

    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        if not artifact_id:
            payload = {"error": "artifact_id is required"}
            out = json.dumps(payload)
            return out

        assets = data.get("assets", [])
        out = []
        for a in assets:
            if a.get("artifact_id_nullable") == artifact_id:
                out.append(
                    _small_fields(a, ["asset_id", "profile", "file_name", "mime_type"])
                )
        out.sort(key=lambda r: r.get("asset_id", ""))
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAssetsForArtifact",
                "description": "List exported assets linked to the artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {"artifact_id": {"type": "string"}},
                    "required": ["artifact_id"],
                },
            },
        }
