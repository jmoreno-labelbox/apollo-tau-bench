from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCourierDetails(Tool):
    """Retrieve courier record."""

    @staticmethod
    def invoke(data, courier_id: str = None) -> str:
        if not courier_id:
            payload = {"error": "courier_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        c = _find_courier(data, courier_id)
        payload = c or {"error": f"courier_id {courier_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getCourierDetails",
                "description": "Fetch courier record by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"courier_id": {"type": "string"}},
                    "required": ["courier_id"],
                },
            },
        }
