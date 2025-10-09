from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindReservationsByUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        res = [r for r in data.get("reservations", []) if r.get("user_id") == user_id]
        return _j(res)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindReservationsByUser",
                "description": "Return all reservations for a user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
