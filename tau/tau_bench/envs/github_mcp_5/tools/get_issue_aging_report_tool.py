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

class GetIssueAgingReportTool(Tool):
    """
    Generate a deterministic aging report for issues in a repository.

    This tool calculates how many days each issue has been open based on its
    `created_at` date compared to CURRENT_DATE. It provides insights into
    long-standing or unresolved issues.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: List of issues with their aging information, including:
                - issue_id (str): Deterministic issue identifier.
                - title (str): Issue title.
                - state (str): Current issue state.
                - created_at (str): Issue creation date.
                - days_open (int): Number of days the issue has been open.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", {}).values()
        aging = [
            {
                "issue_id": _safe_id(
                    i, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]
                ),
                "title": i.get("title"),
                "state": i.get("state"),
                "created_at": i.get("created_at"),
                "days_open": (
                    _days_between(i.get("created_at", CURRENT_DATE), CURRENT_DATE)
                    if i.get("state") == "open"
                    else 0
                ),
                "report_date": CURRENT_DATE,
            }
            for i in issues.values() if i.get("repo") == repo_name
        ]
        return _response("ok", aging)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetIssueAgingReport",
                "description": "Generate deterministic report of how long issues have been open.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
