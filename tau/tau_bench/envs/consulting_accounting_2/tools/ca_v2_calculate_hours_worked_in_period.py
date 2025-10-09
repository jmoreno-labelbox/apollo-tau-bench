from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CaV2CalculateHoursWorkedInPeriod(Tool):
    """Compute the total hours worked on projects for a defined period."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        end_date: str = None,
        project_ids: list = None,
        start_date: str = None
    ) -> str:
        if project_ids is None:
            project_ids = []

        if not all([start_date, end_date]):
            return _error("start_date and end_date are required.")

        time_entries = data.get("time_entries", [])

        # Narrow down by date and optionally by project IDs
        filtered_entries = []
        for entry in time_entries:
            entry_date = entry.get("entry_date", "")
            if start_date <= entry_date <= end_date:
                if not project_ids or entry.get("project_id") in project_ids:
                    filtered_entries.append(entry)

        # Compute overall totals
        total_hours = sum(entry.get("hours_worked", 0) for entry in filtered_entries)

        # Categorize by project
        hours_by_project = {}
        for entry in filtered_entries:
            project_id = entry.get("project_id")
            if project_id not in hours_by_project:
                hours_by_project[project_id] = 0
            hours_by_project[project_id] += entry.get("hours_worked", 0)

        return _ok(
            total_hours=total_hours,
            hours_by_project=hours_by_project,
            entry_count=len(filtered_entries),
            period_start=start_date,
            period_end=end_date,
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateHoursWorkedInPeriod",
                "description": "Calculate total hours worked for a specific period, optionally filtered by project IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                        "project_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["start_date", "end_date"],
                },
            },
        }
