# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_review_cycle_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cycle_id: str, status: str, updated_at: str) -> str:
        cycles = data.get("review_cycles", [])
        for cycle in cycles:
            if cycle.get("cycle_id") == cycle_id:
                cycle["status"] = status
                cycle["updated_at"] = updated_at
                return json.dumps(cycle, indent=2)
        return json.dumps({"error": f"Cycle {cycle_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "update_review_cycle_status",
            "description": "Update the status of a review cycle.",
            "parameters": {"type": "object","properties": {
                "cycle_id": {"type": "string"},
                "status": {"type": "string"},
                "updated_at": {"type": "string"}
            },"required": ["cycle_id","status","updated_at"]}
        }}
