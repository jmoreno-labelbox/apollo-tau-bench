from tau_bench.envs.tool import Tool
import json
from typing import Any

class AllocateTrackingId(Tool):
    """Generate a new tracking_id string using courier_id and a seed provided by the caller."""

    @staticmethod
    def invoke(data, courier_id: str = None, seed: int = None) -> str:
        if not courier_id or seed is None:
            payload = {"error": "courier_id and seed are required"}
            out = json.dumps(payload, indent=2)
            return out
        new_id = f"TRK-{courier_id.strip('#')}-{str(seed)}"
        payload = {"tracking_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "allocateTrackingId",
                "description": "Return a tracking id for a courier based on a numeric/string seed.",
                "parameters": {
                    "type": "object",
                    "properties": {"courier_id": {"type": "string"}, "seed": {}},
                    "required": ["courier_id", "seed"],
                },
            },
        }
