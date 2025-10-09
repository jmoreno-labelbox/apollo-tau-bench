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

class CreatePullRequestTool(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str = None,
        repo: str = None,
        title: str = None,
        body: str = None,
        head: str = None,
        base: str = "main"
    ) -> str:
        if not all([owner, repo, title, body, head, base]):
            payload = {
                "status": "error",
                "message": "Missing required parameters for create_pull_request.",
                "required": ["owner", "repo", "title", "body", "head", "base"],
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

        # Simulate creating a pull request
        pr_number = len(repository.get("pull_requests", [])) + 1
        repository.setdefault("pull_requests", []).append(
            {
                "pr_number": pr_number,
                "owner": owner,
                "repo_name": repo,
                "pr_titles": [title],
                "pr_bodies": [body],
                "pr_states": ["open"],
                "head_branches": [head],
                "base_branches": [base],
                "head_shas": [""],  # Placeholder for SHA
                "mergeable_flags": [True],
                "merged_flags": [False],
                "pr_files": [],  # This will be populated by get_pull_request_files later
                "pr_comments": [],
                "pr_comment_users": [],
                "reviewers": [],
                "review_states": [],
                "review_events": [],
                "created_ts": [datetime.now(timezone.utc).isoformat()],
                "updated_ts": [datetime.now(timezone.utc).isoformat()],
            }
        )
        payload = {
            "status": "success",
            "message": f"Pull request #{pr_number} created successfully.",
            "pr_number": pr_number,
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
                "name": "createPullRequest",
                "description": "Creates a pull request from a head branch to a base branch.",
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
                        "title": {
                            "type": "string",
                            "description": "The title of the pull request.",
                        },
                        "body": {
                            "type": "string",
                            "description": "The body/description of the pull request.",
                        },
                        "head": {
                            "type": "string",
                            "description": "The name of the branch where your changes are implemented.",
                        },
                        "base": {
                            "type": "string",
                            "description": "The name of the branch you want your changes pulled into.",
                        },
                    },
                    "required": ["owner", "repo", "title", "body", "head", "base"],
                },
            },
        }
