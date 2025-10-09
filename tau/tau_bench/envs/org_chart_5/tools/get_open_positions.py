from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class get_open_positions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None, level: str = None) -> str:
        filled_position_ids = {
            e.get("position_id")
            for e in data.get("employees", [])
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
        payload = open_positions
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOpenPositions",
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
