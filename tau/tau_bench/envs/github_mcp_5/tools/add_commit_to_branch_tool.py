# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _validate_param(
    kwargs: Dict[str, Any],
    param: str,
    expected_type: type,
    required: bool = True,
    subtype: type = None
) -> Any:
    """
    Validate and retrieve a parameter from keyword arguments.

    Performs deterministic validation on the presence and type of a parameter,
    with optional subtype checks when the parameter is a list.

    Args:
        kwargs (Dict[str, Any]): Dictionary of keyword arguments to validate.
        param (str): The name of the parameter to validate.
        expected_type (type): Expected top-level type of the parameter (e.g., str, list).
        required (bool, optional): Whether the parameter is required. Defaults to True.
        subtype (type, optional): Expected element type if the parameter is a list.
            For example, subtype=str enforces that all elements in the list are strings.

    Returns:
        Any: The validated parameter value if present and valid, or None if not required.
             On validation failure, returns a standardized error response.
    """
    value = kwargs.get(param)

    if required and value is None:
        return _response(
            "error",
            ERROR_MESSAGES["REQUIRED_PARAMETER"].format(param=param)
        )

    if value is not None and not isinstance(value, expected_type):
        return _response(
            "error",
            ERROR_MESSAGES["INVALID_PARAMETER_TYPE"].format(
                param=param,
                expected_type=expected_type.__name__
            )
        )

    if subtype and isinstance(value, list):
        for item in value:
            if not isinstance(item, subtype):
                return _response(
                    "error",
                    f"Parameter '{param}' must be a list of {subtype.__name__}."
                )

    return value

def _response(status: str, data_or_message: Any, error_code: str = None) -> str:
    """
    Build a standardized JSON response.

    Args:
        status (str): Response status, either "ok" or "error".
        data_or_message (Any): Data payload when status is "ok", or error message when status is "error".
        error_code (str, optional): Machine-friendly error code to include when status is "error".

    Returns:
        str: A JSON-formatted string containing either:
             {"status": "ok", "data": ...}
             or {"status": "error", "error_code": ..., "message": ...},
             indented for readability.
    """
    if status == "ok":
        return json.dumps({"status": "ok", "data": data_or_message}, indent=2)
    return json.dumps(
        {
            "status": "error",
            "error_code": error_code or "UNKNOWN_ERROR",
            "message": data_or_message,
        },
        indent=2,
    )

def _normalize_user(user: Any) -> str:
    """
    Normalize user identifiers for deterministic outputs.

    Args:
        user (Any): Raw user field (string, int, or None).

    Returns:
        str: Stringified user identifier, or "unknown" if empty/None.
    """
    return str(user) if user else "unknown"

def _generate_commit_sha(repo: str, branch: str, seq: int) -> str:
    """
    Generate a deterministic 12-character hexadecimal SHA for commits.

    Args:
        repo (str): Repository name.
        branch (str): Branch name.
        seq (int): Sequential number of the commit.

    Returns:
        str: Deterministic 12-character hexadecimal SHA.
    """
    seed = f"{repo}_{branch}_{seq}"
    return hashlib.sha1(seed.encode()).hexdigest()[:12]

class AddCommitToBranchTool(Tool):
    """
    Add a deterministic commit to a repository branch (in-memory only).

    This tool simulates the addition of a new commit to a repository branch.
    Each commit is assigned a deterministic SHA identifier based on the repository,
    branch, and commit sequence number. Metadata fields (`created_at`, `updated_at`,
    `timestamp`) are set to CURRENT_DATE for deterministic outputs.

    Usage:
        - Provide repository name, branch name, commit message, and author.
        - A new commit entry is created unless a commit with the same message already
          exists on the same branch.

    Input Parameters:
        repo_name (str): The name of the repository.
        branch (str): The branch where the commit will be added.
        message (str): The commit message.
        author (str): The author of the commit.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A dictionary representing the created commit, including:
                - sha (str): Deterministic commit SHA (repo + branch + sequence).
                - repo (str): Repository name.
                - branch (str): Branch name.
                - message (str): Commit message.
                - author (str): Normalized author identifier.
                - timestamp (str): Commit timestamp (CURRENT_DATE).
                - created_at (str): Creation date (CURRENT_DATE).
                - updated_at (str): Last update date (CURRENT_DATE).

    Errors:
        - Returns an error if any required parameter is missing or of the wrong type.
        - Returns an error if a commit with the same message already exists on the branch.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            branch = _validate_param(kwargs, "branch", str)
            message = _validate_param(kwargs, "message", str)
            author = _validate_param(kwargs, "author", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = list(data.get("commits", {}).values())
        if any(c.get("repo") == repo_name and c.get("message") == message and c.get("branch") == branch for c in commits):
            return _response("error", ERROR_MESSAGES["ALREADY_EXISTS"].format(entity="Commit", entity_id=message), "ALREADY_EXISTS")

        new_commit = {
            "sha": _generate_commit_sha(repo_name, branch, len(commits) + 1),
            "repo": repo_name,
            "branch": branch,
            "message": message,
            "author": _normalize_user(author),
            "timestamp": CURRENT_DATE,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        commits.append(new_commit)
        return _response("ok", new_commit)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_commit_to_branch",
                "description": "Add a deterministic commit to a branch (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "message": {"type": "string"},
                        "author": {"type": "string"},
                    },
                    "required": ["repo_name", "branch", "message", "author"],
                },
            },
        }