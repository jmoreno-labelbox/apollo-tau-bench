# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAlertState(Tool):
    """Updates the state of an alert."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("id")
        new_state = kwargs.get("state")
        alerts = list(data.get("alerts", {}).values())
        for alert in alerts:
            if alert.get("id") == alert_id:
                alert["state"] = new_state
                return json.dumps({"status": "success", "message": f"State for alert '{alert_id}' updated to '{new_state}'."})
        return json.dumps({"error": f"Alert with ID '{alert_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_alert_state",
                "description": "Updates the state of an alert.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "state": {"type": "string"}
                    },
                    "required": ["id", "state"],
                },
            },
        }
