# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSiemAlertTool(Tool):
    """Retrieve details of a specific SIEM alert (read-only, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], alert_id) -> str:
        alerts = data.get("siem_alerts", [])
        if not isinstance(alerts, list):
            return json.dumps({"error": "siem_alerts must be a list"}, indent=2)

        if not isinstance(alert_id, str) or not alert_id.strip():
            return json.dumps({"error": "alert_id must be a non-empty string"}, indent=2)

        for a in alerts:
            if a.get("alert_id") == alert_id:
                return json.dumps(a, indent=2)

        return json.dumps({"error": f"alert_id {alert_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_siem_alert",
                "description": "Retrieve SIEM alert details by alert_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"}
                    },
                    "required": ["alert_id"]
                }
            }
        }
