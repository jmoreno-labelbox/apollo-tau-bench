# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EscalateSiemAlertTool(Tool):
    """Escalate the severity of a SIEM alert and optionally create an incident ticket."""

    @staticmethod
    def invoke(data: Dict[str, Any], alert_id, reason, severity) -> str:
        alerts = data.get("siem_alerts", [])
        new_severity = severity

        alert = next((a for a in alerts if a["alert_id"] == alert_id), None)
        if not alert:
            return json.dumps({"error": f"Alert {alert_id} not found"}, indent=2)

        severity_order = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

        # Thoroughly validate the severity value prior to invoking .index().
        if not new_severity or new_severity not in severity_order:
            return json.dumps({"error": "Invalid severity level"}, indent=2)
        if alert["severity"] not in severity_order:
            return json.dumps({"error": "Existing severity value invalid"}, indent=2)
        if severity_order.index(new_severity) <= severity_order.index(alert["severity"]):
            return json.dumps({"error": "Only escalation permitted"}, indent=2)

        alert["severity"] = new_severity

        return json.dumps({"success": f"Alert {alert_id} escalated to {new_severity}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "escalate_siem_alert",
                "description": (
                    "Escalate SIEM alert severity. Only escalation (not downgrade) allowed."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"},
                        "severity": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["alert_id", "severity", "reason"],
                },
            }
        }
