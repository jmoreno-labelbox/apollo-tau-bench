# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListFiles(Tool):
    """Lists all file paths in the given branch of a repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name, branch = kwargs.get("repo_name"), kwargs.get("branch")
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        files = repo["branch_files"][idx]
        return json.dumps({"files": files}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_files",
                "description": "Lists all files in a given branch of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo_name", "branch"]
                }
            }
        }
