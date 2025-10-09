from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ReadNoaaStationSearches(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        rows = data.get("noaa_station_searches", {}).values() or []
        payload = {"rows": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "readNoaaStationSearches",
                "description": "List prior NOAA station discovery queries/results.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
