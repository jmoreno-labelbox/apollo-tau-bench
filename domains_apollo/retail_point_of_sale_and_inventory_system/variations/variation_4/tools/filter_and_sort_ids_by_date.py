from tau_bench.envs.tool import Tool
import json
from typing import Any

class FilterAndSortIdsByDate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        ids_dates: dict[str, str],
        filter_start_date: str = None,
        filter_end_date: str = None,
        top_n: int = None,
        sort_order: str = "newest"
    ) -> str:
        # Transform dictionary into a list of tuples (id, date)
        items = list(ids_dates.items())

        def timestamp_to_value(ts: str) -> str:
            return int(
                ts.replace("-", "").replace(":", "").replace("T", "").replace("Z", "")
            )

        # Apply date range filter if specified
        if filter_start_date or filter_end_date:
            filtered = []
            for id_, date in items:
                date_value = timestamp_to_value(date)
                if filter_start_date and date_value < timestamp_to_value(
                    filter_start_date
                ):
                    continue
                if filter_end_date and date_value > timestamp_to_value(filter_end_date):
                    continue
                filtered.append((id_, date))
            result = dict(filtered)
        else:
            # Order by date
            reverse = (
                sort_order == "newest"
            )  # Newest indicates highest values first, which is in reverse order
            sorted_items = sorted(
                items, key=lambda x: timestamp_to_value(x[1]), reverse=reverse
            )
            if top_n is not None:
                sorted_items = sorted_items[:top_n]
            result = dict(sorted_items)
        payload = result
        out = json.dumps(payload)
        return out
        pass
        #Transform dictionary into a list of tuples (id, date)
        items = list(ids_dates.items())

        def timestamp_to_value(ts: str) -> str:
            pass
            return int(
                ts.replace("-", "").replace(":", "").replace("T", "").replace("Z", "")
            )

        #Apply date range filter if specified
        if filter_start_date or filter_end_date:
            filtered = []
            for id_, date in items:
                date_value = timestamp_to_value(date)
                if filter_start_date and date_value < timestamp_to_value(
                    filter_start_date
                ):
                    continue
                if filter_end_date and date_value > timestamp_to_value(filter_end_date):
                    continue
                filtered.append((id_, date))
            result = dict(filtered)
        else:
            #Order by date
            reverse = (
                sort_order == "newest"
            )  #Newest indicates highest values first, which is in reverse order
            sorted_items = sorted(
                items, key=lambda x: timestamp_to_value(x[1]), reverse=reverse
            )
            if top_n is not None:
                sorted_items = sorted_items[:top_n]
            result = dict(sorted_items)
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterAndSortIdsByDate",
                "description": "Filter a dictionary of IDs and dates by date range, or sort and return the top N newest/oldest entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ids_dates": {
                            "type": "object",
                            "description": "Dictionary mapping IDs to date strings (ISO format).",
                        },
                        "filter_start_date": {
                            "type": "string",
                            "default": None,
                            "description": "Start date (inclusive) for filtering (ISO format).",
                        },
                        "filter_end_date": {
                            "type": "string",
                            "default": None,
                            "description": "End date (inclusive) for filtering (ISO format).",
                        },
                        "top_n": {
                            "type": "integer",
                            "default": None,
                            "description": "Number of top entries to return after sorting.",
                        },
                        "sort_order": {
                            "type": "string",
                            "default": "desc",
                            "description": "Sort order: 'desc' for newest first, 'asc' for oldest first.",
                        },
                    },
                    "required": ["ids_dates"],
                },
            },
        }
