from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListAlerts(Tool):
    """Delivers code scanning alerts for a specified repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        if not repo_name:
            payload = {"error": "repo_name is required."}
            out = json.dumps(payload, indent=2)
            return out

        alerts = _alerts(data)
        filtered = [
            {
                "alert_number": a.get("alert_number"),
                "rule": a.get("rule"),
                "severity": a.get("severity"),
                "state": a.get("state"),
                "dismissed": a.get("dismissed", False),
            }
            for a in alerts
            if a.get("repo_name") == repo_name
        ]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listAlerts",
                "description": "Returns code scanning alerts for a given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
