# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReleasesByRepositoryTool(Tool):
    """
    List all releases for a repository deterministically.

    This tool retrieves all releases associated with a given repository.
    Each release is assigned a deterministic `release_id` via `_safe_id` and
    includes a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if releases were found, or "error" otherwise.
            - data: A list of releases with metadata, including:
                - release_id (str): Deterministic unique release ID.
                - repo (str): Repository name.
                - version (str): Release version string.
                - description (str): Release description.
                - created_at (str): Creation timestamp.
                - updated_at (str): Last update timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        releases = data.get("releases", [])
        filtered = [
            {
                "release_id": _safe_id(r, "release_id", "REL_", ["repo", "version"]),
                "repo": repo_name,
                "version": r.get("version"),
                "description": r.get("description"),
                "created_at": r.get("created_at"),
                "report_date": CURRENT_DATE,
            }
            for r in releases if r.get("repo") == repo_name
        ]
        return _response("ok", filtered)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_releases_by_repository",
                "description": "List all releases for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
