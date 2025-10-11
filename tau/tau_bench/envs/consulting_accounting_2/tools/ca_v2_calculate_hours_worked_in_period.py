# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _ok(**payload) -> str:
    out = {"status": "success"}
    out.update(payload)
    return json.dumps(out)

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class CaV2CalculateHoursWorkedInPeriod(Tool):
    """Calculate total hours worked across projects for a specific period."""

    @staticmethod
    def invoke(data: Dict[str, Any], end_date, start_date, project_ids = []) -> str:

        if not all([start_date, end_date]):
            return _error("start_date and end_date are required.")

        time_entries = data.get("time_entries", [])

        # Filter based on date, with an optional filter for project_ids.
        filtered_entries = []
        for entry in time_entries:
            entry_date = entry.get("entry_date", "")
            if start_date <= entry_date <= end_date:
                if not project_ids or entry.get("project_id") in project_ids:
                    filtered_entries.append(entry)

        # Compute sums
        total_hours = sum(entry.get("hours_worked", 0) for entry in filtered_entries)

        # Organize by project
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
            period_end=end_date
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_hours_worked_in_period",
                "description": "Calculate total hours worked for a specific period, optionally filtered by project IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                        "project_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["start_date", "end_date"],
                },
            },
        }