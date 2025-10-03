from tau_bench.envs.tool import Tool
import json
from typing import Any

class ApplyChildNotesForPlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        meal_plan_id: int,
        note: str = "Child: low spice, small pieces"
    ) -> str:
        entries = _get_table(data, "meal_plan_entries")
        updated_ids: list[int] = []
        for e in entries:
            if e.get("meal_plan_id") == meal_plan_id and e.get("meal_type") == "Dinner":
                prev = e.get("notes")
                if prev != note:
                    e["notes"] = note
                    updated_ids.append(e.get("entry_id"))
        payload = {"updated_entry_ids": updated_ids, "note": note}
        out = json.dumps(payload, indent=2)
        return out
        pass
        entries = _get_table(data, "meal_plan_entries")
        updated_ids: list[int] = []
        for e in entries:
            if e.get("meal_plan_id") == meal_plan_id and e.get("meal_type") == "Dinner":
                prev = e.get("notes")
                if prev != note:
                    e["notes"] = note
                    updated_ids.append(e.get("entry_id"))
        payload = {"updated_entry_ids": updated_ids, "note": note}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyChildNotesForPlan",
                "description": "Idempotently sets a child-friendly note on all Dinner entries of a meal plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "meal_plan_id": {"type": "integer"},
                        "note": {"type": "string"},
                    },
                    "required": ["meal_plan_id"],
                },
            },
        }
