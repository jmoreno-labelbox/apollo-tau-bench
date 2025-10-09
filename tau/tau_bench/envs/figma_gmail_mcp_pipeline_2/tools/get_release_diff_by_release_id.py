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

class GetReleaseDiffByReleaseId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str = None) -> str:
        if not release_id:
            payload = {"error": "Missing required field: release_id"}
            out = json.dumps(payload, indent=2)
            return out

        release_diffs: list[dict[str, Any]] = data.get("release_diffs", [])
        for row in release_diffs:
            if row.get("release_id") == release_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No release_diff for release_id '{release_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDiffByReleaseId",
                "description": "Fetch the release_diff row for a given release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }
