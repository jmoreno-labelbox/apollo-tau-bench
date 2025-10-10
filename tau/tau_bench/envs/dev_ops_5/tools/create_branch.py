# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBranch(Tool):
    """Creates a new branch in a repository from a source branch."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        branches = list(data.get("branches", {}).values())
        new_id_num = max([int(b["id"].split("_")[1]) for b in branches]) + 1
        new_id = f"branch_{new_id_num:03d}"
        
        new_branch = {
            "id": new_id,
            "repository_id": kwargs.get("repository_id"),
            "name": kwargs.get("branch_name"),
            "created_at": "2025-01-28T00:00:00Z"
        }
        branches.append(new_branch)
        return json.dumps(new_branch)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_branch",
                "description": "Creates a new branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string"},
                        "branch_name": {"type": "string"},
                        "source_branch_id": {"type": "string"}
                    },
                    "required": ["repository_id", "branch_name", "source_branch_id"],
                },
            },
        }
