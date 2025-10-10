# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSiemAlertDetailsTool(Tool):
    """Retrieve details of a SIEM alert."""

    @staticmethod
    def invoke(data: Dict[str, Any], alert_id) -> str:
        aid = alert_id
        for a in data.get("siem_alerts", []):
            if a["alert_id"] == aid:
                return json.dumps(a, indent=2)
        return json.dumps({"error": f"SIEM alert {aid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_siem_alert_details",
                "description": "Get detailed information for a specific SIEM alert",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"}
                    },
                    "required": ["alert_id"]
                }
            }
        }
