from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAlertState(Tool):
    """Modifies the status of an alert."""

    def invoke(
        data: dict[str, Any],
        alert_id: str = None,
        id: Any = None,
        new_state: str = None
    ) -> str:
        alerts = data.get("alerts", {}).values()
        for alert in alerts.values():
            if alert.get("id") == alert_id:
                alert["state"] = new_state
                payload = {
                    "status": "success",
                    "message": f"State for alert '{alert_id}' updated to '{new_state}'.",
                }
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
                "name": "updateAlertState",
                "description": "Updates the state of an alert.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "state": {"type": "string"},
                    },
                    "required": ["id", "state"],
                },
            },
        }
