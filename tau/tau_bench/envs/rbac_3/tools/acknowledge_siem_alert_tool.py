from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class AcknowledgeSiemAlertTool(Tool):
    """acknowledge_siem_alert
    Records in data['siem_acknowledgments'] with: alert_id, ack_by, status, note, ack_at(HARD_TS)
    """

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None, ack_by: str = None, status: str = "ACKNOWLEDGED", note: str = None, severity_in: Any = None) -> str:
        pass
        ack_at = _HARD_TS

        if not alert_id or not ack_by:
            payload = {"error": "alert_id and ack_by are required"}
            out = json.dumps(payload, indent=2)
            return out

        alerts: list[dict[str, Any]] = data.setdefault("siem_alerts", [])
        rec = next((a for a in alerts if a.get("alert_id") == alert_id), None)
        if not rec:
            payload = {"error": f"Alert {alert_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        acks: list[dict[str, Any]] = data.setdefault("siem_acknowledgments", [])
        ack = next((x for x in acks if x.get("alert_id") == alert_id), None)
        if not ack:
            ack = {"alert_id": alert_id}

        ack["ack_by"] = ack_by
        ack["status"] = status
        ack["note"] = note
        ack["ack_at"] = ack_at

        #insert or update
        replaced = False
        for i, x in enumerate(acks):
            if x.get("alert_id") == alert_id:
                acks[i] = ack
                replaced = True
                break
        if not replaced:
            acks.append(ack)
        payload = ack
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AcknowledgeSiemAlert",
                "description": (
                    "Record an acknowledgment for a SIEM alert in a separate store (no changes to alert record)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {"type": "string"},
                        "ack_by": {
                            "type": "string",
                            "description": "User ID acknowledging",
                        },
                        "status": {
                            "type": "string",
                            "description": "ACKNOWLEDGED, CLOSED, etc.",
                        },
                        "note": {"type": "string"},
                    },
                    "required": ["alert_id", "ack_by"],
                },
            },
        }
