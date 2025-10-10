# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ResolveAlert(Tool):
    """Resolve a code scanning alert by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        alert_id = kwargs.get("alert_id")
        for a in _alerts(data):
            if a.get("owner") == owner and a.get("repo") == repo and a.get("id") == alert_id:
                a["state"] = "resolved"
                a["resolved_at"] = get_current_timestamp()
                return json.dumps(a)
        raise RuntimeError("Alert not found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolve_alert",
                "description": "Mark a code scanning alert as resolved.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "alert_id": {"type": "string"}
                    },
                    "required": ["repo", "alert_id"]
                }
            },
        }
