from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MaintenanceLogsForAircraft(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str) -> str:
        out = [
            m
            for m in data.get("MaintenanceLogs", {}).values()
            if (m.get("aircraft") or {}).get("aircraft_id") == aircraft_id
        ]
        return _j(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MaintenanceLogsForAircraft",
                "description": "List maintenance logs for a given aircraft_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"aircraft_id": {"type": "string"}},
                    "required": ["aircraft_id"],
                },
            },
        }
