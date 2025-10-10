# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSiemAlert(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alerts = data.get('siem_alerts', [])
        new_id_num = max((int(a['alert_id'][5:]) for a in alerts), default=0) + 1
        new_alert_id = f"ALRT-{new_id_num:03d}"
        new_alert = {
                "alert_id": new_alert_id,
                "user_id": kwargs.get("user_id"),
                "resource_id": kwargs.get("resource_id"),
                "alert_type": kwargs.get("alert_type"),
                "severity": kwargs.get("severity"),
                "timestamp": NOW.strftime(DT_STR_FORMAT)
        }
        alerts.append(new_alert)
        data['siem_alerts'] = alerts
        return json.dumps(new_alert)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_siem_alert",
                        "description": "Creates a new SIEM alert.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "resource_id": {"type": "string"},
                                        "alert_type": {"type": "string"},
                                        "severity": {"type": "string"}
                                },
                                "required": ["user_id", "resource_id", "alert_type", "severity"]
                        }
                }
        }
