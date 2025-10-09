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

class CloseIssueTool(Tool):
    """
    Close an existing issue deterministically (in-memory only).

    This tool changes the state of a specified issue to "closed" and
    stamps `closed_at` and `updated_at` fields with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        issue_id (str): Deterministic ID of the issue to close.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if closed successfully, or "error" otherwise.
            - data: Updated issue metadata.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if the issue does not exist in the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, issue_number: int) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            issue_number = _validate_param({"issue_number": issue_number}, "issue_number", int)
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

        issue["state"] = "closed"
        issue["closed_at"] = CURRENT_DATE
        issue["updated_at"] = CURRENT_DATE
        return _response("ok", issue)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CloseIssue",
                "description": "Close an existing issue deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "issue_number"],
                },
            },
        }
