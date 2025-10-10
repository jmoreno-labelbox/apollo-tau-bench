# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateIssueTool(Tool):
    """
    Create a new issue deterministically (in-memory only).

    This tool simulates the creation of a new issue in a repository.
    IDs are generated using `_safe_id`, and metadata such as `created_at`
    and `updated_at` are stamped with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        title (str): The issue title.
        body (str): The issue description or body text.
        labels (List[str], optional): Labels for the issue (normalized to lowercase).
        assignees (List[str], optional): List of assignee identifiers.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if created successfully, or "error" otherwise.
            - data: Metadata of the created issue, including deterministic `issue_id`.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if an issue with the same title already exists.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            title = _validate_param(kwargs, "title", str)
            body = _validate_param(kwargs, "body", str)
            labels = _validate_param(kwargs, "labels", list, required=False, subtype=str) or []
            assignees = _validate_param(kwargs, "assignees", list, required=False, subtype=str) or []
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = list(data.get("issues", {}).values())
        if any(i.get("repo") == repo_name and i.get("title") == title for i in issues):
            return _response("error", ERROR_MESSAGES["ALREADY_EXISTS"].format(entity="Issue", entity_id=title), "ALREADY_EXISTS")

        new_number = len(issues) + 1
        new_issue = {
            "repo": repo_name,
            "number": new_number,
            "title": title,
            "body": body,
            "state": "open",
            "labels": [lbl.lower() for lbl in labels],
            "assignees": [_normalize_user(a) for a in assignees],
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        new_issue["issue_id"] = _safe_id(new_issue, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"])
        issues.append(new_issue)
        return _response("ok", new_issue)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_issue",
                "description": "Create a deterministic issue (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "labels": {"type": "array", "items": {"type": "string"}},
                        "assignees": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo_name", "title", "body"],
                },
            },
        }
