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

class GetPullRequestFilesTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, pr_number: int = None) -> str:
        if not all([owner, repo, pr_number]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for get_pull_request_files.",
                    "required": ["owner", "repo", "pr_number"],
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

        pull_requests = repository.get("pull_requests", [])
        pull_request = next(
            (pr for pr in pull_requests if pr["pr_number"] == pr_number), None
        )

        if not pull_request:
            payload = {
                    "status": "error",
                    "message": f"Pull request #{pr_number} not found in repository '{repo}'.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # In a real scenario, you would fetch the files associated with the PR's commits.
        # For simulation, we'll return the file_paths from the repository's current state
        # that were likely involved in the PR's HEAD branch.
        head_branch = pull_request.get("head_branches", [""])[0]
        if head_branch:
            branch_index = next(
                (
                    i
                    for i, branch in enumerate(repository.get("branches", []))
                    if branch["name"] == head_branch
                ),
                -1,
            )
            if branch_index != -1:
                pr_files = repository.get("branch_files", [[]])[branch_index]
            else:
                pr_files = []  # Default if branch not found
        else:
            pr_files = []  # Default if no head branch specified

        # Update the PR object with the simulated files
        pull_request["pr_files"] = [{"filename": f} for f in pr_files]
        payload = {"status": "success", "files": [{"filename": f} for f in pr_files]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPullRequestFiles",
                "description": "Retrieves the list of files changed in a pull request.",
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
                        "pr_number": {
                            "type": "integer",
                            "description": "The number of the pull request.",
                        },
                    },
                    "required": ["owner", "repo", "pr_number"],
                },
            },
        }
