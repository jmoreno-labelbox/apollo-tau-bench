# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _prs(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("pull_requests", [])

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class ListPRs(Tool):
    """List pull requests for a repo with optional state filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo, state) -> str:
        owner = owner or _actor_name(data)
        result = [p for p in _prs(data) if p.get("owner") == owner and p.get("repo") == repo]
        if state:
            result = [p for p in result if p.get("state") == state]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_prs",
                "description": "List pull requests for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "state": {"type": "string", "enum": ["open", "closed", "merged"]}
                    },
                    "required": ["repo"]
                }
            },
        }