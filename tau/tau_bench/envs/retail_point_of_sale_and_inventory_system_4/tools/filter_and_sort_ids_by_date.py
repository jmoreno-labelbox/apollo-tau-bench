# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterAndSortIdsByDate(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        ids_dates: Dict[str, str],
        filter_start_date: str = None,
        filter_end_date: str = None,
        top_n: int = None,
        sort_order: str = "newest"
    ) -> str:
        # Transform dictionary into a list of tuples containing (id, date).
        items = list(ids_dates.items())

        def timestamp_to_value(ts: str) -> str:
            return int(ts.replace("-", "").replace(":", "").replace("T", "").replace("Z", ""))

        # Apply filtering based on the specified date range if available.
        if filter_start_date or filter_end_date:
            filtered = []
            for id_, date in items:
                date_value = timestamp_to_value(date)
                if filter_start_date and date_value < timestamp_to_value(filter_start_date):
                    continue
                if filter_end_date and date_value > timestamp_to_value(filter_end_date):
                    continue
                filtered.append((id_, date))
            result = dict(filtered)
        else:
            # Arrange in chronological order.
            reverse = sort_order == "newest" # Newest indicates sorting in descending order, prioritizing the highest values.
            sorted_items = sorted(items, key=lambda x: timestamp_to_value(x[1]), reverse=reverse)
            if top_n is not None:
                sorted_items = sorted_items[:top_n]
            result = dict(sorted_items)
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_and_sort_ids_by_date",
                "description": "Filter a dictionary of IDs and dates by date range, or sort and return the top N newest/oldest entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ids_dates": {
                            "type": "object",
                            "description": "Dictionary mapping IDs to date strings (ISO format)."
                        },
                        "filter_start_date": {
                            "type": "string",
                            "default": None,
                            "description": "Start date (inclusive) for filtering (ISO format)."
                        },
                        "filter_end_date": {
                            "type": "string",
                            "default": None,
                            "description": "End date (inclusive) for filtering (ISO format)."
                        },
                        "top_n": {
                            "type": "integer",
                            "default": None,
                            "description": "Number of top entries to return after sorting."
                        },
                        "sort_order": {
                            "type": "string",
                            "default": "desc",
                            "description": "Sort order: 'desc' for newest first, 'asc' for oldest first."
                        }
                    },
                    "required": ["ids_dates"]
                }
            }
        }
