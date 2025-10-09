from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetSiemAlert(Tool):
    """
    Retrieve SIEM alerts based on ID, user, resource, or severity.

    kwargs:
      alert_id: str (optional) - Specific alert ID to retrieve
      user_id: str (optional) - Filter by the user who triggered the alerts
      resource_id: str (optional) - Filter by the resource involved in the alerts
      severity: str (optional) - Filter by severity (CRITICAL, HIGH, MEDIUM, LOW)
    """

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None, user_id: str = None, resource_id: str = None, severity: str = None) -> str:
        siem_alerts = data.get("siem_alerts", [])

        # If alert_id is supplied, return the specific alert
        if alert_id:
            alert = _find_by_id(siem_alerts, "alert_id", alert_id)
            if not alert:
                payload = {"error": f"SIEM alert {alert_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "siem_alert": alert}
            out = json.dumps(payload)
            return out

        # Narrow down alerts according to the supplied criteria
        filtered_alerts = []
        for alert in siem_alerts:
            if user_id and alert.get("user_id") != user_id:
                continue
            if resource_id and alert.get("resource_id") != resource_id:
                continue
            if severity and alert.get("severity") != severity:
                continue
            filtered_alerts.append(alert)
        payload = {"ok": True, "siem_alerts": filtered_alerts}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlert",
                "description": "Retrieve SIEM alerts by ID, user, resource, or severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {
                            "type": "string",
                            "description": "Specific SIEM alert ID to retrieve.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Filter by user who triggered alerts.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Filter by resource involved in alerts.",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Filter by severity (CRITICAL, HIGH, MEDIUM, LOW).",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
