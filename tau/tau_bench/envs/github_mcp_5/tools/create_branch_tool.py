from tau_bench.envs.tool import Tool
import calendar
import json
import os
import random
import uuid
from datetime import datetime, timezone
from typing import Any
import hashlib
from datetime import datetime



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateBranchTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, branch_name: str = None, sha: str = None) -> str:
        if not all([owner, repo, branch_name, sha]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for create_branch.",
                    "required": ["owner", "repo", "branch_name", "sha"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", {}).values()
        repository = next(
            (r for r in repositories.values() if r["repo_name"] == repo and r["owner"] == owner),
            None,
        )

        if not repository:
            payload = {
                    "status": "error",
                    "message": f"Repository '{repo}' not found for owner '{owner}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Simulate creating a branch
        repository.setdefault("branches", []).append(
            {"name": branch_name, "commit_sha": sha}
        )
        repository.setdefault("branch_files", []).append(
            []
        )  # Add empty file list for new branch
        repository.setdefault("branch_contents", []).append(
            []
        )  # Add empty contents list
        payload = {
                "status": "success",
                "message": f"Branch '{branch_name}' created successfully.",
                "ref": f"refs/heads/{branch_name}",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createBranch",
                "description": "Creates a new branch in a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "The owner of the repository.",
                        },
                        "repo": {
                            "type": "string",
                            "description": "The name of the repository.",
                        },
                        "branch_name": {
                            "type": "string",
                            "description": "The name of the new branch.",
                        },
                        "sha": {
                            "type": "string",
                            "description": "The SHA of the commit to branch from.",
                        },
                    },
                    "required": ["owner", "repo", "branch_name", "sha"],
                },
            },
        }
