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
        return list(db.values())
    return db

class GetPullRequestStatusTool(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo: str = None, pr_number: int = None) -> str:
        if not all([owner, repo, pr_number]):
            payload = {
                    "status": "error",
                    "message": "Missing required parameters for get_pull_request_status.",
                    "required": ["owner", "repo", "pr_number"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repositories = data.get("repositories", [])
        repository = next(
            (r for r in repositories if r["repo_name"] == repo and r["owner"] == owner),
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

        #Simulate getting status, e.g., checks and mergeability
        #In a real API, this would be more detailed.
        status = {
            "checks": [
                {"name": "CI Check", "status": "success"},
                {"name": "Code Style", "status": "success"},
            ],
            "mergeable": pull_request.get("mergeable_flags", [False])[0],
            "state": pull_request.get("pr_states", ["open"])[0],
        }
        payload = {"status": "success", "pull_request_status": status}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPullRequestStatus",
                "description": "Retrieves the status of a pull request, including checks and mergeability.",
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
