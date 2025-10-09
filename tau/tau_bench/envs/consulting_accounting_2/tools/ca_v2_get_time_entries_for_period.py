from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2GetTimeEntriesForPeriod(Tool):
    """Retrieve time logs for a specific project within a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, start_date: str = None, end_date: str = None) -> str:
        if not all([project_id, start_date, end_date]):
            return _error("project_id, start_date, and end_date are required.")

        time_entries = data.get("time_entries", {}).values()
        filtered_entries = []

        for entry in time_entries.values():
            if (
                entry.get("project_id") == project_id
                and start_date <= entry.get("entry_date", "") <= end_date
            ):
                filtered_entries.append(entry)
        payload = filtered_entries
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetTimeEntriesForPeriod",
                "description": "Get time entries for a specific project within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                    },
                    "required": ["project_id", "start_date", "end_date"],
                },
            },
        }
