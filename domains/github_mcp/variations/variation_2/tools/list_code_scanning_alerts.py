from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListCodeScanningAlerts(Tool):
    """Enumerates all code scanning alerts for a specified repository and optional severity."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, severity: str = None) -> str:
        flat_alerts = []

        for record in _alerts(data):
            if repo_name and record.get("repo_name") != repo_name:
                continue

            for i, alert_number in enumerate(record.get("alert_numbers", [])):
                alert = {
                    "alert_number": alert_number,
                    "severity": record.get("severities", [])[i],
                    "state": record.get("states", [])[i],
                    "description": record.get("descriptions", [])[i],
                }

                if severity:
                    if alert["severity"].lower() != severity.lower():
                        continue

                flat_alerts.append(alert)
        payload = {"alerts": flat_alerts}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListCodeScanningAlerts",
                "description": "Lists all code scanning alerts optionally filtered by repository and severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                },
            },
        }
