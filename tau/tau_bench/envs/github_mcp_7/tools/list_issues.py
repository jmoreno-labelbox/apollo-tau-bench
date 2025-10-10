# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListIssues(Tool):
    """List issues for a repo with optional state filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        state = kwargs.get("state")
        result = [i for i in _issues(data) if i.get("owner") == owner and i.get("repo") == repo]
        if state:
            result = [i for i in result if i.get("state") == state]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_issues",
                "description": "List issues in a repository (optionally by state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "state": {"type": "string", "enum": ["open", "closed"]}
                    },
                    "required": ["repo"]
                }
            },
        }
