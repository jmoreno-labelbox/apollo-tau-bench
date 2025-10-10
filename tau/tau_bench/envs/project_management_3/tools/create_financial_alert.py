# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFinancialAlert(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_type = kwargs.get("alert_type")
        entity_type = kwargs.get("entity_type")
        entity_id = kwargs.get("entity_id")
        threshold_value = kwargs.get("threshold_value")
        notify_list = kwargs.get("notify_list", [])
        alert_id = kwargs.get("alert_id", f"alert_{uuid.uuid4().hex[:8]}")

        if not all([alert_type, entity_type, entity_id, notify_list]):
            return json.dumps(
                {
                    "error": "alert_type, entity_type, entity_id, and notify_list are required"
                }
            )

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

        return json.dumps({"success": True, "alert": new_alert})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_financial_alert",
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
