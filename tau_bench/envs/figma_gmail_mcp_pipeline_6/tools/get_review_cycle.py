from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_review_cycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str) -> str:
        cyc = next(
            (c for c in _table(data, "review_cycles") if c.get("cycle_id") == cycle_id),
            None,
        )
        if not cyc:
            payload = {"error": f"cycle_id '{cycle_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"cycle_id": cyc.get("cycle_id"), "status": cyc.get("status")}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewCycle",
                "description": "Return (cycle_id, status) as a structured JSON object.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }
