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

class GetReleaseDetailsByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_name: str = None) -> str:
        if not release_name:
            payload = {"error": "Missing required field: release_name"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        releases: list[dict[str, Any]] = data.get("releases", [])

        results: list[dict[str, Any]] = [
            r for r in releases if r.get("release_name") == release_name
        ]
        results.sort(key=lambda r: (str(r.get("created_ts")), str(r.get("release_id"))))

        if not results:
            payload = {"error": f"No release found with release_name '{release_name}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"count": len(results), "releases": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDetailsByName",
                "description": "Return releases matching an exact release_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_name": {"type": "string"}},
                    "required": ["release_name"],
                },
            },
        }
