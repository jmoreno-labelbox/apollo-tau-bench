from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class EscalateSiemAlertTool(Tool):
    """Increase the severity of a SIEM alert and optionally generate an incident ticket."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None, severity: str = None, reason: str = None) -> str:
        alerts = data.get("siem_alerts", {}).values()

        alert = next((a for a in alerts.values() if a["alert_id"] == alert_id), None)
        if not alert:
            payload = {"error": f"Alert {alert_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        severity_order = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

        # Thoroughly verify severity value prior to using .index()
        if not severity or severity not in severity_order:
            payload = {"error": "Invalid severity level"}
            out = json.dumps(payload, indent=2)
            return out
        if alert["severity"] not in severity_order:
            payload = {"error": "Existing severity value invalid"}
            out = json.dumps(payload, indent=2)
            return out
        if severity_order.index(severity) <= severity_order.index(alert["severity"]):
            payload = {"error": "Only escalation permitted"}
            out = json.dumps(payload, indent=2)
            return out

        alert["severity"] = severity
        payload = {"success": f"Alert {alert_id} escalated to {severity}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EscalateSiemAlert",
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
            },
        }
