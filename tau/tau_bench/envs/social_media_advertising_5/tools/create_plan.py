# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], author, checksum, created_at, date, plan_id, total_budget, allocations = []) -> str:
        rec = {"plan_id": plan_id, "date": date, "total_budget": total_budget,
               "author": author, "created_at": created_at,
               "checksum": checksum, "allocations": allocations}
        data.setdefault("plans", []).append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "create_plan", "description": "Creates a plan with allocations.",
                             "parameters": {"type": "object",
                                            "properties": {"plan_id": {"type": "string"}, "date": {"type": "string"},
                                                           "total_budget": {"type": "number"},
                                                           "author": {"type": "string"},
                                                           "created_at": {"type": "string"},
                                                           "checksum": {"type": "string"},
                                                           "allocations": {"type": "array", "items": {"type": "object"}}},
                                            "required": ["plan_id", "date", "total_budget", "author", "created_at",
                                                         "checksum", "allocations"]}}}
