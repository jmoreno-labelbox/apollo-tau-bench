from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetSiemAlertTool(Tool):
    """Get information about a specific SIEM alert (read-only, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str) -> str:
        alerts = data.get("siem_alerts", [])
        if not isinstance(alerts, list):
            payload = {"error": "siem_alerts must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(alert_id, str) or not alert_id.strip():
            payload = {"error": "alert_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for a in alerts:
            if a.get("alert_id") == alert_id:
                payload = a
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"alert_id {alert_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlert",
                "description": "Retrieve SIEM alert details by alert_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"alert_id": {"type": "string"}},
                    "required": ["alert_id"],
                },
            },
        }
