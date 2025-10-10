# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteBranch(Tool):
    """Deletes a branch."""
    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        branch_id = id
        branches = list(data.get("branches", {}).values())
        original_count = len(branches)
        data['branches'] = [b for b in branches if b.get("id") != branch_id]
        if len(data['branches']) < original_count:
            return json.dumps({"status": "success", "message": f"Branch '{branch_id}' deleted."})
        return json.dumps({"error": f"Branch with ID '{branch_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_branch",
                "description": "Deletes a branch.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
