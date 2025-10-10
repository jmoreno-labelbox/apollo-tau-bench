# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSiemAlerts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:

        matching_alerts = [
                alert for alert in data.get('siem_alerts', [])
                if alert.get('user_id') == user_id
        ]

        return json.dumps({"alerts": matching_alerts})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_siem_alerts",
                        "description": "Retrieves a list of SIEM alerts based on the user's ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {
                                                "type": "string",
                                                "description": "The user_id to retrieve SIEM alerts for."
                                        }
                                },
                                "required": ["user_id"]
                        }
                }
        }
