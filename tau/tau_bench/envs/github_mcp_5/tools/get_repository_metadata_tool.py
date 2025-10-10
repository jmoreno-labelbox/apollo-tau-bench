# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepositoryMetadataTool(Tool):
    """
    Retrieve deterministic metadata for a specific repository by name.

    This tool searches the dataset for a repository with the given name and
    returns its metadata, augmented with a deterministic `report_date` field.

    Usage:
        - Provide the repository name as input.
        - Returns a JSON response with the repository metadata or an error if not found.

    Input Parameters:
        repo_name (str): The name of the repository to look up.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if found, "error" otherwise.
            - data: Repository metadata with deterministic `report_date`.

    Errors:
        - Returns an error response if `repo_name` is missing or not a string.
        - Returns an error if no repository with the given name exists in the dataset.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        repos = list(data.get("repositories", {}).values())
        repo_info = next((r for r in repos if r.get("name") == repo_name), None)

        if not repo_info:
            return _response("error", ERROR_MESSAGES["NOT_FOUND"].format(entity="Repository", entity_id=repo_name), "NOT_FOUND")

        result = {
            **repo_info,
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository_metadata",
                "description": "Get deterministic metadata for a repository by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
