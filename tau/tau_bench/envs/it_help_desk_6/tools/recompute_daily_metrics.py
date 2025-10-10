# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecomputeDailyMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date: str) -> str:
        opened = len([t for t in data["tickets"] if t["opened_at"].startswith(date)])
        closed = len([t for t in data["tickets"] if t.get("closed_at") and t["closed_at"].startswith(date)])
        closed_24 = 0
        # Approximate: treat any closed on same date as within 24h
        for t in data["tickets"]:
            if t.get("closed_at") and t["closed_at"].startswith(date) and t["opened_at"][:10] == date:
                closed_24 += 1
        avg_age_open_hours = 0
        row = {
            "date": date,
            "tickets_opened": opened,
            "tickets_closed": closed,
            "closed_within_24h": closed_24,
            "avg_open_age_hours": avg_age_open_hours,
        }
        _append_row(data["daily_metrics"], row)
        return json.dumps({"status": "ok", "metrics": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recompute_daily_metrics",
                "description": "Recompute and append daily ticket metrics for a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {"date": {"type": "string"}},
                    "required": ["date"],
                },
            },
        }
