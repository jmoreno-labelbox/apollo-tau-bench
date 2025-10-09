from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class OpenHousesForProperties(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_ids: list[int] = None, date_from: str = None, date_to: str = None) -> str:
        pids = set(property_ids or [])
        rows = []
        for oh in data.get("open_houses", []) or []:
            if pids and oh.get("property_id") not in pids:
                continue
            dt = oh.get("start_at", "")
            if date_from and dt < f"{date_from}T00:00:00Z":
                continue
            if date_to and dt > f"{date_to}T23:59:59Z":
                continue
            rows.append(oh)
        payload = {"matches": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "OpenHousesForProperties",
                "description": "Fetch open house windows for specific properties within a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {"type": "array", "items": {"type": "string"}},
                        "date_from": {"type": "string"},
                        "date_to": {"type": "string"},
                    },
                    "required": ["property_ids", "date_from", "date_to"],
                },
            },
        }
