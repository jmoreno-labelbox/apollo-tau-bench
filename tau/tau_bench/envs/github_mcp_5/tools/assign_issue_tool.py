# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            issue_number = _validate_param(kwargs, "issue_number", int)
            assignees = _validate_param(kwargs, "assignees", list, required=False, subtype=str) or []
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = list(data.get("issues", {}).values())
        issue = next((i for i in issues if i.get("repo") == repo_name and i.get("number") == issue_number), None)

        if not issue:
            return _response("error", ERROR_MESSAGES["NOT_FOUND"].format(entity="Issue", entity_id=issue_number), "NOT_FOUND")

        issue["assignees"] = [_normalize_user(a) for a in assignees]
        issue["updated_at"] = CURRENT_DATE
        return _response("ok", issue)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_issue",
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
