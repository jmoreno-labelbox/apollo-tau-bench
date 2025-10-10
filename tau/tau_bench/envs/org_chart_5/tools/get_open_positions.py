# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_open_positions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department_id, level) -> str:

        filled_position_ids = {
            e.get("position_id")
            for e in list(data.get("employees", {}).values())
            if e.get("status") == "Active"
        }
        all_positions = data.get("positions", [])

        open_positions = [
            p for p in all_positions if p.get("position_id") not in filled_position_ids
        ]

        if department_id:
            open_positions = [
                p for p in open_positions if p.get("department_id") == department_id
            ]
        if level:
            open_positions = [p for p in open_positions if p.get("level_id") == level]

        return json.dumps(open_positions, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_open_positions",
                "description": "List all open positions not currently filled by an active employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {"type": "string"},
                        "level": {"type": "string"},
                    },
                },
            },
        }
