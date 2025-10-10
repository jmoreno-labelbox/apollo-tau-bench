# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetTimeEntriesForPeriod(Tool):
    """Get time entries for a specific project and date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], end_date, project_id, start_date) -> str:

        if not all([project_id, start_date, end_date]):
            return _error("project_id, start_date, and end_date are required.")

        time_entries = data.get("time_entries", [])
        filtered_entries = []

        for entry in time_entries:
            if (entry.get("project_id") == project_id and
                start_date <= entry.get("entry_date", "") <= end_date):
                filtered_entries.append(entry)

        return json.dumps(filtered_entries)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_time_entries_for_period",
                "description": "Get time entries for a specific project within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"}
                    },
                    "required": ["project_id", "start_date", "end_date"],
                },
            },
        }
