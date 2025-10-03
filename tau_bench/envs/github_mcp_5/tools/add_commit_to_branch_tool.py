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

class AddCommitToBranchTool(Tool):
    """
    Add a deterministic commit to a repository branch (in-memory only).

    This tool simulates the addition of a new commit to a repository branch.
    Each commit is assigned a deterministic SHA identifier based on the repository,
    branch, and commit sequence number. Metadata fields (`created_at`, `updated_at`,
    `timestamp`) are set to CURRENT_DATE for deterministic outputs.

    Usage:
        - Provide repository name, branch name, commit message, and author.
        - A new commit entry is created unless a commit with the same message already
          exists on the same branch.

    Input Parameters:
        repo_name (str): The name of the repository.
        branch (str): The branch where the commit will be added.
        message (str): The commit message.
        author (str): The author of the commit.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A dictionary representing the created commit, including:
                - sha (str): Deterministic commit SHA (repo + branch + sequence).
                - repo (str): Repository name.
                - branch (str): Branch name.
                - message (str): Commit message.
                - author (str): Normalized author identifier.
                - timestamp (str): Commit timestamp (CURRENT_DATE).
                - created_at (str): Creation date (CURRENT_DATE).
                - updated_at (str): Last update date (CURRENT_DATE).

    Errors:
        - Returns an error if any required parameter is missing or of the wrong type.
        - Returns an error if a commit with the same message already exists on the branch.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, branch: str, message: str, author: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            branch = _validate_param({"branch": branch}, "branch", str)
            message = _validate_param({"message": message}, "message", str)
            author = _validate_param({"author": author}, "author", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        if any(
            c.get("repo") == repo_name
            and c.get("message") == message
            and c.get("branch") == branch
            for c in commits
        ):
            return _response(
                "error",
                ERROR_MESSAGES["ALREADY_EXISTS"].format(
                    entity="Commit", entity_id=message
                ),
                "ALREADY_EXISTS",
            )

        new_commit = {
            "sha": _generate_commit_sha(repo_name, branch, len(commits) + 1),
            "repo": repo_name,
            "branch": branch,
            "message": message,
            "author": _normalize_user(author),
            "timestamp": CURRENT_DATE,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        commits.append(new_commit)
        return _response("ok", new_commit)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCommitToBranch",
                "description": "Add a deterministic commit to a branch (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "message": {"type": "string"},
                        "author": {"type": "string"},
                    },
                    "required": ["repo_name", "branch", "message", "author"],
                },
            },
        }
