from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class GetTimeWindowTool(Tool):
    """
    get_time_window
    Given an ISO8601 timestamp and one or both of:
      - days:  e.g., "1d", "5d", "-5d"
      - hours: e.g., "1h", "3h", "4.5h", "-1h"
    returns {"date_from": <ts>, "date_to": <ts + delta>} (both ISO-8601, maintaining offset).
    If only negative values are supplied, date_to will be the original ts and date_from will be ts + delta.
    """

    @staticmethod
    def _parse_iso(ts: str) -> datetime:
        pass
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))

    @staticmethod
    def _parse_offset(s: str | None, unit: str) -> float:
        pass
        if not s:
            return 0.0
        s = s.strip().lower()
        assert s.endswith(unit), f"Offset must end with '{unit}'"
        return float(s[:-1])

    @staticmethod
    def invoke(data: dict[str, Any], timestamp: str = None, days: float = None, hours: float = None) -> str:
        pass
        import json

        ts = timestamp
        if not ts:
            payload = {"error": "timestamp is required"}
            out = json.dumps(payload, indent=2)
            return out

        base = GetTimeWindowTool._parse_iso(ts)
        d = GetTimeWindowTool._parse_offset(days, "d") if days else 0.0
        h = GetTimeWindowTool._parse_offset(hours, "h") if hours else 0.0
        delta = timedelta(days=d, hours=h)

        # Ascertain the direction of the window
        if d < 0 or h < 0:
            start, end = base + delta, base
        else:
            start, end = base, base + delta

        # Maintain the precise "+00:00" format if included in the input
        def fmt(dt: datetime) -> str:
            pass
            s = dt.isoformat()
            if s.endswith("+00:00"):
                return s
            if s[-6] in ["+", "-"] and s[-3] == ":":
                return s
            return s

        out = {"date_from": fmt(start), "date_to": fmt(end)}
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTimeWindow",
                "description": (
                    "Derive a time window from a base timestamp and offsets (days/hours)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": (
                                "ISO 8601 timestamp (e.g., 2024-06-01T00:00:00+00:00)"
                            ),
                        },
                        "days": {
                            "type": "string",
                            "description": "Relative days like '5d', '-5d'",
                        },
                        "hours": {
                            "type": "string",
                            "description": "Relative hours like '3h', '4.5h', '-1h'",
                        },
                    },
                    "required": ["timestamp"],
                },
            },
        }
