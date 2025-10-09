from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetSiemAlerts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        matching_alerts = [
            alert
            for alert in data.get("siem_alerts", [])
            if alert.get("user_id") == user_id
        ]
        payload = {"alerts": matching_alerts}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlerts",
                "description": "Retrieves a list of SIEM alerts based on the user's ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user_id to retrieve SIEM alerts for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
