from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCustomersWithBirthdayToday(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], current_day: str) -> str:
        db = _convert_db_to_list(data.get("customers", {}))
        # current_day must follow the "MM-DD" format
        result = []
        for row in db:
            birthdate = row.get("birthdate", "")
            # Allow birthdate in either "YYYY-MM-DD" or "MM-DD"
            if len(birthdate) >= 5:
                birthdate = birthdate[-5:]
            if birthdate == current_day:
                result.append(row.get("customer_id"))
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomersWithBirthdayToday",
                "description": "Return a list of customer IDs who have a birthday on the given day (MM-DD).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_day": {
                            "type": "string",
                            "description": "The current day in MM-DD format (e.g., '04-23').",
                        }
                    },
                    "required": ["current_day"],
                },
            },
        }
