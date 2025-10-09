from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCycleById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None) -> str:
        if not cycle_id:
            payload = {"error": "Missing required field: cycle_id"}
            out = json.dumps(payload, indent=2)
            return out

        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No cycle with id '{cycle_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCycleById",
                "description": "Fetch a single review cycle by cycle_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }
