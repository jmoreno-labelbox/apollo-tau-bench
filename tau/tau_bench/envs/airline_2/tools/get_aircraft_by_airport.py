from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAircraftByAirport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], airport_id: str) -> str:
        res = []
        for a in data.get("aircraft", []):
            if a.get("location").get("airport_id") == airport_id:
                res.append(_j(a))
        return _j(res)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByAirport",
                "description": "Return aircraft by their base airport.",
                "parameters": {
                    "type": "object",
                    "properties": {"airport_id": {"type": "string"}},
                    "required": ["airport_id"],
                },
            },
        }
