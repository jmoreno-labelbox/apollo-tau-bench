# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCommits(Tool):
    """List commits for a repo (optional branch filter)."""
    @staticmethod
    def invoke(data: Dict[str, Any], branch, owner, repo) -> str:
        owner = owner or _actor_name(data)
        result = [c for c in _commits(data) if c.get("owner") == owner and c.get("repo") == repo]
        if branch:
            result = [c for c in result if c.get("branch") == branch]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_commits",
                "description": "List commit records for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo"]
                }
            },
        }
