from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetBranchByName(Tool):
    """Fetches a branch using its name within a particular repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repository_id: str = None, branch_name: str = None) -> str:
        branches = data.get("branches", {}).values()
        for branch in branches.values():
            if (
                branch.get("repository_id") == repository_id
                and branch.get("name") == branch_name
            ):
                payload = branch
                out = json.dumps(payload)
                return out
        payload = {"error": f"Branch '{branch_name}' not found in repository '{repository_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBranchByName",
                "description": "Retrieves a branch by its name within a specific repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {
                            "type": "string",
                            "description": "The ID of the repository.",
                        },
                        "branch_name": {
                            "type": "string",
                            "description": "The name of the branch.",
                        },
                    },
                    "required": ["repository_id", "branch_name"],
                },
            },
        }
