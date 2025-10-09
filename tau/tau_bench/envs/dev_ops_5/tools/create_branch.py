from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateBranch(Tool):
    """Generates a new branch in a repository based on a source branch."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        branch_name: str = None,
        repository_id: str = None,
        source_branch_id: Any = None
    ) -> str:
        branches = data.get("branches", [])
        new_id_num = max([int(b["id"].split("_")[1]) for b in branches]) + 1
        new_id = f"branch_{new_id_num:03d}"

        new_branch = {
            "id": new_id,
            "repository_id": repository_id,
            "name": branch_name,
            "created_at": "2025-01-28T00:00:00Z",
        }
        branches.append(new_branch)
        payload = new_branch
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateBranch",
                "description": "Creates a new branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string"},
                        "branch_name": {"type": "string"},
                        "source_branch_id": {"type": "string"},
                    },
                    "required": ["repository_id", "branch_name", "source_branch_id"],
                },
            },
        }
