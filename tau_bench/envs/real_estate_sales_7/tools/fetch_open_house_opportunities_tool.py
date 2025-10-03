from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class FetchOpenHouseOpportunitiesTool(Tool):
    """Locates open houses that align with client criteria and availability."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        property_candidates: list = None,
        date: str = None,
        date_range_start: str = None,
        date_range_end: str = None
    ) -> str:
        property_candidates = property_candidates or []
        # Improvement: enable simplified single date that automatically extends to 3 days
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
            return _err("date WA (date_range_start and date_range_end) are required")

        prop_set = set(property_candidates)
        open_houses = []
        for oh in data.get("open_houses", []):
            if str(oh.get("property_id")) in prop_set:
                # Verify if open house dates coincide with the search range
                oh_start = oh.get("start_at", "")
                oh_end = oh.get("end_at", "")
                if oh_start <= date_range_end and oh_end >= date_range_start:
                    open_houses.append(oh)

        out = {
            "search_period": [date_range_start, date_range_end],
            "open_house_opportunities": open_houses[:10],
            "total_opportunities": len(open_houses),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #Facilitates Route Optimization Protocol (for planning viewings)
        return {
            "type": "function",
            "function": {
                "name": "FetchOpenHouseOpportunities",
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
