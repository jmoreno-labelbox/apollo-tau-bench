from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetNeighborhoodDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_id: str = None, beds: Any = None, property_type: Any = None, price_min: Any = None) -> str:
        n = next(
            (
                n
                for n in data.get("neighborhoods", [])
                if n.get("neighborhood_id") == neighborhood_id
            ),
            None,
        )
        if not n:
            payload = {"error": f"Neighborhood {neighborhood_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = n
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNeighborhoodDetails",
                "description": "Return a neighborhood row including bordering_ids_json.",
                "parameters": {
                    "type": "object",
                    "properties": {"neighborhood_id": {"type": "integer"}},
                    "required": ["neighborhood_id"],
                },
            },
        }
