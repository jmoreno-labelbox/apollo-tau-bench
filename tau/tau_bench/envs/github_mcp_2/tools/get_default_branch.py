# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDefaultBranch(Tool):
    """Returns the default branch of a given repo owned by the acting user."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name) -> str:
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            return json.dumps({"default_branch": repo.get("default_branch")}, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_default_branch",
                "description": "Returns the default branch name of a given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }
