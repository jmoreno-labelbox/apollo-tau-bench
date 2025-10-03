from tau_bench.envs.tool import Tool
import json
from typing import Any

class ResolveAlert(Tool):
    """Address a code scanning alert using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, alert_id: str = None) -> str:
        owner = owner or _actor_name(data)
        for a in _alerts(data):
            if (
                a.get("owner") == owner
                and a.get("repo") == repo
                and a.get("id") == alert_id
            ):
                a["state"] = "resolved"
                a["resolved_at"] = get_current_timestamp()
                payload = a
                out = json.dumps(payload)
                return out
        raise RuntimeError("Alert not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolveAlert",
                "description": "Mark a code scanning alert as resolved.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "alert_id": {"type": "string"},
                    },
                    "required": ["repo", "alert_id"],
                },
            },
        }
