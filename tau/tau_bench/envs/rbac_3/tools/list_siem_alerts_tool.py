from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListSiemAlertsTool(Tool):
    """ListSiemAlerts"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        resource_id: str = None,
        severity: str = None,
        alert_type: str = None,
        alert_id: str = None,
        date_from: str = None,
        date_to: str = None
,
    severity_in: Any = None,
    ) -> str:
        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        alerts: list[dict[str, Any]] = data.get("siem_alerts", {}).values()
        out: list[dict[str, Any]] = []
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSiemAlerts",
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
