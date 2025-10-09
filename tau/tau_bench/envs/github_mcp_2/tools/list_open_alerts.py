from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListOpenAlerts(Tool):
    """Enumerates all active code-scanning alerts along with the repository, alert ID, and severity."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        alerts = _alerts(data)
        open_alerts = [
            {
                "repo_name": a.get("repo_name"),
                "alert_number": a.get("alert_number"),
                "severity": a.get("severity"),
            }
            for a in alerts
            if a.get("state") != "closed"
        ]
        payload = open_alerts
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listOpenAlerts",
                "description": "Returns open alerts across all repositories with ID and severity.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
