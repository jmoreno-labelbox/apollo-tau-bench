# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSiemAlert(Tool):
    """
    Create a new SIEM alert for security incidents.

    kwargs:
      user_id: str (required) - ID of the user triggering the alert
      resource_id: str (required) - ID of the resource involved
      alert_type: str (default: "UNAUTHORIZED_ACCESS_ATTEMPT")
      severity: str (default: "HIGH") - CRITICAL, HIGH, MEDIUM, LOW
      timestamp: str ISO (defaults now)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id", "")
        resource_id = kwargs.get("resource_id", "")
        alert_type = kwargs.get("alert_type", "UNAUTHORIZED_ACCESS_ATTEMPT")
        severity = kwargs.get("severity", "HIGH")
        timestamp = kwargs.get("timestamp") or get_current_timestamp()

        if not user_id or not resource_id:
            return json.dumps({"error": "user_id and resource_id required"})

        # Validate severity
        valid_severities = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
        if severity not in valid_severities:
            return json.dumps({"error": f"severity must be one of: {valid_severities}"})

        # Validate user exists
        users = list(data.get("users", {}).values())
        user = _find_by_id(users, "user_id", user_id)
        if not user:
            return json.dumps({"error": f"User {user_id} not found"})

        # Validate resource exists
        resources = data.get("resources", [])
        resource = _find_by_id(resources, "resource_id", resource_id)
        if not resource:
            return json.dumps({"error": f"Resource {resource_id} not found"})

        alert_id = _next_id(data, "siem_alerts", "ALRT")

        alert_record = {
            "alert_id": alert_id,
            "timestamp": timestamp,
            "user_id": user_id,
            "resource_id": resource_id,
            "alert_type": alert_type,
            "severity": severity
        }

        data.setdefault("siem_alerts", []).append(alert_record)
        return json.dumps({"ok": True, "siem_alert": alert_record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_siem_alert",
                "description": "Create a new SIEM alert for security incidents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "ID of the user triggering the alert."},
                        "resource_id": {"type": "string", "description": "ID of the resource involved."},
                        "alert_type": {"type": "string", "description": "Type of alert.", "default": "UNAUTHORIZED_ACCESS_ATTEMPT"},
                        "severity": {"type": "string", "description": "Alert severity: CRITICAL, HIGH, MEDIUM, LOW.", "default": "HIGH"},
                        "timestamp": {"type": "string", "description": "ISO timestamp (optional)."}
                    },
                    "required": ["user_id", "resource_id"],
                    "additionalProperties": False
                }
            }
        }
