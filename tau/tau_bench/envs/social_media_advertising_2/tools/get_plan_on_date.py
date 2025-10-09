from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPlanOnDate(Tool):
    """Provide a static plan snapshot for a specified date."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        target_date = date
        for plan in data.get("plans", {}).values():
            if plan.get("date") == target_date:
                payload = plan
                out = json.dumps(payload)
                return out
        payload = {"error": f"No plan found for {target_date}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlanOnDate",
                "description": "Return a frozen plan snapshot for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Plan date (YYYY-MM-DD)",
                        }
                    },
                    "required": ["date"],
                },
            },
        }
