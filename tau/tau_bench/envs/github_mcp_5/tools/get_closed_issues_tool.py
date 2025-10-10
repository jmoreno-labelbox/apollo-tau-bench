# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetClosedIssuesTool(Tool):
    """
    Retrieve all closed issues for a repository deterministically.

    This tool lists issues in the dataset that are marked as "closed" for a given
    repository. Each issue is returned with a deterministic `issue_id` generated
    by `_safe_id`, normalized labels, and a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if issues were found, or "error" otherwise.
            - data: A list of closed issues with metadata, including:
                - issue_id (str): Deterministic unique issue ID.
                - title (str): The issue title.
                - state (str): The issue state ("closed").
                - assignees (List[str]): List of normalized assignee identifiers.
                - labels (List[str]): List of labels (normalized to lowercase).
                - created_at (str): Creation timestamp.
                - closed_at (str): Closing timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = list(data.get("issues", {}).values())
        closed_issues = [
            {
                "issue_id": _safe_id(i, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]),
                "title": i.get("title"),
                "labels": [lbl.lower() for lbl in i.get("labels", [])],
                "state": i.get("state"),
                "closed_at": i.get("closed_at") or CURRENT_DATE,
                "report_date": CURRENT_DATE,
            }
            for i in issues
            if i.get("repo") == repo_name and i.get("state") == "closed"
        ]
        return _response("ok", closed_issues)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_closed_issues",
                "description": "List all closed issues for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
