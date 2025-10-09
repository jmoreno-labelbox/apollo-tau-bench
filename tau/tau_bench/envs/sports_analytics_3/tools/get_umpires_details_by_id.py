from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUmpiresDetailsById(Tool):
    """Retrieve an umpire record using umpire_id."""

    @staticmethod
    def invoke(data: dict[str, Any], umpire_id: str = None) -> str:
        #1) Confirm validity
        if umpire_id is None:
            payload = {"error": "Missing required field: umpire_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        umpires: list[dict[str, Any]] = data.get("umpires", {}).values()

        #3) Lookup for exact matches
        for ump in umpires:
            if ump.get("umpire_id") == umpire_id:
                payload = ump
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No umpire found with ID {umpire_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUmpiresDetailsById",
                "description": "Fetch a single umpire's full details by umpire_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "umpire_id": {
                            "type": "integer",
                            "description": "Exact umpire ID to retrieve.",
                        }
                    },
                    "required": ["umpire_id"],
                },
            },
        }
