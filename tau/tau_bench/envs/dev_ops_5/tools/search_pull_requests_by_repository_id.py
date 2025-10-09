from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchPullRequestsByRepositoryId(Tool):
    """Looks for all pull requests in a particular repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_id: str = None) -> str:
        pull_requests = data.get("pull_requests", {}).values()

        matching_prs = [
            pr for pr in pull_requests.values() if pr.get("repository_id") == repository_id
        ]
        payload = {"pull_requests": matching_prs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchPullRequestsByRepositoryId",
                "description": "Searches for all pull requests within a specific repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {
                            "type": "string",
                            "description": "The unique ID of the repository to search within.",
                        }
                    },
                    "required": ["repository_id"],
                },
            },
        }
