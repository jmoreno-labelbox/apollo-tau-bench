# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRepositoriesTool(Tool):
    """
    List all repositories with deterministic metadata.

    This tool retrieves all repositories from the dataset and augments each entry
    with a deterministic `report_date` field set to CURRENT_DATE. It does not filter
    by name or other attributes — all repositories present in the dataset are returned.

    Usage:
        - No input parameters are required.
        - Returns metadata for every repository in the dataset.

    Input Parameters:
        None

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A list of repositories, each enriched with a `report_date` field.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        repos = list(data.get("repositories", {}).values())
        result = [{**r, "report_date": CURRENT_DATE} for r in repos]
        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_repositories",
                "description": "List all repositories with deterministic metadata.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
