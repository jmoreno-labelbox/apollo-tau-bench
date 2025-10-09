from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListBranches(Tool):
    """Enumerates all branches within a specified repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            for repo in _repos(data):
                if repo.get("repo_name") == repo_name:
                    payload = {"branches": repo.get("branches", [])}
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Repository not found: {repo_name}"}
            out = json.dumps(payload, indent=2)
            return out
        except Exception as e:
            payload = {"error": str(e)}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListBranches",
                "description": "Returns all branches in the given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
