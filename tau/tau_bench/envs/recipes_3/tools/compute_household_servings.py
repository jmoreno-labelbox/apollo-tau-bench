# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeHouseholdServings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        members = [
            m for m in data.get("members", []) if int(m.get("household_id")) == int(household_id)
        ]
        adults = sum(1 for m in members if not bool(m.get("is_child", False)))
        children = sum(1 for m in members if bool(m.get("is_child", False)))
        return json({"servings_adult": adults, "servings_child": children})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_household_servings",
                "description": "Count adults vs children to derive servings.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
