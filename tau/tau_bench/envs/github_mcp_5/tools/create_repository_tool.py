# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRepositoryTool(Tool):
    """
    Create a new repository deterministically (in-memory only).

    This tool registers a new repository in the dataset with a unique deterministic ID.
    The ID is generated using `_safe_id`, based on the repository name.
    Each repository is also stamped with `created_at`, `updated_at`, and a fixed
    `default_branch` value of "main".

    Usage:
        - Provide the repository name, visibility flag, and optionally a description.
        - If a repository with the same name already exists, an error is returned.

    Input Parameters:
        repo_name (str): The unique name of the repository.
        description (str, optional): A short description of the repository. Defaults to "".
        private (bool): Whether the repository is private.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if created successfully, or "error" otherwise.
            - data: The repository metadata, including a deterministic `repo_id`.

    Errors:
        - Returns an error if `repo_name` or `private` are missing or of the wrong type.
        - Returns an error if a repository with the given name already exists.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            description = _validate_param(kwargs, "description", str, required=False)
            private = _validate_param(kwargs, "private", bool)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        repos = list(data.get("repositories", {}).values())
        if any(r.get("name") == repo_name for r in repos):
            return _response("error", ERROR_MESSAGES["ALREADY_EXISTS"].format(entity="Repository", entity_id=repo_name), "ALREADY_EXISTS")


        new_repo = {
            "name": repo_name,
            "description": description or "",
            "private": private,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
            "default_branch": "main",
        }
        new_repo["repo_id"] = _safe_id(new_repo, "repo_id", "REPO_", ["name"])
        repos.append(new_repo)

        return _response("ok", new_repo)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_repository",
                "description": "Create a new repository deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "description": {"type": "string"},
                        "private": {"type": "boolean"},
                    },
                    "required": ["repo_name", "private"],
                },
            },
        }
