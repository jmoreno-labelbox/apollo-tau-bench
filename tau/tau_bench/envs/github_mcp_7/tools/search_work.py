# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchWork(Tool):
    """Simple text search across issues and PR titles."""
    @staticmethod
    def invoke(data: Dict[str, Any], owner, query, repo) -> str:
        owner = owner or _actor_name(data)
        q = (query or "").lower()
        hits_issues = [i for i in _issues(data) if i.get("owner") == owner and i.get("repo") == repo and q in (i.get("title", "") + " " + i.get("body", "")).lower()]
        hits_prs = [p for p in _prs(data) if p.get("owner") == owner and p.get("repo") == repo and q in (p.get("title", "") or "").lower()]
        return json.dumps({"issues": hits_issues, "pull_requests": hits_prs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_work",
                "description": "Search issues and PRs by text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "query": {"type": "string"}
                    },
                    "required": ["repo", "query"]
                }
            },
        }
