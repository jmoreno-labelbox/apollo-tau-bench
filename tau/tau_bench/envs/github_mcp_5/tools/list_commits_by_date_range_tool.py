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

class ListCommitsByDateRangeTool(Tool):
    """
    List commits for a repository within a deterministic date range.

    This tool retrieves all commits in a given repository that fall within a
    specified inclusive date range. Each commit is augmented with a deterministic
    `report_date` field. Authors are normalized using `_normalize_user`.

    Usage:
        - Provide the repository name, start date, and end date.
        - Dates must be provided in ISO 8601 format (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS).
        - Returns metadata for all commits whose timestamps fall within the range.

    Input Parameters:
        repo_name (str): The name of the repository.
        start_date (str): The start date of the range (inclusive).
        end_date (str): The end date of the range (inclusive).

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A list of commits, each represented as a dictionary with:
                - commit_id (str): The commit SHA identifier.
                - repo (str): The repository name.
                - message (str): The commit message.
                - author (str): The normalized author identifier.
                - timestamp (str): The commit timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name`, `start_date`, or `end_date` are missing or invalid types.
        - Returns an error if no commits match the specified date range.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, start_date: str, end_date: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            start_date = _validate_param({"start_date": start_date}, "start_date", str)
            end_date = _validate_param({"end_date": end_date}, "end_date", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        filtered = [
            {
                "commit_id": c.get("sha"),
                "repo": repo_name,
                "message": c.get("message"),
                "author": _normalize_user(c.get("author")),
                "timestamp": c.get("timestamp"),
                "report_date": CURRENT_DATE,
            }
            for c in commits
            if c.get("repo") == repo_name
            and start_date <= c.get("timestamp", "") <= end_date
        ]
        return _response("ok", filtered)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCommitsByDateRange",
                "description": "List commits for a repository between a start and end date (deterministic).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["repo_name", "start_date", "end_date"],
                },
            },
        }
