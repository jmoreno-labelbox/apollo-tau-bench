# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCycleById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cycle_id) -> str:
        if not cycle_id:
            return json.dumps({"error": "Missing required field: cycle_id"}, indent=2)
        cycles: List[Dict[str, Any]] = list(data.get("review_cycles", {}).values())
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No cycle with id '{cycle_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_cycle_by_id",
                "description": "Fetch a single review cycle by cycle_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"}
                    },
                    "required": ["cycle_id"]
                }
            }
        }
