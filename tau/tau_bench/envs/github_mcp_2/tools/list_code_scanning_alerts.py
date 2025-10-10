# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCodeScanningAlerts(Tool):
    """Lists all code scanning alerts for a given repository and optional severity."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name, severity) -> str:
        severity_filter = severity

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

                if severity_filter:
                    if alert["severity"].lower() != severity_filter.lower():
                        continue

                flat_alerts.append(alert)

        return json.dumps({"alerts": flat_alerts}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_code_scanning_alerts",
                "description": "Lists all code scanning alerts optionally filtered by repository and severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                }
            }
        }
