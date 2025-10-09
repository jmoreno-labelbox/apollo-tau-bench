from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateArtifactMetadata(Tool):
    """Modify artifact.metadata with specified keys in a deterministic manner."""

    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, metadata_patch: dict[str, Any] = {}) -> str:
        rows = data.get("artifacts", {}).values()
        idx = _idx_by_id(rows, artifact_id)
        if idx is None:
            payload = {"artifact": None}
            out = json.dumps(payload, indent=2)
            return out
        art = rows[idx]
        art.setdefault("metadata", {}).values()
        art["metadata"].update(metadata_patch)
        rows[idx] = art
        payload = {"artifact": art}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateArtifactMetadata",
                "description": "Apply a shallow patch to artifact.metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "metadata_patch": {"type": "object"},
                    },
                    "required": ["artifact_id", "metadata_patch"],
                },
            },
        }
