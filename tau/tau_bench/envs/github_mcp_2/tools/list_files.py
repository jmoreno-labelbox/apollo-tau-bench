from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListFiles(Tool):
    """Enumerates all file paths within the specified branch of a repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        files = repo["branch_files"][idx]
        payload = {"files": files}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListFiles",
                "description": "Lists all files in a given branch of a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }
