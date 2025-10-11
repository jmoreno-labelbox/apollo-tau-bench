# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_repo(data: Dict[str, Any], owner: str, repo: str) -> Optional[Dict[str, Any]]:
    for r in _repos(data):
        if r.get("owner") == owner and (r.get("repo_name") or r.get("name")) == repo:
            return r
    return None

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class RepoTopics(Tool):
    """Set or list repository topics (simple list of strings)."""
    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo, topics) -> str:
        owner = owner or _actor_name(data)
        r = _find_repo(data, owner, repo)
        if not r:
            raise RuntimeError("Repository not found")
        if isinstance(topics, list):
            r["topics"] = [str(t) for t in topics]
        return json.dumps({"topics": r.get("topics", [])})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "repo_topics",
                "description": "Set or get repo topics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "topics": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["repo"]
                }
            },
        }