from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class SetRepositoryVisibility(Tool):
    """Modifies the visibility status of a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, visibility: str = None) -> str:
        _auth(data)["username"]

        if not all([repo_name, visibility]):
            payload = {"error": "repo_name and visibility are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        repo = _find_repo_record(data, repo_name)
        if visibility not in ["public", "private"]:
            payload = {"error": "Invalid visibility. Must be 'public' or 'private'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repo["visibility"] = visibility
        payload = {
                "message": "Visibility updated",
                "repo_name": repo_name,
                "visibility": visibility,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetRepositoryVisibility",
                "description": "Updates visibility of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string", "enum": ["public", "private"]},
                    },
                    "required": ["repo_name", "visibility"],
                },
            },
        }
