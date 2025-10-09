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

class GetPullRequestMetadataTool(Tool):
    """
    Retrieve deterministic metadata for a pull request by ID.

    This tool searches for a pull request by its deterministic ID (`pr_id`)
    and returns its metadata, augmented with a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if found, or "error" otherwise.
            - data: A dictionary with pull request metadata, including deterministic `pr_id`.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if no pull request with the given ID exists.
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

        result = {
            **pr,
            "pr_id": _safe_id(
                pr, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"]
            ),
            "report_date": CURRENT_DATE,
        }
        if "author" in result:
            result["author"] = _normalize_user(result["author"])
        if "reviewers" in result:
            result["reviewers"] = [
                _normalize_user(r) for r in result.get("reviewers", [])
            ]

        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPullRequestMetadata",
                "description": "Retrieve deterministic metadata for a pull request by number.",
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
