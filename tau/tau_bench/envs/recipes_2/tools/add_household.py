from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddHousehold(Tool):
    """Incorporates a new household."""

    @staticmethod
    def invoke(data: dict[str, Any], household_name: str = None, timezone: str = None, primary_user_id: int = None) -> str:
        households = data.get("households", [])
        new_id = (
            max([h.get("household_id", 0) for h in households]) + 1
            if households
            else 201
        )
        new_household = {
            "household_id": new_id,
            "household_name": household_name,
            "timezone": timezone,
            "primary_user_id": primary_user_id,
        }
        data["households"].append(new_household)
        payload = new_household
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addHousehold",
                "description": "Adds a new household.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_name": {"type": "string"},
                        "timezone": {"type": "string"},
                        "primary_user_id": {"type": "integer"},
                    },
                    "required": ["household_name", "timezone", "primary_user_id"],
                },
            },
        }
