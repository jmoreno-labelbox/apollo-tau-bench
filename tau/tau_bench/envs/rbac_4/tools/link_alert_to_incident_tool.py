# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkAlertToIncidentTool(Tool):
    """Link an existing SIEM alert to an incident record (write operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        incidents = list(data.get("incidents", {}).values())
        alerts = data.get("siem_alerts", [])

        if not isinstance(incidents, list):
            return json.dumps({"error": "incidents must be a list"}, indent=2)
        if not isinstance(alerts, list):
            return json.dumps({"error": "siem_alerts must be a list"}, indent=2)

        incident_id = kwargs.get("incident_id")
        alert_id = kwargs.get("alert_id")

        if not isinstance(incident_id, str) or not incident_id.strip():
            return json.dumps({"error": "incident_id must be a non-empty string"}, indent=2)
        if not isinstance(alert_id, str) or not alert_id.strip():
            return json.dumps({"error": "alert_id must be a non-empty string"}, indent=2)

        incident = next((i for i in incidents if i.get("incident_id") == incident_id), None)
        if not incident:
            return json.dumps({"error": f"Incident {incident_id} not found"}, indent=2)

        alert = next((a for a in alerts if a.get("alert_id") == alert_id), None)
        if not alert:
            return json.dumps({"error": f"Alert {alert_id} not found"}, indent=2)

        linked = incident.setdefault("linked_alerts", [])
        if alert_id not in linked:
            linked.append(alert_id)

        return json.dumps(
            {"success": f"Linked alert {alert_id} to incident {incident_id}",
             "incident_id": incident_id,
             "alert_id": alert_id},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_alert_to_incident",
                "description": "Append an alert_id to an incident's linked_alerts after validating existence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "incident_id": {"type": "string"},
                        "alert_id": {"type": "string"}
                    },
                    "required": ["incident_id", "alert_id"]
                },
            },
        }
