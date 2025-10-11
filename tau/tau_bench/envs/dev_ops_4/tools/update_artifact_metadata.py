# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    for i, r in enumerate(rows):
        if r.get("id") == _id:
            return i
    return None

class UpdateArtifactMetadata(Tool):
    """Patch artifact.metadata with provided keys deterministically."""
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id, metadata_patch = {}) -> str:
        rows = list(data.get("artifacts", {}).values())
        idx = _idx_by_id(rows, artifact_id)
        if idx is None:
            return json.dumps({"artifact": None}, indent=2)
        art = rows[idx]
        art.setdefault("metadata", {})
        art["metadata"].update(metadata_patch)
        rows[idx] = art
        return json.dumps({"artifact": art}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_artifact_metadata",
                "description": "Apply a shallow patch to artifact.metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "metadata_patch": {"type": "object"}
                    },
                    "required": ["artifact_id", "metadata_patch"]
                }
            }
        }