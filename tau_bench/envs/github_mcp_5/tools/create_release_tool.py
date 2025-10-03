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

class CreateReleaseTool(Tool):
    """
    Create a new release deterministically (in-memory only).

    This tool simulates the creation of a new release in a repository.
    IDs are generated via `_safe_id` using repository name and version.
    Metadata is stamped with CURRENT_DATE for deterministic behavior.

    Input Parameters:
        repo_name (str): The name of the repository.
        version (str): Version identifier for the release.
        description (str): Description of the release contents.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the release was created successfully, or "error" otherwise.
            - data: Metadata of the created release, including deterministic `release_id`.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if a release with the same version already exists for the repository.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str, version: str, description: str,
    name: Any = None,
    ) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
            version = _validate_param({"version": version}, "version", str)
            description = _validate_param({"description": description}, "description", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        releases = data.get("releases", [])
        if any(
            r.get("repo") == repo_name and r.get("version") == version for r in releases
        ):
            return _response(
                "error",
                ERROR_MESSAGES["ALREADY_EXISTS"].format(
                    entity="Release", entity_id=version
                ),
                "ALREADY_EXISTS",
            )

        new_release = {
            "repo": repo_name,
            "version": version,
            "description": description,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        new_release["release_id"] = _safe_id(
            new_release, "release_id", "REL_", ["repo", "version"]
        )
        releases.append(new_release)
        return _response("ok", new_release)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRelease",
                "description": "Create a new deterministic release (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "version": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["repo_name", "version", "description"],
                },
            },
        }
