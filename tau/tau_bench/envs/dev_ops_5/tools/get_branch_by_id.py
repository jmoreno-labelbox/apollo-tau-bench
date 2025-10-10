# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBranchById(Tool):
    """Retrieves a branch by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        branch_id = kwargs.get("id")
        branches = list(data.get("branches", {}).values())
        for b in branches:
            if b.get("id") == branch_id:
                return json.dumps(b)
        return json.dumps({"error": f"Branch with ID '{branch_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_branch_by_id",
                "description": "Retrieves a branch by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
