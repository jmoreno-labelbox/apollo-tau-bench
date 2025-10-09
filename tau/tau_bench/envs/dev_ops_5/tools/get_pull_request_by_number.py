from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPullRequestByNumber(Tool):
    """Fetches a pull request using its repository and number."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_id: str = None, number: int = None) -> str:
        prs = data.get("pull_requests", {}).values()
        for pr in prs:
            if pr.get("repository_id") == repository_id and pr.get("number") == number:
                payload = pr
                out = json.dumps(payload)
                return out
        payload = {"error": f"PR #{number} in repo '{repository_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPullRequestByNumber",
                "description": "Retrieves a pull request by its repository and number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string"},
                        "number": {"type": "integer"},
                    },
                    "required": ["repository_id", "number"],
                },
            },
        }
