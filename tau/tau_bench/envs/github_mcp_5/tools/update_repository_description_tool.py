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

class UpdateRepositoryDescriptionTool(Tool):
    """
    Update the description of an existing repository (in-memory only).

    This tool searches for a repository by name and updates its description field.
    The `updated_at` timestamp is refreshed to the CURRENT_DATE to ensure
    deterministic versioning of repository metadata.

    Usage:
        - Provide the repository name and the new description.
        - If the repository is not found, an error response is returned.

    Input Parameters:
        repo_name (str): The unique name of the repository to update.
        description (str): The new description text for the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the update was successful, or "error" otherwise.
            - data: The updated repository metadata, including the refreshed `updated_at` field.

    Errors:
        - Returns an error if `repo_name` or `description` are missing or of the wrong type.
        - Returns an error if the repository with the given name does not exist.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, description: str = None) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            description = _validate_param({"description": description}, "description", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        repos = data.get("repositories", [])
        repo = next((r for r in repos if r.get("name") == repo_name), None)

        if not repo:
            return _response(
                "error",
                ERROR_MESSAGES["NOT_FOUND"].format(
                    entity="Repository", entity_id=repo_name
                ),
            )

        repo["description"] = description
        repo["updated_at"] = CURRENT_DATE
        return _response("ok", repo)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateRepositoryDescription",
                "description": "Update a repository description deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["repo_name", "description"],
                },
            },
        }
