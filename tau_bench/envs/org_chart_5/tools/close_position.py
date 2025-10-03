from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any

class close_position(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], position_id: str = None) -> str:
        positions = data.get("positions", [])
        position_to_close = next(
            (p for p in positions if p.get("position_id") == position_id), None
        )

        if position_to_close:
            positions.remove(position_to_close)
            payload = {"success": f"Position {position_id} has been closed and removed."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"error": f"Position {position_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ClosePosition",
                "description": "Mark a position as closed by removing it from the list of available positions.",
                "parameters": {
                    "type": "object",
                    "properties": {"position_id": {"type": "string"}},
                    "required": ["position_id"],
                },
            },
        }
