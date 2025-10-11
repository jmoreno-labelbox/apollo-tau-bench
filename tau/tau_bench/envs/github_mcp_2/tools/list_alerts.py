# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _alerts(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("code_scanning_alerts", [])

class ListAlerts(Tool):
    """Returns code scanning alerts for a given repository."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name) -> str:
        if not repo_name:
            return json.dumps({"error": "repo_name is required."}, indent=2)

        alerts = _alerts(data)
        filtered = [
            {
                "alert_number": a.get("alert_number"),
                "rule": a.get("rule"),
                "severity": a.get("severity"),
                "state": a.get("state"),
                "dismissed": a.get("dismissed", False)
            }
            for a in alerts
            if a.get("repo_name") == repo_name
        ]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_alerts",
                "description": "Returns code scanning alerts for a given repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"}
                    },
                    "required": ["repo_name"]
                }
            }
        }