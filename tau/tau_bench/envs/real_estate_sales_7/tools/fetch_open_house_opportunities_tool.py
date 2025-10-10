# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchOpenHouseOpportunitiesTool(Tool):
    """Finds open houses matching client criteria and availability."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_candidates = kwargs.get("property_candidates") or []
        # Improvement: enable single date input that automatically extends to a 3-day span.
        date = kwargs.get("date")
        date_range_start = kwargs.get("date_range_start")
        date_range_end = kwargs.get("date_range_end")
        if date and (not date_range_start or not date_range_end):
            try:
                from datetime import datetime, timedelta

                start_dt = datetime.strptime(str(date), "%Y-%m-%d")
                end_dt = start_dt + timedelta(days=3)
                date_range_start = f"{start_dt.strftime('%Y-%m-%d')}T00:00:00Z"
                date_range_end = f"{end_dt.strftime('%Y-%m-%d')}T23:59:59Z"
            except Exception:
                # Best-effort fallback
                date_str = str(date)
                date_range_start = f"{date_str}T00:00:00Z"
                try:
                    y, m, d = date_str.split("-")
                    date_range_end = f"{y}-{m}-{int(d)+3:02d}T23:59:59Z"
                except Exception:
                    date_range_end = f"{date_str}T23:59:59Z"
        if not date_range_start or not date_range_end:
            return _err("date or (date_range_start and date_range_end) are required")

        prop_set = set(property_candidates)
        open_houses = []
        for oh in data.get("open_houses", []):
            if str(oh.get("property_id")) in prop_set:
                # Verify if the open house dates intersect with the search period.
                oh_start = oh.get("start_at", "")
                oh_end = oh.get("end_at", "")
                if oh_start <= date_range_end and oh_end >= date_range_start:
                    open_houses.append(oh)

        out = {
            "search_period": [date_range_start, date_range_end],
            "open_house_opportunities": open_houses[:10],
            "total_opportunities": len(open_houses),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Facilitates Route Optimization Protocol (scheduling viewings)
        return {
            "type": "function",
            "function": {
                "name": "fetch_open_house_opportunities",
                "description": (
                    "Find open houses for a set of properties within a date range."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_candidates": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "date_range_start": {"type": ["string", "null"]},
                        "date_range_end": {"type": ["string", "null"]},
                        "date": {
                            "type": ["string", "null"],
                            "description": (
                                "Start date (YYYY-MM-DD) to auto-expand 3 days"
                            ),
                        },
                    },
                    "required": ["property_candidates"],
                },
            },
        }
