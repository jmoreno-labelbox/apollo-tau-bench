from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetArtifactSummaryTool(Tool):
    """Retrieve summary information for a particular artifact."""

    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        if not artifact_id:
            payload = {"error": "artifact_id is required"}
            out = json.dumps(payload)
            return out

        rows = data.get("figma_artifacts", {}).values()
        for r in rows.values():
            if r.get("artifact_id") == artifact_id:
                payload = _small_fields(
                        r,
                        [
                            "artifact_id",
                            "artifact_name",
                            "artifact_type",
                            "owner_email",
                            "deep_link",
                            "current_tags",
                            "modified_ts",
                        ],
                    )
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"artifact_id {artifact_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetArtifactSummary",
                "description": "Return concise details for a given artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {"artifact_id": {"type": "string"}},
                    "required": ["artifact_id"],
                },
            },
        }
