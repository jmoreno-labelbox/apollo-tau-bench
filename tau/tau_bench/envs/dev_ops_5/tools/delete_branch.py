from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteBranch(Tool):
    """Removes a branch."""

    def invoke(
        data: dict[str, Any],
        branch_id: str = None,
        id: Any = None
    ) -> str:
        branches = data.get("branches", [])
        original_count = len(branches)
        data["branches"] = [b for b in branches if b.get("id") != branch_id]
        if len(data["branches"]) < original_count:
            payload = {"status": "success", "message": f"Branch '{branch_id}' deleted."}
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
                "name": "deleteBranch",
                "description": "Deletes a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
