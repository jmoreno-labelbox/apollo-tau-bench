# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAlertById(Tool):
    """Retrieves an alert by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("id")
        alerts = list(data.get("alerts", {}).values())
        for alert in alerts:
            if alert.get("id") == alert_id:
                return json.dumps(alert)
        return json.dumps({"error": f"Alert with ID '{alert_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_alert_by_id",
                "description": "Retrieves an alert by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
