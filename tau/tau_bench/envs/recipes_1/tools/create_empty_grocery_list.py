# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _max_id, _json_dump






def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    vals = []
    for r in records:
        try:
            vals.append(int(r.get(key)))
        except Exception:
            pass
    return max(vals) if vals else default

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class CreateEmptyGroceryList(Tool):
    """Create an empty grocery_list header; returns list_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], created_by_user_id, household_id, source_meal_plan_id, status_enum = "initialized") -> str:
        if household_id is None or created_by_user_id is None:
            return _json_dump({"error": "household_id and created_by_user_id are required"})
        tbl = data.setdefault("grocery_lists", [])
        next_id = _max_id(tbl, "list_id", 8000) + 1
        row = {
            "list_id": next_id,
            "household_id": int(household_id),
            "source_meal_plan_id": int(source_meal_plan_id) if source_meal_plan_id is not None else None,
            "created_by_user_id": int(created_by_user_id),
            "created_at": "2025-01-01T12:00:00Z",
            "status_enum": str(status_enum)
        }
        tbl.append(row)
        return _json_dump({"list_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_empty_grocery_list",
            "description":"Create an empty grocery_list header.",
            "parameters":{"type":"object","properties":{
                "household_id":{"type":"integer"},
                "source_meal_plan_id":{"type":"integer"},
                "created_by_user_id":{"type":"integer"},
                "status_enum":{"type":"string"}
            },"required":["household_id","created_by_user_id"]}
        }}