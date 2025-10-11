# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _parse_iso(ts: Optional[str]) -> Optional[datetime]:
    """Robust ISO8601 parse: supports 'Z' and offsets; returns None if missing."""
    if not ts:
        return None
    ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts)

def _eq(a: Optional[str], b: Optional[str]) -> bool:
    return (a or "") == (b or "")

class ListSiemAlertsTool(Tool):
    """list_siem_alerts"""

    @staticmethod
    def invoke(data: Dict[str, Any], alert_id, alert_type, date_from, date_to, resource_id, severity, user_id) -> str:

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