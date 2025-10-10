# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AcknowledgeSiemAlertTool(Tool):
    """acknowledge_siem_alert
    Writes to data['siem_acknowledgments'] with: alert_id, ack_by, status, note, ack_at(HARD_TS)
    """

    @staticmethod
    def invoke(data: Dict[str, Any], ack_by, alert_id, note, status) -> str:
        status = status or "ACKNOWLEDGED"
        ack_at = _HARD_TS

        if not alert_id or not ack_by:
            return json.dumps({"error": "alert_id and ack_by are required"}, indent=2)

        alerts: List[Dict[str, Any]] = data.setdefault("siem_alerts", [])
        rec = next((a for a in alerts if a.get("alert_id") == alert_id), None)
        if not rec:
            return json.dumps({"error": f"Alert {alert_id} not found"}, indent=2)

        acks: List[Dict[str, Any]] = data.setdefault("siem_acknowledgments", [])
        ack = next((x for x in acks if x.get("alert_id") == alert_id), None)
        if not ack:
            ack = {"alert_id": alert_id}

        ack["ack_by"] = ack_by
        ack["status"] = status
        ack["note"] = note
        ack["ack_at"] = ack_at

        # insert or update
        replaced = False
        for i, x in enumerate(acks):
            if x.get("alert_id") == alert_id:
                acks[i] = ack
                replaced = True
                break
        if not replaced:
            acks.append(ack)

        return json.dumps(ack, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "acknowledge_siem_alert",
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
