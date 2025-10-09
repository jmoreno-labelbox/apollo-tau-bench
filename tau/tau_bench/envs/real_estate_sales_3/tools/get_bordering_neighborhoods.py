from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetBorderingNeighborhoods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_id: str = None) -> str:
        nid = neighborhood_id
        n = next(
            (
                n
                for n in data.get("neighborhoods", [])
                if n.get("neighborhood_id") == nid
            ),
            None,
        )
        if not n:
            payload = {"error": f"Neighborhood {nid} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"neighborhood_id": nid, "bordering": n.get("bordering_ids_json") or []}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBorderingNeighborhoods",
                "description": "List bordering neighborhood IDs for a given neighborhood.",
                "parameters": {
                    "type": "object",
                    "properties": {"neighborhood_id": {"type": "integer"}},
                    "required": ["neighborhood_id"],
                },
            },
        }
