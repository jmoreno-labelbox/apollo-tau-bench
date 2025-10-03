from tau_bench.envs.tool import Tool
import json
from typing import Any

class update_review_cycle_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cycle_id: str, status: str, updated_at: str
    ) -> str:
        cycles = data.get("review_cycles", [])
        for cycle in cycles:
            if cycle.get("cycle_id") == cycle_id:
                cycle["status"] = status
                cycle["updated_at"] = updated_at
                payload = cycle
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Cycle {cycle_id} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewCycleStatus",
                "description": "Update the status of a review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "status": {"type": "string"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["cycle_id", "status", "updated_at"],
                },
            },
        }
