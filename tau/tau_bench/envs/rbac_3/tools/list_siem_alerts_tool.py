# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListSiemAlertsTool(Tool):
    """list_siem_alerts"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        resource_id = kwargs.get("resource_id")
        severity = kwargs.get("severity")
        alert_type = kwargs.get("alert_type")
        alert_id = kwargs.get("alert_id")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        alerts: List[Dict[str, Any]] = data.get("siem_alerts", [])
        out: List[Dict[str, Any]] = []
        for a in alerts:
            if user_id and not _eq(a.get("user_id"), user_id):
                continue
            if resource_id and not _eq(a.get("resource_id"), resource_id):
                continue
            if severity and not _eq(a.get("severity"), severity):
                continue
            if alert_type and not _eq(a.get("alert_type"), alert_type):
                continue
            if alert_id and not _eq(a.get("alert_id"), alert_id):
                continue
            if dt_from or dt_to:
                ts = _parse_iso(a.get("timestamp"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue
            out.append(a)

        out.sort(key=lambda r: ((r.get("timestamp") or ""), (r.get("alert_id") or "")))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_siem_alerts",
                "description": "List SIEM alerts with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "severity": {
                            "type": "string",
                            "description": "CRITICAL, HIGH, MEDIUM, LOW",
                        },
                        "alert_type": {"type": "string"},
                        "alert_id": {
                            "type": "string",
                            "description": "Specific alert ID to filter by",
                        },
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 lower bound",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 upper bound",
                        },
                    },
                    "required": [],
                },
            },
        }
