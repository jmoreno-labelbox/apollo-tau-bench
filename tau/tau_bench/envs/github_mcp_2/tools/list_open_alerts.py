# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _alerts(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("code_scanning_alerts", [])

class ListOpenAlerts(Tool):
    """Lists all open code-scanning alerts with repo, alert ID, and severity."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alerts = _alerts(data)
        open_alerts = [
            {
                "repo_name": a.get("repo_name"),
                "alert_number": a.get("alert_number"),
                "severity": a.get("severity")
            }
            for a in alerts
            if a.get("state") != "closed"
        ]
        return json.dumps(open_alerts, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_open_alerts",
                "description": "Returns open alerts across all repositories with ID and severity.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }