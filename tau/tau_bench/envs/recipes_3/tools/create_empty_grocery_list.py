# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateEmptyGroceryList(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        created_by_user_id: int,
        source_meal_plan_id: Optional[int] = None,
        status_enum: str = "initialized",
    ) -> str:
        tbl = _tbl(data, "grocery_lists")
        next_id = _max_id(tbl, "list_id", 8000) + 1
        row = {
            "list_id": next_id,
            "household_id": int(household_id),
            "source_meal_plan_id": (
                int(source_meal_plan_id) if source_meal_plan_id is not None else None
            ),
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T12:00:00",
            "status_enum": str(status_enum),
        }
        tbl.append(row)
        return json({"list_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_empty_grocery_list",
                "description": "Create an empty grocery list header.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                        "source_meal_plan_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": ["household_id", "created_by_user_id"],
                },
            },
        }
