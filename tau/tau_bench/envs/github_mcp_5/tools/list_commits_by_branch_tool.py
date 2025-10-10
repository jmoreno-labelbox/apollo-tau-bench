# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCommitsByBranchTool(Tool):
    """
    List commits for a repository branch deterministically.

    This tool retrieves all commits for a given repository branch and augments
    each commit with a deterministic `report_date` field. Author fields are
    normalized with `_normalize_user` to ensure consistent outputs.

    Usage:
        - Provide the repository name and branch name.
        - Returns metadata for all commits matching that repository and branch.

    Input Parameters:
        repo_name (str): The name of the repository.
        branch (str): The branch name within the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A list of commits, each represented as a dictionary with:
                - commit_id (str): The commit SHA identifier.
                - repo (str): The repository name.
                - branch (str): The branch name.
                - message (str): The commit message.
                - author (str): The normalized author identifier.
                - timestamp (str): The commit timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` or `branch` are missing or of the wrong type.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            branch = _validate_param(kwargs, "branch", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = list(data.get("commits", {}).values())
        branch_commits = [
            {
                "commit_id": c.get("sha"),
                "repo": repo_name,
                "branch": branch,
                "message": c.get("message"),
                "author": _normalize_user(c.get("author")),
                "timestamp": c.get("timestamp"),
                "report_date": CURRENT_DATE,
            }
            for c in commits
            if c.get("repo") == repo_name and c.get("branch") == branch
        ]
        return _response("ok", branch_commits)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_commits_by_branch",
                "description": "List commits for a repository branch deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }
