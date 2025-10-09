from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateSiemAlert(Tool):
    """
    Establish a new SIEM alert for security incidents.

    kwargs:
      user_id: str (mandatory) - ID of the user initiating the alert
      resource_id: str (mandatory) - ID of the resource involved
      alert_type: str (default: "UNAUTHORIZED_ACCESS_ATTEMPT")
      severity: str (default: "HIGH") - CRITICAL, HIGH, MEDIUM, LOW
      timestamp: str ISO (defaults to now)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str = "", 
        resource_id: str = "", 
        alert_type: str = "UNAUTHORIZED_ACCESS_ATTEMPT", 
        severity: str = "HIGH", 
        timestamp: str = None
    ) -> str:
        if timestamp is None:
            timestamp = get_current_timestamp()

        if not user_id or not resource_id:
            payload = {"error": "user_id and resource_id required"}
            out = json.dumps(payload)
            return out

        # Confirm severity
        valid_severities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if severity not in valid_severities:
            payload = {"error": f"severity must be one of: {valid_severities}"}
            out = json.dumps(payload)
            return out

        # Confirm the user is present
        users = data.get("users", [])
        user = _find_by_id(users, "user_id", user_id)
        if not user:
            payload = {"error": f"User {user_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the resource is present
        resources = data.get("resources", [])
        resource = _find_by_id(resources, "resource_id", resource_id)
        if not resource:
            payload = {"error": f"Resource {resource_id} not found"}
            out = json.dumps(payload)
            return out

        alert_id = _next_id(data, "siem_alerts", "ALRT")

        alert_record = {
            "alert_id": alert_id,
            "timestamp": timestamp,
            "user_id": user_id,
            "resource_id": resource_id,
            "alert_type": alert_type,
            "severity": severity,
        }

        data.setdefault("siem_alerts", []).append(alert_record)
        payload = {"ok": True, "siem_alert": alert_record}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSiemAlert",
                "description": "Create a new SIEM alert for security incidents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "ID of the user triggering the alert.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "ID of the resource involved.",
                        },
                        "alert_type": {
                            "type": "string",
                            "description": "Type of alert.",
                            "default": "UNAUTHORIZED_ACCESS_ATTEMPT",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Alert severity: CRITICAL, HIGH, MEDIUM, LOW.",
                            "default": "HIGH",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO timestamp (optional).",
                        },
                    },
                    "required": ["user_id", "resource_id"],
                    "additionalProperties": False,
                },
            },
        }
