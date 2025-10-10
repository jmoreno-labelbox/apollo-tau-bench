# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListBranches(Tool):
    """Lists all branches in a given repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        try:
            for repo in _repos(data):
                if repo.get("repo_name") == repo_name:
                    return json.dumps({"branches": repo.get("branches", [])}, indent=2)
            return json.dumps({"error": f"Repository not found: {repo_name}"}, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_branches",
                "description": "Returns all branches in the given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }
