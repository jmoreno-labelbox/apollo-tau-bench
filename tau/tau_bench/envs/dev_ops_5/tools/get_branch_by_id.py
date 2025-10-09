from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetBranchById(Tool):
    """Fetches a branch using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        branch_id = id
        branches = data.get("branches", {}).values()
        for b in branches.values():
            if b.get("id") == branch_id:
                payload = b
                out = json.dumps(payload)
                return out
        payload = {"error": f"Branch with ID '{branch_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBranchById",
                "description": "Retrieves a branch by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
