# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddHousehold(Tool):
    """Adds a new household."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_name = kwargs.get("household_name")
        timezone = kwargs.get("timezone")
        primary_user_id = kwargs.get("primary_user_id")
        households = data.get("households", [])
        new_id = max([h.get("household_id", 0) for h in households]) + 1 if households else 201
        new_household = {
            "household_id": new_id, "household_name": household_name,
            "timezone": timezone, "primary_user_id": primary_user_id
        }
        data["households"].append(new_household)
        return json.dumps(new_household)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_household",
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
