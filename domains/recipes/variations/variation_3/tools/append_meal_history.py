from tau_bench.envs.tool import Tool
import json
from typing import Any

class AppendMealHistory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int,
        plan_date: str,
        recipe_id: int,
        was_prepared: bool,
        rating_int: int | None = None
    ) -> str:
        table = _get_table(data, "meal_history")
        next_id = _max_int(table, "history_id", 0) + 1
        rec = {
            "history_id": next_id,
            "household_id": household_id,
            "plan_date": plan_date,
            "recipe_id": recipe_id,
            "was_prepared": was_prepared,
            "rating_int": rating_int,
        }
        table.append(rec)
        payload = {"history_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
        table = _get_table(data, "meal_history")
        next_id = _max_int(table, "history_id", 0) + 1
        rec = {
            "history_id": next_id,
            "household_id": household_id,
            "plan_date": plan_date,
            "recipe_id": recipe_id,
            "was_prepared": was_prepared,
            "rating_int": rating_int,
        }
        table.append(rec)
        payload = {"history_id": next_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendMealHistory",
                "description": "Appends a meal_history record with next history_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "plan_date": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                        "was_prepared": {"type": "boolean"},
                        "rating_int": {"type": "integer"},
                    },
                    "required": [
                        "household_id",
                        "plan_date",
                        "recipe_id",
                        "was_prepared",
                    ],
                },
            },
        }
