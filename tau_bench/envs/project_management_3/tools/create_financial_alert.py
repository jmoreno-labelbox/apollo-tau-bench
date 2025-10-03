from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any

class CreateFinancialAlert(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        alert_type: str,
        entity_type: str,
        entity_id: str,
        threshold_value: Any = None,
        notify_list: list = None,
        alert_id: str = None
    ) -> str:
        if notify_list is None:
            notify_list = []
        if alert_id is None:
            alert_id = f"alert_{uuid.uuid4().hex[:8]}"

        if not all([alert_type, entity_type, entity_id, notify_list]):
            payload = {
                "error": "alert_type, entity_type, entity_id, and notify_list are required"
            }
            out = json.dumps(payload)
            return out

        financial_alerts = data.get("financial_alerts", [])

        new_alert = {
            "alert_id": alert_id,
            "alert_type": alert_type,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "threshold_value": threshold_value,
            "notify_list": notify_list,
            "status": "active",
            "created_date": datetime.now().isoformat(),
            "triggered_count": 0,
            "last_triggered": None,
        }

        financial_alerts.append(new_alert)
        payload = {"success": True, "alert": new_alert}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFinancialAlert",
                "description": "Create automated financial alerts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_type": {
                            "type": "string",
                            "description": "Type of alert",
                        },
                        "entity_type": {
                            "type": "string",
                            "description": "Entity type to monitor",
                        },
                        "entity_id": {"type": "string", "description": "Entity ID"},
                        "alert_id": {"type": "string", "description": "Alert ID"},
                        "threshold_value": {
                            "type": "number",
                            "description": "Threshold value (optional)",
                        },
                        "notify_list": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs to notify",
                        },
                    },
                    "required": [
                        "alert_type",
                        "entity_type",
                        "entity_id",
                        "notify_list",
                    ],
                },
            },
        }
