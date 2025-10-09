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
    def invoke(data: dict[str, Any], repo_name: str, description: str = None, private: bool = False) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            description = _validate_param({"description": description}, "description", str, required=False)
            private = _validate_param({"private": private}, "private", bool)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        repos = data.get("repositories", {}).values()
        if any(r.get("name") == repo_name for r in repos.values()):
            return _response(
                "error",
                ERROR_MESSAGES["ALREADY_EXISTS"].format(
                    entity="Repository", entity_id=repo_name
                ),
                "ALREADY_EXISTS",
            )

        new_repo = {
            "name": repo_name,
            "description": description or "",
            "private": private,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
            "default_branch": "main",
        }
        new_repo["repo_id"] = _safe_id(new_repo, "repo_id", "REPO_", ["name"])
        data["repositories"][new_repo["repositorie_id"]] = new_repo

        return _response("ok", new_repo)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRepository",
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
