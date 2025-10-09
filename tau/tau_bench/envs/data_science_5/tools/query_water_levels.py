from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class QueryWaterLevels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None, start: str = None, end: str = None) -> str:
        station = station_id
        out = []
        for r in data.get("water_levels", {}).values() or []:
            if station and r.get("station_id") != station:
                continue
            ts = r.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            out.append(r)
        payload = {"rows": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "queryWaterLevels",
                "description": "Read observed water-level rows (optional station/time filters).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "start": {"type": "string"},
                        "end": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
