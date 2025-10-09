from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_release_diff(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str) -> str:
        diffs = data.get("release_diffs", {}).values()
        for diff in diffs:
            if diff.get("release_id") == release_id:
                payload = diff
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Release diff for {release_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDiff",
                "description": "Retrieve the diff summary for a given release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }
