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

class ListIssuesByLabelTool(Tool):
    """
    List issues in a repository filtered by label.

    This tool retrieves all issues in a repository that contain a given label.
    Labels are normalized to lowercase to ensure deterministic matching.

    Input Parameters:
        repo_name (str): The name of the repository.
        label (str): The label to filter issues by.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: List of issues with the specified label, including:
                - issue_id (str): Deterministic unique issue ID.
                - title (str): The issue title.
                - state (str): The issue state.
                - assignees (List[str]): Normalized assignee identifiers.
                - labels (List[str]): Normalized labels.
                - created_at (str): Creation date.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if parameters are missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, label: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            label = _validate_param({"label": label}, "label", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", [])
        labeled = [
            {
                "issue_id": _safe_id(
                    i, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]
                ),
                "title": i.get("title"),
                "labels": [lbl.lower() for lbl in i.get("labels", [])],
                "state": i.get("state"),
                "report_date": CURRENT_DATE,
            }
            for i in issues
            if i.get("repo") == repo_name
            and label.lower() in [lbl.lower() for lbl in i.get("labels", [])]
        ]
        return _response("ok", labeled)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListIssuesByLabel",
                "description": "Retrieve issues by label for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "label": {"type": "string"},
                    },
                    "required": ["repo_name", "label"],
                },
            },
        }
