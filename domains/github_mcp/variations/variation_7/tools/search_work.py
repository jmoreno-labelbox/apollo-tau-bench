from tau_bench.envs.tool import Tool
import json
from typing import Any

class SearchWork(Tool):
    """Basic text search through issue and pull request titles."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, query: str = None) -> str:
        owner = owner or _actor_name(data)
        q = (query or "").lower()
        hits_issues = [
            i
            for i in _issues(data)
            if i.get("owner") == owner
            and i.get("repo") == repo
            and q in (i.get("title", "") + " " + i.get("body", "")).lower()
        ]
        hits_prs = [
            p
            for p in _prs(data)
            if p.get("owner") == owner
            and p.get("repo") == repo
            and q in (p.get("title", "") or "").lower()
        ]
        payload = {"issues": hits_issues, "pull_requests": hits_prs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchWork",
                "description": "Search issues and PRs by text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "query": {"type": "string"},
                    },
                    "required": ["repo", "query"],
                },
            },
        }
