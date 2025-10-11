# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ClosePullRequestTool(Tool):
    """
    Close an existing pull request deterministically (in-memory only).

    This tool updates the state of a pull request from "open" to "closed".
    The `updated_at` timestamp is refreshed with CURRENT_DATE to ensure
    deterministic outputs.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request to close.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the pull request was closed successfully, or "error" otherwise.
            - data: Updated pull request metadata, including new state and `updated_at`.

    Errors:
        - Returns an error if `repo_name` or `pr_id` are missing or invalid.
        - Returns an error if the specified pull request does not exist in the dataset.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            pr_id = _validate_param(kwargs, "pr_id", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = list(data.get("pull_requests", {}).values())
        pr = next((p for p in prs if p.get("repo") == repo_name and _safe_id(p, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"]) == pr_id), None)

        if not pr:
            return _response("error", ERROR_MESSAGES["NOT_FOUND"].format(entity="Pull Request", entity_id=pr_id), "NOT_FOUND")

        pr["state"] = "closed"
        pr["updated_at"] = CURRENT_DATE
        return _response("ok", pr)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_pull_request",
                "description": "Close a pull request deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_id": {"type": "string"},
                    },
                    "required": ["repo_name", "pr_id"],
                },
            },
        }
