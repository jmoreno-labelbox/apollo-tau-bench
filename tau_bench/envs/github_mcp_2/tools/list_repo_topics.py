from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListRepoTopics(Tool):
    """Enumerates all topics associated with a specified repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        repo = _find_repo_record(data, repo_name)
        payload = {"topics": repo.get("topics", [])}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListRepoTopics",
                "description": "Returns the list of repository topics.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
