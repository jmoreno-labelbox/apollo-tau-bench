# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHouseholdById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        return json.dumps({"household": _require(data, "households", "household_id", int(household_id))})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_household_by_id",
                "description": "Get household by household_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
