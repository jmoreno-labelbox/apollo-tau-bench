from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetAircraftStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str, new_status: str) -> str:
        new_status = new_status[:1].upper() + new_status[1:]
        for a in data.get("aircraft", []):
            if a.get("aircraft_id") == aircraft_id:
                a["status"] = new_status
                return _j(a)
        return _j({"error": "aircraft_not_found", "aircraft_id": aircraft_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetAircraftStatus",
                "description": "Set status on an aircraft deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["aircraft_id", "new_status"],
                },
            },
        }
