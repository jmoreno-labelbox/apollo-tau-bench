from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetReleaseById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str = None) -> str:
        if not release_id:
            payload = {"error": "Missing required field: release_id"}
            out = json.dumps(payload, indent=2)
            return out

        releases: list[dict[str, Any]] = data.get("releases", {}).values()
        for row in releases:
            if row.get("release_id") == release_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No release with id '{release_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getReleaseById",
                "description": "Fetch a single release by release_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }
