from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateGroceryList(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        source_meal_plan_id: int,
        created_by_user_id: int,
        status_enum: str = "initialized"
    ) -> str:
        table = _get_table(data, "grocery_lists")
        existing = next(
            (
                g
                for g in table
                if g.get("household_id") == household_id
                and g.get("source_meal_plan_id") == source_meal_plan_id
            ),
            None,
        )
        if existing:
            payload = {"list_id": existing.get("list_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
        next_id = _max_int(table, "list_id", 0) + 1
        rec = {
            "list_id": next_id,
            "household_id": household_id,
            "source_meal_plan_id": source_meal_plan_id,
            "created_by_user_id": created_by_user_id,
            "created_at": "FIXED",
            "status_enum": status_enum,
        }
        table.append(rec)
        payload = {"list_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "grocery_lists")
        existing = next(
            (
                g
                for g in table
                if g.get("household_id") == household_id
                and g.get("source_meal_plan_id") == source_meal_plan_id
            ),
            None,
        )
        if existing:
            payload = {"list_id": existing.get("list_id"), "deduplicated": True}
            out = json.dumps(
                payload, indent=2
            )
            return out
        next_id = _max_int(table, "list_id", 0) + 1
        rec = {
            "list_id": next_id,
            "household_id": household_id,
            "source_meal_plan_id": source_meal_plan_id,
            "created_by_user_id": created_by_user_id,
            "created_at": "FIXED",
            "status_enum": status_enum,
        }
        table.append(rec)
        payload = {"list_id": next_id, "deduplicated": False}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createGroceryList",
                "description": "Creates or returns an existing grocery_list deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "source_meal_plan_id": {"type": "integer"},
                        "created_by_user_id": {"type": "integer"},
                        "status_enum": {"type": "string"},
                    },
                    "required": [
                        "household_id",
                        "source_meal_plan_id",
                        "created_by_user_id",
                    ],
                },
            },
        }
