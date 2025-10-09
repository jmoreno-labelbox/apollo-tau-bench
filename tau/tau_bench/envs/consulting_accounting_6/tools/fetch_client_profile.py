from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FetchClientProfile(Tool):
    """Retrieve a client/publisher entry using publisher_id."""

    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        pid = publisher_id
        row = next(
            (p for p in data.get("publishers", []) if p.get("publisher_id") == pid),
            None,
        )
        if not row:
            payload = {"error": f"publisher_id '{pid}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchClientProfile",
                "description": "Fetch a client/publisher record.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }
