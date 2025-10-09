from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOpenHouseWindowsForNeighborhoods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_ids: list[int] = None) -> str:
        nids = set(neighborhood_ids or [])
        props = [
            p for p in data.get("properties", {}).values() if p.get("neighborhood_id") in nids
        ]
        prop_ids = {p.get("property_id") for p in props}
        rows = [
            oh
            for oh in data.get("open_houses", {}).values()
            if oh.get("property_id") in prop_ids
        ]
        payload = {"neighborhood_ids": list(nids), "open_houses": rows}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOpenHouseWindowsForNeighborhoods",
                "description": "Fetch open house windows for neighborhoods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        }
                    },
                    "required": ["neighborhood_ids"],
                },
            },
        }
