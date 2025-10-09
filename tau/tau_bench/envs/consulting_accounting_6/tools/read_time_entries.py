from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ReadTimeEntries(Tool):
    """Retrieve time logs for projects within a specified date range."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id_list: list = None, period_start: str = None, period_end: str = None) -> str:
        prj_ids = set(project_id_list or [])
        start = period_start
        end = period_end
        out = []
        for t in data.get("time_entries", {}).values() or []:
            if prj_ids and t.get("project_id") not in prj_ids:
                continue
            if start and t.get("entry_date", "") < start:
                continue
            if end and t.get("entry_date", "") > end:
                continue
            out.append(t)
        payload = {"rows": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadTimeEntries",
                "description": "Fetch time entries by project and period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id_list": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "period_start": {"type": "string"},
                        "period_end": {"type": "string"},
                    },
                    "required": ["project_id_list", "period_start", "period_end"],
                },
            },
        }
