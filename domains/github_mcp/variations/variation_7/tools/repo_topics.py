from tau_bench.envs.tool import Tool
import json
from typing import Any

class RepoTopics(Tool):
    """Define or display repository topics (a simple list of strings)."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, topics: list = None) -> str:
        owner = owner or _actor_name(data)
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        if isinstance(topics, list):
            r["topics"] = [str(t) for t in topics]
        payload = {"topics": r.get("topics", [])}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RepoTopics",
                "description": "Set or get repo topics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "topics": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo"],
                },
            },
        }
