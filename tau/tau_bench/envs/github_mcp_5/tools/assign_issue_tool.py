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

class AssignIssueTool(Tool):
    """
    Assign one or more users to an existing issue (in-memory only).

    This tool updates the `assignees` field of a specified issue.
    Assignee identifiers are normalized via `_normalize_user`.
    The `updated_at` field is refreshed deterministically.

    Input Parameters:
        repo_name (str): The name of the repository.
        issue_id (str): Deterministic ID of the issue.
        assignees (List[str]): List of users to assign to the issue.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if assignment successful, or "error" otherwise.
            - data: Updated issue metadata with new assignees.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if the issue does not exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, issue_number: int, assignees: list[str] = None) -> str:
        if assignees is None:
            assignees = []
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            issue_number = _validate_param({"issue_number": issue_number}, "issue_number", int)
            assignees = (
                _validate_param({"assignees": assignees}, "assignees", list, required=False, subtype=str)
                or []
            )
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", {}).values()
        issue = next(
            (
                i
                for i in issues.values() if i.get("repo") == repo_name and i.get("number") == issue_number
            ),
            None,
        )

        if not issue:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Issue", entity_id=issue_number
                ),
                "NOT_FOUND",
            )

        issue["assignees"] = [_normalize_user(a) for a in assignees]
        issue["updated_at"] = CURRENT_DATE
        return _response("ok", issue)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignIssue",
                "description": "Assign users to an issue deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "assignees": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo_name", "issue_number", "assignees"],
                },
            },
        }
