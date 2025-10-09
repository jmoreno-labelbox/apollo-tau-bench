from tau_bench.envs.tool import Tool
import json
from typing import Any

class LinkAlertToIncidentTool(Tool):
    """Connect an existing SIEM alert to an incident record (write operation, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], incident_id: str = None, alert_id: str = None) -> str:
        incidents = data.get("incidents", [])
        alerts = data.get("siem_alerts", [])

        if not isinstance(incidents, list):
            payload = {"error": "incidents must be a list"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(alerts, list):
            payload = {"error": "siem_alerts must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(incident_id, str) or not incident_id.strip():
            payload = {"error": "incident_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if not isinstance(alert_id, str) or not alert_id.strip():
            payload = {"error": "alert_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        incident = next(
            (i for i in incidents if i.get("incident_id") == incident_id), None
        )
        if not incident:
            payload = {"error": f"Incident {incident_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        alert = next((a for a in alerts if a.get("alert_id") == alert_id), None)
        if not alert:
            payload = {"error": f"Alert {alert_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        linked = incident.setdefault("linked_alerts", [])
        if alert_id not in linked:
            linked.append(alert_id)
        payload = {
                "success": f"Linked alert {alert_id} to incident {incident_id}",
                "incident_id": incident_id,
                "alert_id": alert_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkAlertToIncident",
                "description": "Append an alert_id to an incident's linked_alerts after validating existence.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "incident_id": {"type": "string"},
                        "alert_id": {"type": "string"},
                    },
                    "required": ["incident_id", "alert_id"],
                },
            },
        }
