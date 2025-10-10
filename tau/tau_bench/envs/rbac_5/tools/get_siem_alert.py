# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSiemAlert(Tool):
    """
    Retrieve SIEM alerts by ID, user, resource, or severity.

    kwargs:
      alert_id: str (optional) - Specific alert ID to retrieve
      user_id: str (optional) - Filter by user who triggered alerts
      resource_id: str (optional) - Filter by resource involved in alerts
      severity: str (optional) - Filter by severity (CRITICAL, HIGH, MEDIUM, LOW)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], alert_id, resource_id, severity, user_id) -> str:

        siem_alerts = data.get("siem_alerts", [])

        # Return a single alert if alert_id is specified.
        if alert_id:
            alert = _find_by_id(siem_alerts, "alert_id", alert_id)
            if not alert:
                return json.dumps({"error": f"SIEM alert {alert_id} not found"})
            return json.dumps({"ok": True, "siem_alert": alert})

        # Refine alerts according to specified parameters.
        filtered_alerts = []
        for alert in siem_alerts:
            if user_id and alert.get("user_id") != user_id:
                continue
            if resource_id and alert.get("resource_id") != resource_id:
                continue
            if severity and alert.get("severity") != severity:
                continue
            filtered_alerts.append(alert)

        return json.dumps({"ok": True, "siem_alerts": filtered_alerts})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_siem_alert",
                "description": "Retrieve SIEM alerts by ID, user, resource, or severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string", "description": "Specific SIEM alert ID to retrieve."},
                        "user_id": {"type": "string", "description": "Filter by user who triggered alerts."},
                        "resource_id": {"type": "string", "description": "Filter by resource involved in alerts."},
                        "severity": {"type": "string", "description": "Filter by severity (CRITICAL, HIGH, MEDIUM, LOW)."}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
