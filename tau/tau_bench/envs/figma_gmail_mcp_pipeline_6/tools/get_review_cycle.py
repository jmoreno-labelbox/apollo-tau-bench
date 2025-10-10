# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_review_cycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cycle_id: str) -> str:
        cyc = next((c for c in _table(data, "review_cycles") if c.get("cycle_id") == cycle_id), None)
        if not cyc:
            return json.dumps({"error": f"cycle_id '{cycle_id}' not found"}, indent=2)
        return json.dumps({"cycle_id": cyc.get("cycle_id"), "status": cyc.get("status")}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_review_cycle",
                "description": "Return (cycle_id, status) as a structured JSON object.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }
