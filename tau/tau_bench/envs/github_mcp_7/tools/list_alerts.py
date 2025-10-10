# Copyright ownership held by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAlerts(Tool):
    """List code scanning alerts for a repo."""
    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo) -> str:
        owner = owner or _actor_name(data)
        result = [a for a in _alerts(data) if a.get("owner") == owner and a.get("repo") == repo]
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_alerts",
                "description": "List static analysis / scanning alerts for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"owner": {"type": "string"}, "repo": {"type": "string"}},
                    "required": ["repo"]
                }
            },
        }
