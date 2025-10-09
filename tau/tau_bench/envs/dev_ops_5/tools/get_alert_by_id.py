from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAlertById(Tool):
    """Fetches an alert using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        alert_id = id
        alerts = data.get("alerts", [])
        for alert in alerts:
            if alert.get("id") == alert_id:
                payload = alert
                out = json.dumps(payload)
                return out
        payload = {"error": f"Alert with ID '{alert_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAlertById",
                "description": "Retrieves an alert by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
