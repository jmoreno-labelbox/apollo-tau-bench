# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTimeWindowTool(Tool):
    """
    get_time_window
    Given an ISO8601 timestamp and one or both of:
      - days:  e.g., "1d", "5d", "-5d"
      - hours: e.g., "1h", "3h", "4.5h", "-1h"
    returns {"date_from": <ts>, "date_to": <ts + delta>} (both ISO-8601, preserving offset).
    If only negative values are provided, date_to will be the original ts and date_from will be ts + delta.
    """

    @staticmethod
    def _parse_iso(ts: str) -> datetime:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))

    @staticmethod
    def _parse_offset(s: Optional[str], unit: str) -> float:
        if not s:
            return 0.0
        s = s.strip().lower()
        assert s.endswith(unit), f"Offset must end with '{unit}'"
        return float(s[:-1])

    @staticmethod
    def invoke(data: Dict[str, Any], days, hours, timestamp) -> str:
        import json

        ts = timestamp
        if not ts:
            return json.dumps({"error": "timestamp is required"}, indent=2)

        base = GetTimeWindowTool._parse_iso(ts)
        d = GetTimeWindowTool._parse_offset(days, "d") if days else 0.0
        h = GetTimeWindowTool._parse_offset(hours, "h") if hours else 0.0
        delta = timedelta(days=d, hours=h)

        # Identify the orientation of the window.
        if d < 0 or h < 0:
            start, end = base + delta, base
        else:
            start, end = base, base + delta

        # Maintain the precise "+00:00" format if it appears in the input.
        def fmt(dt: datetime) -> str:
            s = dt.isoformat()
            if s.endswith("+00:00"):
                return s
            if s[-6] in ["+", "-"] and s[-3] == ":":
                return s
            return s

        out = {"date_from": fmt(start), "date_to": fmt(end)}
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_time_window",
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
