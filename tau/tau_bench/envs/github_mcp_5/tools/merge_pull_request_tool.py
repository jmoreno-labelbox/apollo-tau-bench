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

class MergePullRequestTool(Tool):
    """
    Merge an existing pull request deterministically (in-memory only).

    This tool changes the state of a pull request to "merged".
    Metadata is updated with `updated_at` set to CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request to merge.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the PR was merged successfully, or "error" otherwise.
            - data: Updated pull request metadata with new state.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if the specified pull request does not exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, pr_number: int) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            pr_number = _validate_param({"pr_number": pr_number}, "pr_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = data.get("pull_requests", [])
        pr = next(
            (
                p
                for p in prs
                if p.get("repo") == repo_name and p.get("number") == pr_number
            ),
            None,
        )

        if not pr:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Pull Request", entity_id=pr_number
                ),
                "NOT_FOUND",
            )

        pr["state"] = "merged"
        pr["merged_at"] = CURRENT_DATE
        pr["updated_at"] = CURRENT_DATE
        return _response("ok", pr)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MergePullRequest",
                "description": "Merge a pull request deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"],
                },
            },
        }
