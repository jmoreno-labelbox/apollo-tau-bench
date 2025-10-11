# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetRepositoryVisibility(Tool):
    """Changes the visibility of a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, visibility) -> str:
        me = _auth(data)["username"]

        if not all([repo_name, visibility]):
            return json.dumps({"error": "repo_name and visibility are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        if visibility not in ["public", "private"]:
            return json.dumps({"error": "Invalid visibility. Must be 'public' or 'private'."}, indent=2)

        repo["visibility"] = visibility
        return json.dumps({"message": "Visibility updated", "repo_name": repo_name, "visibility": visibility}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_repository_visibility",
                "description": "Updates visibility of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "visibility": {"type": "string", "enum": ["public", "private"]}
                    },
                    "required": ["repo_name", "visibility"]
                }
            }
        }
