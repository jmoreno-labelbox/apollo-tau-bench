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

class GetAssetsByArtifactId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None) -> str:
        if not artifact_id:
            payload = {"error": "Missing required field: artifact_id"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        assets = data.get("assets", [])

        results = [
            row for row in assets if row.get("artifact_id_nullable") == artifact_id
        ]

        if not results:
            payload = {"error": f"No assets found for artifact_id '{artifact_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        results.sort(key=lambda r: str(r.get("asset_id")))
        payload = {"count": len(results), "assets": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAssetsByArtifactId",
                "description": "Return all asset objects belonging to the given artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"artifact_id": {"type": "string"}},
                    "required": ["artifact_id"],
                },
            },
        }
