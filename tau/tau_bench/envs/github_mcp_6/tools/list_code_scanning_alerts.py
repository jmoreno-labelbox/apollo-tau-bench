# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCodeScanningAlerts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str) -> str:
        """List code scanning alerts for a repo."""
        alerts_data = data.get("code_scanning_alerts", [])

        for alert_entry in alerts_data:
            if alert_entry["owner"] == owner and alert_entry["repo_name"] == repo:
                alerts = []
                for i, alert_num in enumerate(alert_entry["alert_numbers"]):
                    alerts.append({
                        "number": alert_num,
                        "severity": alert_entry["severities"][i],
                        "state": alert_entry["states"][i],
                        "ref": alert_entry["refs"][i]
                    })
                return json.dumps({"alerts": alerts}, indent=2)

        return json.dumps({"alerts": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_code_scanning_alerts",
                "description": "List code scanning alerts for a repo.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"}
                    },
                    "required": ["owner", "repo"]
                }
            }
        }
