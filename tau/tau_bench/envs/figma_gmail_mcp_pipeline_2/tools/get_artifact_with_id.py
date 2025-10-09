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

class GetArtifactWithId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None) -> str:
        if not artifact_id:
            payload = {"error": "Missing required field: artifact_id"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        artifacts = data.get("figma_artifacts", [])
        for row in artifacts:
            if row.get("artifact_id") == artifact_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No artifact with id '{artifact_id}'."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getArtifactWithId",
                "description": "Fetch a single Figma artifact by artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"artifact_id": {"type": "string"}},
                    "required": ["artifact_id"],
                },
            },
        }
