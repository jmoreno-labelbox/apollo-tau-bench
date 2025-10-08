from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class CreateSiemAlert(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, resource_id: str = None, alert_type: str = None, severity: str = None) -> str:
        alerts = data.get("siem_alerts", [])
        new_id_num = max((int(a["alert_id"][5:]) for a in alerts), default=0) + 1
        new_alert_id = f"ALRT-{new_id_num:03d}"
        new_alert = {
            "alert_id": new_alert_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "alert_type": alert_type,
            "severity": severity,
            "timestamp": NOW.strftime(DT_STR_FORMAT),
        }
        alerts.append(new_alert)
        data["siem_alerts"] = alerts
        payload = new_alert
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createSiemAlert",
                "description": "Creates a new SIEM alert.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "alert_type": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                    "required": ["user_id", "resource_id", "alert_type", "severity"],
                },
            },
        }
