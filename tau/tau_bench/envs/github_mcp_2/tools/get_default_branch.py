from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetDefaultBranch(Tool):
    """Delivers the default branch of a specified repository owned by the acting user."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            repo = _find_repo_record(data, repo_name)
            payload = {"default_branch": repo.get("default_branch")}
            out = json.dumps(payload, indent=2)
            return out
        except Exception as e:
            payload = {"error": str(e)}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDefaultBranch",
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
