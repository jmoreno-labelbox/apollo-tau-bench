from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateSiemAlert(Tool):
    """Create a new SIEM alert manually based on an investigation."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        user_id: str = None,
        resource_id: str = None,
        alert_type: str = None,
        severity: str = None
    ) -> str:
        try:
            siem_alerts = data.get("siem_alerts", [])
        except:
            siem_alerts = []

        existing_ids = [
            int(item["alert_id"].replace("ALRT-", ""))
            for item in siem_alerts
            if item.get("alert_id", "").startswith("ALRT-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        alert_id = f"ALRT-{next_id_num:03d}"

        new_alert = {
            "alert_id": alert_id,
            "timestamp": timestamp,
            "user_id": user_id,
            "resource_id": resource_id,
            "alert_type": alert_type,
            "severity": severity,
        }

        siem_alerts.append(new_alert)
        data["siem_alerts"] = siem_alerts
        payload = {"message": "SIEM alert created successfully.", "alert_details": new_alert}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSiemAlert",
                "description": "Manually creates a new SIEM (Security Information and Event Management) alert to formally track a discovered security incident.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user associated with the security event.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource that was targeted.",
                        },
                        "alert_type": {
                            "type": "string",
                            "description": "The type of alert (e.g., 'POTENTIAL_DATA_EXFILTRATION', 'UNAUTHORIZED_ACCESS_ATTEMPT').",
                        },
                        "severity": {
                            "type": "string",
                            "description": "The severity of the alert (e.g., 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW').",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp to record as the alert creation time.",
                        },
                    },
                    "required": [
                        "user_id",
                        "resource_id",
                        "alert_type",
                        "severity",
                        "timestamp",
                    ],
                },
            },
        }
