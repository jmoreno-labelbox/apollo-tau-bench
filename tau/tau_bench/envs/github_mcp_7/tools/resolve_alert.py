# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _alerts(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("code_scanning_alerts", [])

def _actor_name(data: Dict[str, Any]) -> str:
    auth = data.get("authentication") or [{}]
    return auth[0].get("username") or "anonymous"

class ResolveAlert(Tool):
    """Resolve a code scanning alert by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], alert_id, owner, repo) -> str:
        owner = owner or _actor_name(data)
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