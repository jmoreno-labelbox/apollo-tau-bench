# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSiemAlertById(Tool):
    """ Get the full details of a specific SIEM alert using its ID. """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("alert_id")
        try:
            siem_alerts = data.get('siem_alerts', [])
        except:
            siem_alerts = []

        for alert in siem_alerts:
            if alert.get("alert_id") == alert_id:
                return json.dumps(alert)

        return json.dumps({"error": f"SIEM alert with ID '{alert_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_siem_alert_by_id",
                "description": "Retrieves the full details of a specific SIEM alert using its unique ID (e.g., 'ALRT-012').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {
                            "type": "string",
                            "description": "The unique ID of the SIEM alert to retrieve."
                        }
                    },
                    "required": ["alert_id"]
                }
            }
        }
