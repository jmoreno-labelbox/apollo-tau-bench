# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class close_position(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        position_id = kwargs.get("position_id")
        positions = data.get("positions", [])
        position_to_close = next(
            (p for p in positions if p.get("position_id") == position_id), None
        )

        if position_to_close:
            positions.remove(position_to_close)
            return json.dumps(
                {"success": f"Position {position_id} has been closed and removed."},
                indent=2,
            )
        else:
            return json.dumps({"error": f"Position {position_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_position",
                "description": "Mark a position as closed by removing it from the list of available positions.",
                "parameters": {
                    "type": "object",
                    "properties": {"position_id": {"type": "string"}},
                    "required": ["position_id"],
                },
            },
        }
