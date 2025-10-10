# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHeadSha(Tool):
    """Returns the SHA of the latest commit on a given branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name, branch = kwargs.get("repo_name"), kwargs.get("branch")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        return json.dumps({"branch": repo["branches"][idx], "sha": repo["branch_shas"][idx]}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_head_sha",
                "description": "Gets the SHA of the head commit on a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name"]
                }
            }
        }
