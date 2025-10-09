from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUmpiresDetailsByName(Tool):
    """Retrieve an umpire record using full_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], full_name: str = None) -> str:
        #1) Confirm validity
        if not isinstance(full_name, str) or full_name == "":
            payload = {"error": "Missing required field: full_name"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        umpires: list[dict[str, Any]] = data.get("umpires", {}).values()

        #3) Exact match (without normalization)
        for ump in umpires:
            if ump.get("full_name") == full_name:
                payload = ump
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No umpire found with full_name {full_name}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUmpiresDetailsByName",
                "description": "Fetch a single umpire's full details by exact full_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "Exact umpire full name to retrieve.",
                        }
                    },
                    "required": ["full_name"],
                },
            },
        }
