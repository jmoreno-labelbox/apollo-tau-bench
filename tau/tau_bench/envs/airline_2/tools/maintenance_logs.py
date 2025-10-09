from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class MaintenanceLogs(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        MaintenanceLogs: list = None
    ) -> str:
        return _j(MaintenanceLogs or [])
        return _j(data.get("MaintenanceLogs", []))

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MaintenanceLogs",
                "description": "List maintenance logs for a given aircraft_id.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
