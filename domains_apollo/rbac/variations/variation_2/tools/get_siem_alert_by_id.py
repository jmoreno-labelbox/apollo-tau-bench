from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetSiemAlertById(Tool):
    """Retrieve complete details of a specific SIEM alert by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None) -> str:
        try:
            siem_alerts = data.get("siem_alerts", [])
        except:
            siem_alerts = []

        for alert in siem_alerts:
            if alert.get("alert_id") == alert_id:
                payload = alert
                out = json.dumps(payload)
                return out
        payload = {"error": f"SIEM alert with ID '{alert_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlertById",
                "description": "Retrieves the full details of a specific SIEM alert using its unique ID (e.g., 'ALRT-012').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {
                            "type": "string",
                            "description": "The unique ID of the SIEM alert to retrieve.",
                        }
                    },
                    "required": ["alert_id"],
                },
            },
        }
