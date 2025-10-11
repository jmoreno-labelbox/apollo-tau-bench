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
    def invoke(data: Dict[str, Any], ) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            description = _validate_param(kwargs, "description", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        repos = list(data.get("repositories", {}).values())
        repo = next((r for r in repos if r.get("name") == repo_name), None)

        if not repo:
            return _response("error", ERROR_MESSAGES["NOT_FOUND"].format(entity="Repository", entity_id=repo_name))

        repo["description"] = description
        repo["updated_at"] = CURRENT_DATE
        return _response("ok", repo)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_repository_description",
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